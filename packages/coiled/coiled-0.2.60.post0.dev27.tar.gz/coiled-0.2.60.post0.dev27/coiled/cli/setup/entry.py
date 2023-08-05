import traceback

import click
from rich import print
from rich.prompt import Prompt

import coiled

from ..utils import CONTEXT_SETTINGS
from .util import setup_failure


@click.command(context_settings=CONTEXT_SETTINGS)
def setup_wizard() -> bool:
    return do_setup_wizard()


def do_setup_wizard() -> bool:
    coiled.add_interaction(
        action="cli-setup-wizard:start",
        success=True,
    )

    print(
        "Coiled creates and manages Dask clusters in your own cloud provider account.\n\n"
        "  1. AWS\n"
        "  2. Google Cloud\n"
        "  3. Azure\n"
        "  4. I don't have an AWS, GCP, or Azure account, help me choose!\n"
        "  [red]x[/red]. Exit the setup wizard\n"
    )

    try:
        choice = Prompt.ask(
            "Please choose your cloud provider so we can guide you in setting up Coiled",
            choices=["1", "2", "3", "4", "x"],
            show_choices=False,
        )
    except KeyboardInterrupt:
        coiled.add_interaction(
            action="cli-setup-wizard:KeyboardInterrupt", success=False
        )
        return False

    coiled.add_interaction(
        action="cli-setup-wizard:prompt", success=True, choice=choice
    )

    if choice == "1":  # AWS
        print("\nRunning [green]coiled setup aws[/green]\n")
        from .aws import do_setup

        try:
            return do_setup(slug="coiled")
        except Exception:
            setup_failure(f"Exception raised {traceback.format_exc()}", backend="aws")
            raise
    elif choice == "2":  # GCP
        print("\nRunning [green]coiled setup gcp[/green]\n")
        from .gcp import do_setup

        try:
            return do_setup()
        except Exception:
            setup_failure(f"Exception raised {traceback.format_exc()}", backend="gcp")
            raise
    elif choice == "3":  # Azure
        print(
            "\nWe don't currently offer managed infrastructure for Dask on Azure. If you're running Dask on Azure, "
            "Coiled can provide you with a platform for advanced analytics of our Dask usage. "
            "Please see our documentation about deploying Dask on Azure:\n"
            "[link]https://docs.coiled.io/user_guide/azure_reference.html[/link]"
        )
    elif choice == "4":  # Other
        print(
            "\nCoiled currently supports AWS and Google Cloud. It's easy to make an account with either and get "
            "started using Coiled. Please see our documentation about choosing a cloud provider:\n"
            "[link]https://docs.coiled.io/user_guide/backends.html#need-a-cloud-provider-account[/link]"
        )

    return False
