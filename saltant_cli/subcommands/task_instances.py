"""Contains command groups for task instances.

Currently this supports container and executable task instances.
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
import json
import click
from .resource import (
    generic_clone_command,
    generic_create_command,
    generic_get_command,
    generic_list_command,
    generic_terminate_command,
    generic_wait_command,
)
from .utils import list_options

# Have a hierarchy of these later if attributes for different types of
# task instances start to diverge. For now all task instances have the
# same attributes regardless of their type.
TASK_INSTANCE_GET_ATTRS = (
    "uuid",
    "name",
    "state",
    "user",
    "task_queue",
    "task_type",
    "datetime_created",
    "datetime_finished",
    "arguments",
)
TASK_INSTANCE_LIST_ATTRS = (
    "uuid",
    "state",
    "user",
    "task_queue",
    "task_type",
    "datetime_created",
    "datetime_finished",
    "name",
)


@click.group()
def container_task_instances():
    """Command group for container task instances."""
    pass


@container_task_instances.command(name="get")
@click.argument("uuid", nargs=1, type=click.UUID)
@click.pass_context
def get_container_task_instance(ctx, uuid):
    """Get a container task instance based on UUID."""
    generic_get_command(
        "container_task_instances", TASK_INSTANCE_GET_ATTRS, ctx, str(uuid)
    )


@container_task_instances.command(name="list")
@list_options
@click.pass_context
def list_container_task_instances(ctx, filters, filters_file):
    """List container task instances matching filter parameters."""
    generic_list_command(
        "container_task_instances",
        TASK_INSTANCE_LIST_ATTRS,
        ctx,
        filters,
        filters_file,
    )


@container_task_instances.command(name="create")
@click.option("--name", help="A name for the task instance.", default="")
@click.option(
    "--task-type",
    help="The ID of the task type.",
    required=True,
    type=click.INT,
)
@click.option(
    "--task-queue",
    help="The ID of the task queue.",
    required=True,
    type=click.INT,
)
@click.option(
    "--json-arguments",
    help="Arguments to give the instance in a JSON string.",
    default="{}",
    show_default=True,
)
@click.pass_context
def create_container_task_instance(ctx, **kwargs):
    """Create a container task instance."""
    # Parse the JSON arguments
    kwargs["arguments"] = json.loads(kwargs.pop("json_arguments"))

    # Rename arguments as necessary
    kwargs["task_queue_id"] = kwargs.pop("task_queue")
    kwargs["task_type_id"] = kwargs.pop("task_type")

    # Run the generic create command
    generic_create_command(
        "container_task_instances", TASK_INSTANCE_GET_ATTRS, ctx, **kwargs
    )


@container_task_instances.command(name="clone")
@click.argument("uuid", nargs=1, type=click.UUID)
@click.pass_context
def clone_container_task_instance(ctx, uuid):
    """Clone a container task instance with given UUID."""
    generic_clone_command(
        "container_task_instances", TASK_INSTANCE_GET_ATTRS, ctx, str(uuid)
    )


@container_task_instances.command(name="terminate")
@click.argument("uuid", nargs=1, type=click.UUID)
@click.pass_context
def terminate_container_task_instance(ctx, uuid):
    """Terminate a container task instance with given UUID."""
    generic_terminate_command(
        "container_task_instances", TASK_INSTANCE_GET_ATTRS, ctx, str(uuid)
    )


@container_task_instances.command(name="wait")
@click.option(
    "--refresh-period",
    help="Number of seconds to wait in between status checks.",
    default=5,
    type=click.FLOAT,
)
@click.argument("uuid", nargs=1, type=click.UUID)
@click.pass_context
def wait_for_container_task_instance(ctx, uuid, refresh_period):
    """Wait for an container task instance with given UUID to finish."""
    generic_wait_command(
        "container_task_instances",
        TASK_INSTANCE_GET_ATTRS,
        ctx,
        str(uuid),
        refresh_period,
    )


@click.group()
def executable_task_instances():
    """Command group for executable task instances."""
    pass


@executable_task_instances.command(name="get")
@click.argument("uuid", nargs=1, type=click.UUID)
@click.pass_context
def get_executable_task_instance(ctx, uuid):
    """Get an executable task instance based on UUID."""
    generic_get_command(
        "executable_task_instances", TASK_INSTANCE_GET_ATTRS, ctx, str(uuid)
    )


@executable_task_instances.command(name="list")
@list_options
@click.pass_context
def list_executable_task_instances(ctx, filters, filters_file):
    """List executable task instances matching filter parameters."""
    generic_list_command(
        "executable_task_instances",
        TASK_INSTANCE_LIST_ATTRS,
        ctx,
        filters,
        filters_file,
    )


@executable_task_instances.command(name="create")
@click.option("--name", help="A name for the task instance.", default="")
@click.option(
    "--task-type",
    help="The ID of the task type.",
    required=True,
    type=click.INT,
)
@click.option(
    "--task-queue",
    help="The ID of the task queue.",
    required=True,
    type=click.INT,
)
@click.option(
    "--json-arguments",
    help="Arguments to give the instance in a JSON string.",
    default="{}",
    show_default=True,
)
@click.pass_context
def create_executable_task_instance(ctx, **kwargs):
    """Create a executable task instance."""
    # Parse the JSON arguments
    kwargs["arguments"] = json.loads(kwargs.pop("json_arguments"))

    # Rename arguments as necessary
    kwargs["task_queue_id"] = kwargs.pop("task_queue")
    kwargs["task_type_id"] = kwargs.pop("task_type")

    # Run the generic create command
    generic_create_command(
        "executable_task_instances", TASK_INSTANCE_GET_ATTRS, ctx, **kwargs
    )


@executable_task_instances.command(name="clone")
@click.argument("uuid", nargs=1, type=click.UUID)
@click.pass_context
def clone_executable_task_instance(ctx, uuid):
    """Clone an executable task instance with given UUID."""
    generic_clone_command(
        "executable_task_instances", TASK_INSTANCE_GET_ATTRS, ctx, str(uuid)
    )


@executable_task_instances.command(name="terminate")
@click.argument("uuid", nargs=1, type=click.UUID)
@click.pass_context
def terminate_executable_task_instance(ctx, uuid):
    """Terminate an executable task instance with given UUID."""
    generic_terminate_command(
        "executable_task_instances", TASK_INSTANCE_GET_ATTRS, ctx, str(uuid)
    )


@executable_task_instances.command(name="wait")
@click.option(
    "--refresh-period",
    help="Number of seconds to wait in between status checks.",
    default=5,
    type=click.FLOAT,
)
@click.argument("uuid", nargs=1, type=click.UUID)
@click.pass_context
def wait_for_executable_task_instance(ctx, uuid, refresh_period):
    """Wait for an executable task instance with given UUID to finish."""
    generic_wait_command(
        "executable_task_instances",
        TASK_INSTANCE_GET_ATTRS,
        ctx,
        str(uuid),
        refresh_period,
    )
