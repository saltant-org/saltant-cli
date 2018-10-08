"""Contains command groups for task instances.

Currently this supports container and executable task instances.
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

# Have a hierarchy of these later if attributes for different types of
# task instances start to diverge. For now all task instances have the
# same attributes regardless of their type.
TASK_INSTANCE_GET_ATTRS = (
    'uuid',
    'name',
    'state',
    'user',
    'task_queue',
    'task_type',
    'datetime_created',
    'datetime_finished',
    'arguments',
)
TASK_INSTANCE_LIST_ATTRS = (
    'uuid',
    'state',
    'user',
    'task_queue',
    'task_type',
    'datetime_created',
    'datetime_finished',
    'name',
)


@click.group()
def container_task_instances():
    """Command group to interface with container task instances."""
    pass


@container_task_instances.command(name='get')
@click.argument(
    'uuid',
    nargs=1,
    type=click.UUID,)
@click.pass_context
def get_container_task_instance(ctx, uuid):
    """Get container task instance based on UUID."""
    generic_get_command(
        'container_task_instances',
        TASK_INSTANCE_GET_ATTRS,
        ctx,
        str(uuid),
    )


@container_task_instances.command(name='list')
@list_options
@click.pass_context
def list_container_task_instances(ctx, filters, filters_file):
    """List container task instances matching filter parameters."""
    generic_list_command(
        'container_task_instances',
        TASK_INSTANCE_LIST_ATTRS,
        ctx,
        filters,
        filters_file,
    )


@click.group()
def executable_task_instances():
    """Command group to interface with executable task instances."""
    pass


@executable_task_instances.command(name='get')
@click.argument(
    'uuid',
    nargs=1,
    type=click.UUID,)
@click.pass_context
def get_executable_task_instance(ctx, uuid):
    """Get executable task instance based on UUID."""
    generic_get_command(
        'executable_task_instances',
        TASK_INSTANCE_GET_ATTRS,
        ctx,
        str(uuid),
    )


@executable_task_instances.command(name='list')
@list_options
@click.pass_context
def list_executable_task_instances(ctx, filters, filters_file):
    """List executable task instances matching filter parameters."""
    generic_list_command(
        'executable_task_instances',
        TASK_INSTANCE_LIST_ATTRS,
        ctx,
        filters,
        filters_file,
    )
