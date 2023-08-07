import re
import time
from datetime import datetime, timedelta, timezone
from typing import List, Optional

import click
from rich.console import Console

import coiled

from ..utils import CONTEXT_SETTINGS

COLORS = [
    "green",
    "yellow",
    "blue",
    "magenta",
    "cyan",
]


@click.command(
    context_settings=CONTEXT_SETTINGS,
)
@click.option(
    "--account",
    default=None,
    help="Coiled account (uses default account if not specified)",
)
@click.option(
    "--cluster",
    default=None,
    help="Cluster for which to show logs, default is most recent",
)
@click.option(
    "--no-scheduler",
    default=False,
    is_flag=True,
    help="Don't include scheduler logs",
)
@click.option(
    "--workers",
    default="all",
    help=(
        "All worker logs included by default, specify 'none' or "
        "comma-delimited list of names, states, or internal IP addresses"
    ),
)
@click.option(
    "--label",
    default="private_ip_address",
    type=click.Choice(
        ["private_ip_address", "name", "id", "public_ip_address", "none"],
        case_sensitive=False,
    ),
)
@click.option(
    "--system",
    default=False,
    is_flag=True,
    help="Just show system logs",
)
@click.option(
    "--combined",
    default=False,
    is_flag=True,
    help="Show combined system and dask logs",
)
@click.option(
    "--tail",
    default=False,
    is_flag=True,
    help="Keep tailing logs",
)
@click.option(
    "--since",
    default=None,
    help="By default will show logs from start of cluster (or 30s ago if tailing)",
)
@click.option(
    "--until",
    default=None,
    help="Show logs up to and including this time, by default will go through present time.",
)
@click.option(
    "--color",
    default=False,
    is_flag=True,
    help="Use for color in logs",
)
@click.option(
    "--show-all-timestamps",
    default=False,
    is_flag=True,
    help="Prepend datetime to all log messages",
)
@click.option(
    "--interval",
    default=3,
    help="Tail polling interval",
)
def better_logs(
    account: Optional[str],
    cluster: Optional[str],
    no_scheduler: bool,
    workers: str,
    label: str,
    system: bool,
    combined: bool,
    tail: bool,
    interval: int,
    since: Optional[str],
    until: Optional[str],
    color: bool,
    show_all_timestamps: bool,
):
    console = Console(force_terminal=color)

    dask = not system or combined
    system = system or combined
    label = label.lower()

    if tail and until:
        raise click.ClickException("You can't use --until when tailing logs.")

    with coiled.Cloud(account=account) as cloud:
        if cluster and cluster.isnumeric():
            cluster_id = int(cluster)
        elif cluster:
            # get cluster by name
            try:
                clusters = cloud.get_clusters_by_name(name=cluster)
                if clusters:
                    recent_cluster = clusters[-1]
                else:
                    raise click.ClickException(
                        f"Unable to find cluster with name '{cluster}'"
                    )

                if tail and recent_cluster["current_state"]["state"] in (
                    "stopped",
                    "error",
                ):
                    tail = False
                    console.print(
                        f"[red]Cluster state is {recent_cluster['current_state']['state']} so not tailing.[/red]"
                    )

                cluster_id = recent_cluster["id"]

            except coiled.errors.DoesNotExist:
                cluster_id = None
        else:
            # default to most recent cluster
            clusters = coiled.list_clusters(max_pages=1)
            if not clusters:
                raise ValueError("Unable to find any clusters for your account")
            match = max(clusters, key=lambda c: c["id"])
            cluster_id = match["id"]

        if not cluster_id:
            raise click.ClickException(f"Unable to find cluster `{cluster}`")

        cluster_info = cloud.cluster_details(cluster_id)

    # instance ID's for which to show logs, key maps to label to use
    instances = {}
    if not no_scheduler and cluster_info.get("scheduler", {}).get("instance"):
        scheduler_id = cluster_info["scheduler"]["instance"]["id"]
        instances[scheduler_id] = {
            "label": "scheduler" if label != "none" else "",
            "color": COLORS[-1],
        }

    def worker_label(worker: dict):
        if label == "none":
            return ""
        return (
            worker.get("name", str(worker["instance"]["id"]))
            if label == "name"
            else worker["instance"].get(label, str(worker["instance"]["id"]))
        )

    # TODO when tailing "all" workers, this won't include workers that appear after we start
    #  (addressing this is future enhancement)

    if workers:
        worker_attrs_to_match = workers.split(",")

        def filter_worker(worker):
            if worker.get("name") and worker["name"] in worker_attrs_to_match:
                # match on name
                return True
            elif (
                worker.get("instance", {}).get("private_ip_address")
                and worker["instance"]["private_ip_address"] in worker_attrs_to_match
            ):
                # match on private IP
                return True
            elif (
                worker.get("current_state", {}).get("state")
                and worker["current_state"]["state"] in worker_attrs_to_match
            ):
                # match on state
                return True

            return False

        instances.update(
            {
                worker["instance"]["id"]: dict(
                    label=worker_label(worker), color=COLORS[idx % len(COLORS)]
                )
                for idx, worker in enumerate(cluster_info["workers"])
                if worker.get("instance")
                and (workers == "all" or filter_worker(worker))
            }
        )

    show_all_instances = workers == "all" and not no_scheduler

    console.print(f"=== Logs for {cluster_info['name']} ({cluster_id}) ===\n")

    from_timestamp = ts_ms_from_string(since)
    until_timestamp = ts_ms_from_string(until)
    last_events = set()

    if tail and not from_timestamp:
        # for tail, start with logs from 30s ago if start isn't specified
        current_ms = int(time.time_ns() // 1e6)
        from_timestamp = current_ms - (30 * 1000)

    while True:
        events = coiled.better_cluster_logs(
            cluster_id=cluster_id,
            # function returns all instances if none specified, we'll use that
            # in order to not exclude instances that show up while tailing
            instance_ids=None if show_all_instances else list(instances.keys()),
            dask=dask,
            system=system,
            since_ms=from_timestamp,
            until_ms=until_timestamp,
        )

        if last_events:
            events = [
                e
                for e in events
                if e["timestamp"] != from_timestamp
                or event_dedupe_key(e) not in last_events
            ]

        if events:
            print_events(
                console, events, instances, show_all_timestamps=show_all_timestamps
            )

            from_timestamp = events[-1]["timestamp"]
            last_events = {
                event_dedupe_key(e) for e in events if e["timestamp"] == from_timestamp
            }

        if tail:
            # TODO stop tailing once cluster is stopped/errored (future MR)
            time.sleep(interval)
        else:
            break


def match_cluster(clusters: List[dict], cluster: str) -> dict:
    if cluster.isnumeric():
        matches = [c for c in clusters if c["id"] == int(cluster)]
        if len(matches) == 1:
            return matches[0]
        elif len(matches) > 1:
            raise ValueError(f"Multiple clusters match '{cluster}'")

    # try to match on cluster name
    matches = sorted(
        [c for c in clusters if c["name"] == cluster], key=lambda c: c["id"]
    )
    if matches:
        return matches[-1]

    raise ValueError(f"No clusters match '{cluster}'")


def event_dedupe_key(event):
    return f'{event["timestamp"]}#{event["instance_id"]}#{event["message"]}'


def print_events(
    console, events, instances: dict, pretty=True, show_all_timestamps=False
):
    for e in events:
        console.print(
            format_log_event(
                e, instances, pretty=pretty, show_all_timestamps=show_all_timestamps
            )
        )


def format_log_event(
    event: dict, instances: dict, pretty: bool, show_all_timestamps: bool
) -> str:
    message = event["message"]
    label = instances[event["instance_id"]]["label"]
    color = instances[event["instance_id"]]["color"]

    time_string = ""

    if event.get("timestamp"):
        time_format = "%Y-%m-%d %H:%M:%S.%f"
        t = datetime.utcfromtimestamp(event["timestamp"] / 1000)

        if show_all_timestamps or not message_has_timestamp(message, t):
            time_string = f"{t.strftime(time_format)} "

    # indent multiline log messages
    if "\n" in message:
        message = message.replace("\n", "\n  ")

    if label:
        formatted_label = (
            f"[{color}]({label})[/{color}] \t" if pretty else f"({label}) \t"
        )
    else:
        formatted_label = ""

    return f"{formatted_label}{time_string}{message}"


def message_has_timestamp(message: str, t: datetime):
    # naively check if timestamp already present in message by looking for year
    # if it's not in log message, then prepend
    if str(t.year) in message:
        return True


def ts_ms_from_string(timestring: Optional[str]) -> Optional[int]:
    # input can be
    #   int: timestamp (ms)
    #   string in ISO 8601 format
    #   string representing delta (e.g, "1h15m")

    if not timestring:
        return None

    if timestring.isnumeric():
        return int(timestring)

    delta_regex = re.compile(
        r"^((?P<days>\d+)d)?((?P<hours>\d+)h)?((?P<minutes>\d+)m)?((?P<seconds>\d+)s)?$"
    )
    match = delta_regex.match(timestring)
    if match:
        match_parts = {key: int(val) for key, val in match.groupdict().items() if val}

        delta = timedelta(**match_parts)
        if delta:
            t = datetime.now(tz=timezone.utc) - delta
            return int(t.timestamp() * 1000)

    try:
        t = datetime.fromisoformat(timestring)
        # interpret as UTC if not specified (rather than local time)
        if t.tzinfo is None:
            t = t.replace(tzinfo=timezone.utc)
    except ValueError:
        pass
    else:
        return int(t.timestamp() * 1000)

    raise ValueError(
        f"Unable to convert '{timestring}' into a timestamp, you can use number (timestamp in ms), "
        f"ISO format, or delta such as 5m."
    )
