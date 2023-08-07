import os
import shutil
import subprocess
import sys
import tempfile
import time
from typing import Optional

import click
import dask
import rich.panel
from rich import print
from rich.prompt import Confirm

import coiled

from ..utils import CONTEXT_SETTINGS
from .util import setup_failure

# names to use when tracking actions
ACTION_INIT = "init"
ACTION_CREATE_GAR = "gar:create"
ACTION_BIND_GAR = "gar:policy-binding"
ACTION_BIND_POLICY = "policy-binding"
ACTION_CREATE_ROLE = "roles-create"
ACTION_LIST_KEYS = "keys-list"
ACTION_ENABLE_SERVICE = "services-enable"
ACTION_CREATE_SA = "service-accounts-create"
ACTION_ACTIVATE_SA = "activate-servicer-account"
ACTION_CREATE_KEY = "keys-create"


CONTROL_PLANE_ROLE = """
title: coiled
description: used by Coiled control-plane for creating infrastructure and clusters
stage: GA
includedPermissions:
- bigquery.datasets.create
- bigquery.jobs.create
- bigquery.datasets.get
- bigquery.datasets.update
- compute.acceleratorTypes.list
- compute.addresses.list
- compute.disks.create
- compute.disks.delete
- compute.disks.list
- compute.disks.useReadOnly
- compute.firewalls.create
- compute.firewalls.delete
- compute.firewalls.get
- compute.firewalls.list
- compute.globalOperations.get
- compute.globalOperations.getIamPolicy
- compute.globalOperations.list
- compute.images.create
- compute.images.delete
- compute.images.get
- compute.images.list
- compute.images.setLabels
- compute.images.useReadOnly
- compute.instances.create
- compute.instances.delete
- compute.instances.get
- compute.instances.getSerialPortOutput
- compute.instances.list
- compute.instances.setLabels
- compute.instances.setMetadata
- compute.instances.setServiceAccount
- compute.instances.setTags
- compute.instanceTemplates.create
- compute.instanceTemplates.delete
- compute.instanceTemplates.get
- compute.instanceTemplates.useReadOnly
- compute.machineTypes.get
- compute.machineTypes.list
- compute.networks.create
- compute.networks.delete
- compute.networks.get
- compute.networks.list
- compute.networks.updatePolicy
- compute.projects.get
- compute.projects.setCommonInstanceMetadata
- compute.regionOperations.get
- compute.regionOperations.list
- compute.regions.get
- compute.regions.list
- compute.routers.create
- compute.routers.delete
- compute.routers.get
- compute.routers.list
- compute.routers.update
- compute.routes.delete
- compute.routes.list
- compute.subnetworks.create
- compute.subnetworks.delete
- compute.subnetworks.get
- compute.subnetworks.getIamPolicy
- compute.subnetworks.list
- compute.subnetworks.use
- compute.subnetworks.useExternalIp
- compute.zoneOperations.get
- compute.zoneOperations.list
- compute.zones.list
- iam.serviceAccounts.actAs
- logging.buckets.create
- logging.buckets.get
- logging.buckets.list
- logging.logEntries.create
- logging.logEntries.list
- logging.sinks.create
- logging.sinks.get
- logging.sinks.list
- storage.buckets.create
- storage.buckets.get
- storage.objects.create
- storage.objects.get
- storage.objects.list
- storage.objects.update
"""


DATA_ROLE = """
title: coiled-data
description: service account attached to cluster instances for data access
stage: GA
includedPermissions:
- logging.logEntries.create
- storage.buckets.get
- storage.buckets.create
- storage.objects.create
- storage.objects.get
- storage.objects.list
- storage.objects.update
"""


def has_gcloud():
    return bool(shutil.which("gcloud"))


def gcloud_wrapper(
    command: str,
    show_stdout: bool = False,
    interactive: bool = False,
    error_handler=None,
    action_name: Optional[str] = None,
):
    p = subprocess.run(command.split(" "), capture_output=not interactive)

    stdout = p.stdout.decode() if p.stdout else None
    stderr = p.stderr.decode() if p.stderr else None

    if action_name:
        coiled.add_interaction(
            action=f"gcloud:{action_name}",
            success=p.returncode == 0,
            command=command,
            return_code=p.returncode,
            additional_text=stdout or None,
            error_message=stderr or None,
        )

    if show_stdout:
        print(stdout)

    if p.returncode:
        if stderr and "already exist" in stderr:
            pass

        elif error_handler and error_handler(stderr):
            # error_handler returns True if error was handled
            return False

        else:
            print(f"[red]gcloud returned an error when running command `{command}`:")
            print(rich.panel.Panel(stderr or ""))
            setup_failure(
                f"gcloud error while running {command}, {stderr}", backend="gcp"
            )
            sys.exit(1)

    return True


