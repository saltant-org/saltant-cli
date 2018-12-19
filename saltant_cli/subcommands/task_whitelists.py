"""Contains command group for task whitelists."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
import click
from .resource import (
    generic_create_command,
    generic_get_command,
    generic_list_command,
    generic_put_command,
)
from .utils import list_options, PythonLiteralOption

TASK_WHITELIST_GET_ATTRS = (
    "id",
    "user",
    "name",
    "description",
    "whitelisted_container_task_types",
    "whitelisted_executable_task_types",
)
TASK_WHITELIST_LIST_ATTRS = ("id", "user", "name", "description")


@click.group()
def task_whitelists():
    """Command group for task whitelists."""
    pass


@task_whitelists.command(name="get")
@click.argument("id", nargs=1, type=click.INT)
@click.pass_context
def get_task_whitelist(ctx, id):
    """Get task whitelist based on ID."""
    generic_get_command("task_whitelists", TASK_WHITELIST_GET_ATTRS, ctx, id)


@task_whitelists.command(name="list")
@list_options
@click.pass_context
def list_task_whitelists(ctx, filters, filters_file):
    """List task whitelists matching filter parameters."""
    generic_list_command(
        "task_whitelists",
        TASK_WHITELIST_LIST_ATTRS,
        ctx,
        filters,
        filters_file,
    )


@task_whitelists.command(name="create")
@click.option("--name", help="The name of the task whitelist.", required=True)
@click.option(
    "--description", help="A description of the task whitelist.", default=""
)
@click.option(
    "--whitelisted-container-task-types",
    help="IDs of the whitelists container task types.",
    cls=PythonLiteralOption,
    default=[],
    show_default=True,
)
@click.option(
    "--whitelisted-executable-task-types",
    help="IDs of the whitelists executable task types.",
    cls=PythonLiteralOption,
    default=[],
    show_default=True,
)
@click.pass_context
def create_task_whitelist(ctx, **kwargs):
    """Create a task whitelist."""
    generic_create_command(
        "task_whitelists", TASK_WHITELIST_GET_ATTRS, ctx, **kwargs
    )


@task_whitelists.command(name="put")
@click.argument("id", nargs=1, type=click.INT)
@click.option("--name", required=True, help="The name of the task whitelist.")
@click.option(
    "--description", required=True, help="A description of the task whitelist."
)
@click.option(
    "--whitelisted-container-task-types",
    help="IDs of the whitelists container task types.",
    cls=PythonLiteralOption,
    required=True,
    show_default=True,
)
@click.option(
    "--whitelisted-executable-task-types",
    help="IDs of the whitelists executable task types.",
    cls=PythonLiteralOption,
    required=True,
    show_default=True,
)
@click.pass_context
def put_task_whitelist(ctx, id, **kwargs):
    """Update a task whitelist, overwritting all its attributes."""
    generic_put_command(
        "task_whitelists", TASK_WHITELIST_GET_ATTRS, ctx, id, **kwargs
    )
