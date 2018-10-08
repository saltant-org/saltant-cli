"""Contains command groups for task types.

Currently this supports container and executable task types.
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
import click
from .resource import (
    generic_get_command,
    generic_list_command,
)
from .utils import(
    list_options,
)

BASE_TASK_TYPE_GET_ATTRS = (
    'id',
    'user',
    'name',
    'description',
    'datetime_created',
    'command_to_run',
    'environment_variables',
    'required_arguments',
    'required_arguments_default_values',
)
CONTAINER_TASK_TYPE_GET_ATTRS = (
    BASE_TASK_TYPE_GET_ATTRS
    + ('logs_path',
       'results_path',
       'container_image',
       'container_type',)
)
EXECUTABLE_TASK_TYPE_GET_ATTRS = BASE_TASK_TYPE_GET_ATTRS

BASE_TASK_TYPE_LIST_ATTRS = (
    'id',
    'name',
    'user',
    'description',
)
CONTAINER_TASK_TYPE_LIST_ATTRS = (
    BASE_TASK_TYPE_LIST_ATTRS
    + ('container_image', 'container_type')
)
EXECUTABLE_TASK_TYPE_LIST_ATTRS = BASE_TASK_TYPE_LIST_ATTRS


@click.group()
def container_task_types():
    """Command group to interface with container task types."""
    pass


@container_task_types.command(name='get')
@click.argument(
    'id',
    nargs=1,
    type=click.INT,)
@click.pass_context
def get_container_task_type(ctx, id):
    """Get container task type with given ID."""
    generic_get_command(
        'container_task_types',
        CONTAINER_TASK_TYPE_GET_ATTRS,
        ctx,
        id,
    )


@container_task_types.command(name='list')
@list_options
@click.pass_context
def list_container_task_types(ctx, filters, filters_file):
    """List container typesinstances matching filter parameters."""
    generic_list_command(
        'container_task_types',
        CONTAINER_TASK_TYPE_LIST_ATTRS,
        ctx,
        filters,
        filters_file,
    )


@click.group()
def executable_task_types():
    """Command group to interface with executable task types."""
    pass


@executable_task_types.command(name='get')
@click.argument(
    'id',
    nargs=1,
    type=click.INT,)
@click.pass_context
def get_executable_task_type(ctx, id):
    """Get executable task type with given ID."""
    generic_get_command(
        'executable_task_types',
        EXECUTABLE_TASK_TYPE_GET_ATTRS,
        ctx,
        id,
    )


@executable_task_types.command(name='list')
@list_options
@click.pass_context
def list_executable_task_types(ctx, filters, filters_file):
    """List executable typesinstances matching filter parameters."""
    generic_list_command(
        'executable_task_types',
        EXECUTABLE_TASK_TYPE_LIST_ATTRS,
        ctx,
        filters,
        filters_file,
    )