def gcloud_enable_service(service: str, project: str):
    command = f"gcloud services enable {service} --project {project}"

    def enable_error_handler(stderr: str):
        if "Billing must be enabled" in stderr:
            print(
                f"[red]We couldn't enable {service} because of an error "
                "related to Google Cloud billing:"
            )
            print(rich.panel.Panel(stderr))
            print(
                "To address this error, please link this project to a "
                "Google Cloud billing account at"
            )
            print()
            print(f"[link]https://console.cloud.google.com/billing?project={project}")
            print()
            print("and then re-run [green]coiled setup gcp[/green]")
            # we've handled the error
            setup_failure("Billing not enabled", backend="gcp")
            return True

        return False

    return gcloud_wrapper(
        command,
        error_handler=enable_error_handler,
        action_name=f"{ACTION_ENABLE_SERVICE}:{service}",
    )


def gcloud_make_key(iam_email: str, key_path: str):
    command = (
        f"gcloud iam service-accounts keys create {key_path} --iam-account {iam_email}"
    )
    p = subprocess.run(command.split(" "), capture_output=True)

    # TODO track interaction
    stdout = p.stdout.decode()
    stderr = p.stderr.decode()

    coiled.add_interaction(
        action=f"gcloud:{ACTION_CREATE_KEY}",
        success=p.returncode == 0,
        command=command,
        return_code=p.returncode,
        additional_text=stdout or None,
        error_message=stderr or None,
    )

    if p.returncode:
        if "service-accounts.keys.create" in stderr and "FAILED_PRECONDITION" in stderr:
            print(
                "[red]An error occurred when attempting to create a key "
                "for the IAM account[/red]"
            )
            print(stderr)
            print(
                "One possibility is that you already have 10 keys for this account. "
                "Existing keys:"
            )
            print()
            gcloud_wrapper(
                f"gcloud iam service-accounts keys list --iam-account={iam_email}",
                show_stdout=True,
                action_name=ACTION_LIST_KEYS,
            )
            print()
            print("You can delete individual keys by running:")
            print()
            print(
                "[green]gcloud iam service-accounts keys delete "
                f"--iam-account={iam_email} [bold]<key_id>[/bold]"
            )
            setup_failure(
                f"Service account key creation failed {stderr}", backend="gcp"
            )
            return False
        else:
            raise

    return True


def get_gcloud_config(key) -> Optional[str]:
    p = subprocess.run(f"gcloud config get {key}".split(" "), capture_output=True)

    if not p.returncode:
        return p.stdout.decode().strip()
    else:
        print(p.stderr)
        return None


def gcloud_wait_for_repo(region: str, key_path: str) -> bool:
    # it takes a while to give the service account (which we created)
    # access to the artifact registry
    # this function waits (with timeout) until that's ready

    # keep track of currently active account (for local `gcloud`) so we can switch back
    previous_account = get_gcloud_config("account")

    # activate the service account we made --
    # subsequent `gcloud` calls with be using those creds
    gcloud_wrapper(
        f"gcloud auth activate-service-account --key-file {key_path}",
        action_name=ACTION_ACTIVATE_SA,
    )

    success = False
    command = f"gcloud artifacts repositories describe coiled --location {region}"
    t0 = time.time()

    # keep checking if service account has access to artifact registry
    while True:
        p = subprocess.run(command.split(" "), capture_output=True)

        if "format: DOCKER" in p.stdout.decode():
            success = True
            break
        elif "PERMISSION_DENIED" in p.stderr.decode():
            if time.time() < t0 + 180:  # wait for up to three minutes
                time.sleep(10)  # 10s delay between retries
                continue
            else:
                break
        else:
            print(
                "[red]An unexpected error occurred while waiting for "
                "Google Artifact Registry to be ready."
            )
            print(rich.panel.Panel(p.stderr.decode()))
            break

    # switch back to the user's account for local `gcloud` commands
    gcloud_wrapper(f"gcloud config set account {previous_account}")
    return success


@click.option(
    "--region",
    default="us-east1",
    help="GCP region to use when setting up your VPC/subnets",
)
@click.option(
    "--skip-gar",
    default=False,
    is_flag=True,
    help="Don't setup Google Artifact Registry",
)
@click.option(
    "--manual-final-setup",
    default=False,
    is_flag=True,
    help="Don't automatically send credentials to Coiled, "
    "finish setup manually in the web UI",
)
@click.option(
    "-y",
    "--yes",
    default=False,
    is_flag=True,
    help="Don't prompt for confirmation, just do it!",
)
@click.command(context_settings=CONTEXT_SETTINGS)
def gcp_setup(region, skip_gar, manual_final_setup, yes):
    do_setup(region, skip_gar, manual_final_setup, yes)


