import click

from ..compatibility import COILED_VERSION
from .cluster import cluster
from .curl import curl
from .diagnostics import diagnostics
from .env import env
from .install import install
from .login import login
from .package_sync import package_sync
from .setup import setup
from .upload import upload

CONTEXT_SETTINGS = {"help_option_names": ["-h", "--help"]}


@click.group(context_settings=CONTEXT_SETTINGS)
@click.version_option(COILED_VERSION, message="%(version)s")
def cli():
    """Coiled command line tool"""
    pass


cli.add_command(login)
cli.add_command(install)
cli.add_command(upload)
cli.add_command(env)
cli.add_command(diagnostics)
cli.add_command(setup)
cli.add_command(cluster)
cli.add_command(package_sync)
cli.add_command(curl)
