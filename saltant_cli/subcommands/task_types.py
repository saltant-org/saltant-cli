"""Contains command groups for task types.

Currently this supports container and executable task types.
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
import json
import click
from .resource import (
    generic_create_command,
    generic_get_command,
    generic_list_command,
    generic_put_command,
)
from .utils import list_options

BASE_TASK_TYPE_GET_ATTRS = (
    "id",
    "user",
    "name",
    "description",
    "datetime_created",
    "command_to_run",
    "environment_variables",
    "required_arguments",
    "required_arguments_default_values",
)
CONTAINER_TASK_TYPE_GET_ATTRS = BASE_TASK_TYPE_GET_ATTRS + (
    "logs_path",
    "results_path",
    "container_image",
    "container_type",
)
EXECUTABLE_TASK_TYPE_GET_ATTRS = BASE_TASK_TYPE_GET_ATTRS + (
    "json_file_option",
)

BASE_TASK_TYPE_LIST_ATTRS = ("id", "name", "user", "description")
CONTAINER_TASK_TYPE_LIST_ATTRS = BASE_TASK_TYPE_LIST_ATTRS + (
    "container_image",
    "container_type",
)
EXECUTABLE_TASK_TYPE_LIST_ATTRS = BASE_TASK_TYPE_LIST_ATTRS


@click.group()
def container_task_types():
    """Command group for container task types."""
    pass


@container_task_types.command(name="get")
@click.argument("id", nargs=1, type=click.INT)
@click.pass_context
def get_container_task_type(ctx, id):
    """Get container task type with given ID."""
    generic_get_command(
        "container_task_types", CONTAINER_TASK_TYPE_GET_ATTRS, ctx, id
    )


@container_task_types.command(name="list")
@list_options
@click.pass_context
def list_container_task_types(ctx, filters, filters_file):
    """List container task types matching filter parameters."""
    generic_list_command(
        "container_task_types",
        CONTAINER_TASK_TYPE_LIST_ATTRS,
        ctx,
        filters,
        filters_file,
    )


@container_task_types.command(name="create")
@click.option("--name", help="The name of the task.", required=True)
@click.option(
    "--command-to-run",
    help="The command to run to execute the task.",
    required=True,
)
@click.option(
    "--container-image", help="The container name and tag.", required=True
)
@click.option(
    "--container-type",
    help="The type of the container.",
    required=True,
    type=click.Choice(["docker", "singularity"]),
)
@click.option(
    "--logs-path",
    help="The path of the logs directory inside the container.",
    default="",
)
@click.option(
    "--results-path",
    help="The path of the results directory inside the container.",
    default="",
)
@click.option(
    "--json-environment-variables",
    help="The environment variables required on the host to execute the task, encoded in a JSON string.",
    default="[]",
    show_default=True,
)
@click.option(
    "--json-required-arguments",
    help="The argument names for the task type, encoded in a JSON string.",
    default="[]",
    show_default=True,
)
@click.option(
    "--json-required-arguments-default-values",
    help="Default values for the tasks required arguments, encoded in a JSON string.",
    default="{}",
    show_default=True,
)
@click.pass_context
def create_container_task_type(ctx, **kwargs):
    """Create a container task type."""
    # Parse the JSON-encoded arguments
    kwargs["environment_variables"] = json.loads(
        kwargs.pop("json_environment_variables")
    )
    kwargs["required_arguments"] = json.loads(
        kwargs.pop("json_required_arguments")
    )
    kwargs["required_arguments_default_values"] = json.loads(
        kwargs.pop("json_required_arguments_default_values")
    )

    # Run the generic create command
    generic_create_command(
        "container_task_types", CONTAINER_TASK_TYPE_GET_ATTRS, ctx, **kwargs
    )


@container_task_types.command(name="put")
@click.argument("id", nargs=1, type=click.INT)
@click.option("--name", required=True, help="The name of the task.")
@click.option(
    "--command-to-run",
    required=True,
    help="The command to run to execute the task.",
)
@click.option(
    "--container-image", required=True, help="The container name and tag."
)
@click.option(
    "--container-type",
    required=True,
    type=click.Choice(["docker", "singularity"]),
    help="The type of the container.",
)
@click.option(
    "--logs-path",
    required=True,
    help="The path of the logs directory inside the container.",
)
@click.option(
    "--results-path",
    required=True,
    help="The path of the results directory inside the container.",
)
@click.option(
    "--json-environment-variables",
    required=True,
    help="The environment variables required on the host to execute the task, encoded in a JSON string.",
)
@click.option(
    "--json-required-arguments",
    required=True,
    help="The argument names for the task type, encoded in a JSON string.",
)
@click.option(
    "--json-required-arguments-default-values",
    required=True,
    help="Default values for the tasks required arguments, encoded in a JSON string.",
)
@click.pass_context
def put_container_task_type(ctx, id, **kwargs):
    """Update a container task type, overwritting all its attributes."""
    # Parse the JSON-encoded arguments
    kwargs["environment_variables"] = json.loads(
        kwargs.pop("json_environment_variables")
    )
    kwargs["required_arguments"] = json.loads(
        kwargs.pop("json_required_arguments")
    )
    kwargs["required_arguments_default_values"] = json.loads(
        kwargs.pop("json_required_arguments_default_values")
    )

    # Run the generic create command
    generic_put_command(
        "container_task_types",
        CONTAINER_TASK_TYPE_GET_ATTRS,
        ctx,
        id,
        **kwargs
    )


@click.group()
def executable_task_types():
    """Command group for executable task types."""
    pass


@executable_task_types.command(name="get")
@click.argument("id", nargs=1, type=click.INT)
@click.pass_context
def get_executable_task_type(ctx, id):
    """Get executable task type with given ID."""
    generic_get_command(
        "executable_task_types", EXECUTABLE_TASK_TYPE_GET_ATTRS, ctx, id
    )


@executable_task_types.command(name="list")
@list_options
@click.pass_context
def list_executable_task_types(ctx, filters, filters_file):
    """List executable types types matching filter parameters."""
    generic_list_command(
        "executable_task_types",
        EXECUTABLE_TASK_TYPE_LIST_ATTRS,
        ctx,
        filters,
        filters_file,
    )


@executable_task_types.command(name="create")
@click.option("--name", help="The name of the task.", required=True)
@click.option(
    "--command-to-run",
    help="The command to run to execute the task.",
    required=True,
)
@click.option(
    "--json-environment-variables",
    help="The environment variables required on the host to execute the task, encoded in a JSON string.",
    default="[]",
    show_default=True,
)
@click.option(
    "--json-required-arguments",
    help="The argument names for the task type, encoded in a JSON string.",
    default="[]",
    show_default=True,
)
@click.option(
    "--json-required-arguments-default-values",
    help="Default values for the tasks required arguments, encoded in a JSON string.",
    default="{}",
    show_default=True,
)
@click.option(
    "--json-file-option",
    help="The option which accepts a JSON-encoded file for the command to run.",
    default=None,
)
@click.pass_context
def create_executable_task_type(ctx, **kwargs):
    """Create an executable task type."""
    # Parse the JSON-encoded arguments
    kwargs["environment_variables"] = json.loads(
        kwargs.pop("json_environment_variables")
    )
    kwargs["required_arguments"] = json.loads(
        kwargs.pop("json_required_arguments")
    )
    kwargs["required_arguments_default_values"] = json.loads(
        kwargs.pop("json_required_arguments_default_values")
    )

    # Run the generic create command
    generic_create_command(
        "executable_task_types", EXECUTABLE_TASK_TYPE_GET_ATTRS, ctx, **kwargs
    )


@executable_task_types.command(name="put")
@click.argument("id", nargs=1, type=click.INT)
@click.option("--name", required=True, help="The name of the task.")
@click.option(
    "--command-to-run",
    required=True,
    help="The command to run to execute the task.",
)
@click.option(
    "--json-environment-variables",
    required=True,
    help="The environment variables required on the host to execute the task, encoded in a JSON string.",
)
@click.option(
    "--json-required-arguments",
    required=True,
    help="The argument names for the task type, encoded in a JSON string.",
)
@click.option(
    "--json-required-arguments-default-values",
    required=True,
    help="Default values for the tasks required arguments, encoded in a JSON string.",
)
@click.option(
    "--json-file-option",
    required=True,
    help="The option which accepts a JSON-encoded file for the command to run.",
)
@click.pass_context
def put_executable_task_type(ctx, id, **kwargs):
    """Update an executable task type, overwritting all its attributes."""
    # Parse the JSON-encoded arguments
    kwargs["environment_variables"] = json.loads(
        kwargs.pop("json_environment_variables")
    )
    kwargs["required_arguments"] = json.loads(
        kwargs.pop("json_required_arguments")
    )
    kwargs["required_arguments_default_values"] = json.loads(
        kwargs.pop("json_required_arguments_default_values")
    )

    # Run the generic create command
    generic_put_command(
        "executable_task_types",
        EXECUTABLE_TASK_TYPE_GET_ATTRS,
        ctx,
        id,
        **kwargs
    )
