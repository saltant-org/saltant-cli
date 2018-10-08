"""Contains command group for task queues."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
import click
from saltant.exceptions import BadHttpRequestError
from .utils import (
    combine_filter_json,
    list_options,
    generate_table,
)

TASK_QUEUE_ATTRS = (
    'id',
    'user',
    'name',
    'private',
    'active',
    'description',
)


@click.group()
@click.pass_context
def task_queues(ctx):
    """Command group to interface with task queues."""
    pass


@task_queues.command(name='get')
@click.argument(
    'id',
    nargs=1,
    type=click.INT,)
@click.pass_context
def get_task_queue(ctx, id):
    """Get task queue based on ID."""
    # Get the client from the context
    client = ctx.obj['client']

    # Query for the task queue
    try:
        # Let the saltant client deal with xor logic
        task_queue = client.task_queues.get(id)

        # Output a pretty table
        output = generate_table(task_queue, TASK_QUEUE_ATTRS)
    except BadHttpRequestError:
        # Bad request
        output = "task queue not found"

    click.echo_via_pager(output)


@task_queues.command(name='list')
@list_options
@click.pass_context
def list_task_queues(ctx, filters, filters_file):
    """List task queues matching filter parameters."""
    # Get the client from the context
    client = ctx.obj['client']

    # Build up JSON filters to use
    combined_filters = combine_filter_json(filters, filters_file)

    # Query for users
    task_queue_list = client.task_queues.list(combined_filters)

    # Output a pretty table
    output = generate_table(task_queue_list, TASK_QUEUE_ATTRS)

    click.echo_via_pager(output)
