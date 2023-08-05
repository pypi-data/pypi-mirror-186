import os
import shutil
import subprocess
import tempfile
from typing import Optional

import click
from rich import print

import coiled

from ..utils import CONTEXT_SETTINGS


def open_ssh(address: str, key: str, jump_to_address: Optional[str] = None):
    """Open an SSH session, relies on `ssh` and `ssh-add` (agent)."""

    if not shutil.which("ssh"):
        print(
            "Unable to find `ssh`, you may need to install OpenSSH or add it to your paths."
        )
        return

    if not shutil.which("ssh-add"):
        print(
            "Unable to find `ssh-add`, you may need to install OpenSSH or add it to your paths."
        )
        return

    with tempfile.TemporaryDirectory() as keydir:
        key_path = os.path.join(keydir, f"scheduler-key-{address}.pem")

        with open(key_path, "w") as f:
            f.write(key)

        # ssh needs file permissions to be set
        os.chmod(key_path, mode=0o600)

        # briefly add key to agent, this allows us to jump to worker with agent forwarding
        p = subprocess.run(["ssh-add", "-t", "5", key_path], capture_output=True)

        if p.returncode and p.stderr:
            print(
                "An error occurred calling `ssh-add`. You may need to enable the ssh agent."
            )
            print(p.stderr)
            return

    if jump_to_address:
        ssh_target = f"-J ubuntu@{address} ubuntu@{jump_to_address}"
        ssh_target_label = f"worker at {jump_to_address}"
    else:
        ssh_target = f"ubuntu@{address}"
        ssh_target_label = f"scheduler at {address}"

    ssh_command = f"ssh {ssh_target} -o StrictHostKeyChecking=no -o ForwardAgent=yes"

    # print(ssh_command)
    print(f"===Starting SSH session to {ssh_target_label}===")
    subprocess.run(ssh_command, shell=True)
    print("===SSH session closed===")


@click.command(context_settings=CONTEXT_SETTINGS)
@click.argument("cluster")
@click.option(
    "--private",
    default=False,
    is_flag=True,
    help="Use private IP address of scheduler (default is public IP address)",
)
@click.option(
    "--worker",
    default=None,
    help="Connect to worker with specified name or private IP address (default is to connect to scheduler)",
)
def ssh(cluster: str, private: bool, worker: Optional[str]):
    with coiled.Cloud() as cloud:

        if cluster.isnumeric():
            cluster_id = int(cluster)
        else:
            try:
                cluster_id = cloud.get_cluster_by_name(name=cluster)
            except coiled.errors.DoesNotExist:
                cluster_id = None

        if not cluster_id:
            print(f"Unable to find cluster `{cluster}`")
            return

        ssh_info = cloud.get_ssh_key(cluster_id=cluster_id, worker=worker)

        # print(ssh_info)

        if ssh_info["scheduler_state"] != "started":
            print(
                f"Scheduler state is {ssh_info['scheduler_state']}. "
                "You can only connect when scheduler is 'started'."
            )
            return

        scheduler_address = (
            ssh_info["scheduler_private_address"]
            if private
            else ssh_info["scheduler_public_address"]
        )

        if not scheduler_address:
            print("Unable to retrieve scheduler address")
            return

        if not ssh_info["private_key"]:
            print("Unable to retrieve SSH key")
            return

        open_ssh(
            address=scheduler_address,
            key=ssh_info["private_key"],
            jump_to_address=ssh_info["worker_address"],
        )