def do_setup(region=None, skip_gar=False, manual_final_setup=False, yes=False):
    try:
        import getpass
        import socket

        local_user = f"{getpass.getuser()}@{socket.gethostname()}"
    except Exception:
        local_user = ""

    coiled.add_interaction(
        action="CliSetupGcp",
        success=True,
        local_user=local_user,
        # use keys that match the cli args
        region=region,
        yes=yes,
    )

    if not has_gcloud():
        print(
            "[red]The `gcloud` CLI was not found. "
            "This is required for coiled setup gcp."
        )
        print(
            "See [link]https://cloud.google.com/sdk/docs/install[/link] for "
            "`gcloud` installation instructions."
        )
        setup_failure("Gcloud cli missing", backend="gcp")
        return False

    project = get_gcloud_config("project")

    if not project:
        print("No project was set, so you'll need to select or create one...")
        gcloud_wrapper("gcloud init", interactive=True, action_name=ACTION_INIT)

    project = get_gcloud_config("project")
    if not project:
        print("[red]There's still no project set so aborting Coiled setup.")
        setup_failure("No project was set", backend="gcp")
        return False

    region = region or get_gcloud_config("compute/region")

    if not region:
        print(
            "No region is set, you'll need to specify region like so:\n"
            "[green]coiled setup gcp --region us-central1[/green]"
        )
        setup_failure("Region was not set", backend="gcp")
        return False

    base_account_name = "coiled"

    main_sa = base_account_name
    data_sa = f"{base_account_name}-data"
    main_role = base_account_name
    data_role = f"{base_account_name}_data"
    gar_name = "coiled"  # this is what control-plane expects

    main_email = f"{main_sa}@{project}.iam.gserviceaccount.com"
    data_email = f"{data_sa}@{project}.iam.gserviceaccount.com"

    resource_description = (
        f"Proposed region for Coiled:\t[green]{region}[/green]\t"
        f"(use `coiled setup gcp --region` to change)\n"
        f"Proposed project for Coiled:\t[green]{project}[/green]\t"
        f"(use `gcloud config set project <project_name>` to set)\n"
        "\n"
        "[bold]The following IAM resources will be created:[/bold]\n"
        "\n"
        f"Service account for creating clusters:\t[green]{main_sa}[/green]\n"
        f"Service account for data access:\t[green]{data_sa}[/green]\n"
        f"IAM Role:\t\t[green]{main_role}[/green] "
        f"(for [green]{main_sa}[/green] service account)\n"
        f"IAM Role:\t\t[green]{data_role}[/green] "
        f"(for [green]{data_sa}[/green] service account)"
    )

    if not skip_gar:
        resource_description += (
            "\n"
            f"Artifact Registry:\t[green]{gar_name}[/green] in region {region}\n"
            "                   \t(use `coiled setup gcp --skip-gar "
            "--manual-final-setup` to configure "
            "Coiled with a different container registry)"
        )

    print(rich.panel.Panel(resource_description))

    if not yes and not Confirm.ask(
        "Proceed with Google Cloud IAM setup for Coiled?", default=True
    ):
        return False

    with tempfile.TemporaryDirectory() as dir:
        main_file = os.path.join(dir, f"{main_role}.yaml")
        with open(main_file, "w") as f:
            f.write(CONTROL_PLANE_ROLE)

        data_file = os.path.join(dir, f"{data_role}.yaml")
        with open(data_file, "w") as f:
            f.write(DATA_ROLE)

        gcloud_wrapper(
            f"gcloud iam roles create {main_role} "
            f"--project={project} --file {main_file} --quiet",
            action_name=ACTION_CREATE_ROLE,
        )

        gcloud_wrapper(
            f"gcloud iam roles create {data_role} "
            f"--project={project} --file {data_file} --quiet",
            action_name=ACTION_CREATE_ROLE,
        )

    gcloud_wrapper(
        f"gcloud iam service-accounts create {main_sa}", action_name=ACTION_CREATE_SA
    )
    gcloud_wrapper(
        f"gcloud iam service-accounts create {data_sa}", action_name=ACTION_CREATE_SA
    )

    gcloud_wrapper(
        f"gcloud projects add-iam-policy-binding {project} "
        f"--member=serviceAccount:{main_email} "
        f"--role=projects/{project}/roles/{main_role}",
        action_name=ACTION_BIND_POLICY,
    )
    gcloud_wrapper(
        f"gcloud projects add-iam-policy-binding {project} "
        f"--member=serviceAccount:{data_email} "
        f"--role=projects/{project}/roles/{data_role}",
        action_name=ACTION_BIND_POLICY,
    )

    print("Service accounts and roles created.")
    print("Enabling services (this may take a while)...")

    services = [
        "compute",
        "bigquery.googleapis.com",
        "logging",
        "monitoring",
    ]

    if not skip_gar:
        services.append("artifactregistry.googleapis.com")

    for service in services:
        print(f"  {service}")
        if not gcloud_enable_service(service, project):
            setup_failure(f"Enabling service {service} failed", backend="gcp")
            return False
    print("Services enabled.")

    if not skip_gar:
        print("Setting up Google Artifact Registry (this may take a few minutes)...")
        gcloud_wrapper(
            f"gcloud artifacts repositories create {gar_name} "
            "--repository-format=docker "
            f"--location={region}",
            action_name=ACTION_CREATE_GAR,
        )
        gcloud_wrapper(
            f"gcloud artifacts repositories add-iam-policy-binding {gar_name} "
            "--role=roles/artifactregistry.repoAdmin "
            f"--location={region} "
            f"--member=serviceAccount:{main_email}",
            action_name=ACTION_BIND_GAR,
        )

    if not manual_final_setup:
        print()
        print(
            "[bold]You can setup Coiled to use the Google Cloud credentials "
            "you just created."
        )
        print(
            "The service account key will go to Coiled, where it will be stored "
            "securely and used to create clusters in your Google Cloud account "
            "on your behalf."
        )
        print(
            "This will also create infrastructure in your account like a VPC "
            "and subnets, none of which has a standing cost."
        )
        print()

    if not manual_final_setup and (
        yes
        or Confirm.ask(
            "Setup your Coiled account to use the Google Cloud "
            "credentials you just created?",
            default=True,
        )
    ):

        coiled.add_interaction(action="prompt:CoiledSetup", success=True)

        with tempfile.TemporaryDirectory() as dir:
            key_path = os.path.join(dir, "coiled-key.json")
            if not gcloud_make_key(main_email, key_path):
                return False

            if not skip_gar:
                print("Waiting for Google Artifact Registry to be ready...")
                if not gcloud_wait_for_repo(region=region, key_path=key_path):
                    # FIXME better instructions about what to do in this case
                    print(
                        "[red]Google Artifact Registry is still not ready. "
                        "You may need to complete account setup manually; "
                        "please contact us if you need help."
                    )
                    setup_failure("Timeout waiting for GAR to be ready", backend="gcp")
                    return False
                print("Google Artifact Registry is ready.")

            print("Setting up Coiled to use your Google Cloud account...")
            coiled.set_backend_options(
                backend="gcp",
                registry_type="gar" if not skip_gar else "ecr",
                gcp_region=region,
                gcp_service_creds_file=key_path,
                instance_service_account=data_email,
            )
            coiled.add_interaction(action="CoiledSetup", success=True)

    else:
        coiled.add_interaction(action="prompt:CoiledSetup", success=False)
        with coiled.Cloud() as cloud:
            coiled_account = cloud.default_account

        setup_url = (
            f"{dask.config.get('coiled.server', coiled.utils.COILED_SERVER)}/"
            f"{coiled_account}/settings/setup/update-backend-options"
        )

        data_role_console_link = (
            "https://console.cloud.google.com/iam-admin/roles/details/"
            f"projects%3C{project}%3Croles%3C{data_role}?project={project}"
        )

        key_path = os.path.abspath("coiled-key.json")
        if not gcloud_make_key(main_email, key_path):
            return False

        print(
            rich.panel.Panel(
                "You've successfully created service accounts for Coiled "
                "in your Google Cloud project. "
                "You can now complete your Coiled account setup by telling "
                "us how to use these service accounts:\n"
                "\n"
                f"1. Go to [link]{setup_url}[/link] and select GCP.\n"
                "\n"
                f"2. The credential file for [green]{main_sa}[/green] has been saved "
                f"on your local computer at \n"
                f"     {key_path}\n"
                f"   Choose this file for the "
                f"[bold]cluster-creation service account[/bold].\n"
                "\n"
                f"3. Enter [green]{data_email}[/green] as the [bold]data access "
                f"service account[/bold].\n"
                "\n"
                "You'll then have the ability to chose non-default network setup "
                "or container registry settings if desired.\n"
                "\n"
                "[bold]Optional steps[/bold]\n"
                "\n"
                "After you've successfully setup your Coiled account, you'll no "
                "longer need the credential file on your local computer and can "
                "delete this if you wish.\n"
                "\n"
                "We've configured the data access service account with scope for "
                "submitting logs and for accessing Google Storage. If you wish to "
                "add or remove permissions attached to your Coiled clusters for "
                "accessing data, you can do that at \n"
                "\n"
                f"[link]{data_role_console_link}[/link]."
            )
        )

    return True
