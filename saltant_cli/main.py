"""Contains the main group of commands."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
import errno
import os
import click
import click_completion
from saltant.client import Client
import yaml
from .config import parse_config_file
from .constants import CONFIG_FILE_NAME, PROJECT_CONFIG_HOME
from .exceptions import ConfigFileNotFound
from .subcommands.completion import completion
from .subcommands.task_instances import (
    container_task_instances,
    executable_task_instances,
)
from .subcommands.task_queues import task_queues
from .subcommands.task_types import container_task_types, executable_task_types
from .subcommands.task_whitelists import task_whitelists
from .subcommands.users import users
from .version import NAME, VERSION


def setup_config(ctx, param, value):
    """Set up file config and exit.

    Args:
        ctx: A click.core.Context object containing information about
            the Click session.
        param: A click.core.Option object containing information about
            the option that spawned this callback.
        value: A Boolean containing the value of the above parameter.
    """
    # Do nothing if this option wasn't specified
    if not value or ctx.resilient_parsing:
        return

    # Construct the path to the config file
    config_file_path = os.path.join(PROJECT_CONFIG_HOME, CONFIG_FILE_NAME)

    # Let the user know about the file we're writing to
    if os.path.exists(config_file_path):
        # Ask for confirmation to overwrite the file
        if not click.confirm(
            "%s already exists! Overwrite it?" % config_file_path
        ):
            # No overwritting. Get out.
            ctx.exit()

    # Get the parameters we need
    config_dict = {}

    config_dict["saltant-api-url"] = click.prompt(
        "Enter the URL of the saltant server's API"
    )
    config_dict["saltant-auth-token"] = click.prompt(
        "Enter an auth token for the saltant server"
    )

    # Make necessary subdirectories. TODO: use simpler methods if/when
    # Python 2.x support is dropped. See
    # https://stackoverflow.com/questions/600268/mkdir-p-functionality-in-python.
    try:
        os.makedirs(PROJECT_CONFIG_HOME)
    except OSError as e:
        if e.errno == errno.EEXIST and os.path.isdir(PROJECT_CONFIG_HOME):
            pass
        else:
            raise

    # Write to the file
    with open(config_file_path, "w") as config_file:
        yaml.dump(config_dict, config_file, default_flow_style=False)

    click.echo("Config settings saved to %s" % config_file_path)

    # Exit
    ctx.exit()


@click.group(help="saltant CLI")
@click.option(
    "-c",
    "--config-path",
    help="Explicit path to config file.",
    default=None,
    type=click.Path(),
)
@click.option(
    "--setup",
    help="Set up config file and exit.",
    is_flag=True,
    callback=setup_config,
    expose_value=False,
    is_eager=True,
)
@click.version_option(version=VERSION, prog_name=NAME)
@click.pass_context
def main(ctx, config_path):
    """Main entry point for saltant CLI.

    Args:
        ctx: A click.core.Context object containing information about
            the Click session.
        config_path: A string (or None) containing an explicit path to a
            config file.
    """
    # Load in the config file
    try:
        config_dict = parse_config_file(config_path)
    except ConfigFileNotFound:
        # Error! Get out!
        click.echo("No config file found. Please run program with --setup.")
        ctx.exit()

    # Create a saltant session
    ctx.ensure_object(dict)
    ctx.obj["client"] = Client(
        base_api_url=config_dict["saltant-api-url"],
        auth_token=config_dict["saltant-auth-token"],
        test_if_authenticated=False,
    )


# Add in subcommands
main.add_command(completion)
main.add_command(container_task_instances)
main.add_command(container_task_types)
main.add_command(executable_task_instances)
main.add_command(executable_task_types)
main.add_command(task_queues)
main.add_command(task_whitelists)
main.add_command(users)

# Enable click_completion monkey patch
click_completion.init()
