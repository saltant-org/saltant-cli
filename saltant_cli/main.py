"""Contains the main function."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
import click
from .version import NAME, VERSION


def print_version(ctx, param, value):
    """Show the version and exit."""
    if not value or ctx.resilient_parsing:
        return

    click.echo("%s version %s" % (NAME, VERSION))
    ctx.exit()


@click.group()
@click.option(
    '--version',
    help="Show the version and exit.",
    is_flag=True,
    callback=print_version,
    expose_value=False,
    is_eager=True,)
def main():
    """saltant CLI"""
    click.echo("Running this")


@main.command()
def subcommand():
    click.echo("Running this, too")
