"""Contains the main function."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
import click
from .config import parse_config_file
from .exceptions import ConfigFileNotFound
from .version import NAME, VERSION


def print_version(ctx, param, value):
    """Show the version and exit."""
    # Not sure exactly what this is for, but it was in the Click docs
    # examples so I guess it's best practice??
    if not value or ctx.resilient_parsing:
        return

    # Print version and exit
    click.echo("%s version %s" % (NAME, VERSION))
    ctx.exit()


@click.group()
@click.option(
    '--config-path',
    help="Explicit path to config file.",
    default=None,
    type=click.Path(),)
@click.option(
    '--version',
    help="Show the version and exit.",
    is_flag=True,
    callback=print_version,
    expose_value=False,
    is_eager=True,)
@click.pass_context
def main(ctx, config_path):
    """saltant CLI"""
    # Load in the config file
    try:
        config_dict = parse_config_file(config_path)
    except ConfigFileNotFound:
        # Error! Get out!
        click.echo("USEFUL ERROR MESSAGE HERE")
        ctx.exit()

    # Create a saltant session
    # ctx.ensure_object(dict)


@main.command()
@click.pass_context
def subcommand(ctx):
    # Put subcommands in their own modules later
    click.echo("THIS IS A SUBCOMMAND")
