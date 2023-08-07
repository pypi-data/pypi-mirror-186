import click

from ..utils import CONTEXT_SETTINGS
from .amp import aws_amp_setup
from .aws import aws_setup
from .entry import setup_wizard
from .gcp import gcp_setup


@click.group(context_settings=CONTEXT_SETTINGS)
def setup():
    """Setup Coiled with cloud provider"""
    pass


setup.add_command(setup_wizard, "wizard")
setup.add_command(aws_setup, "aws")
setup.add_command(gcp_setup, "gcp")

setup.add_command(aws_amp_setup, "amp")
