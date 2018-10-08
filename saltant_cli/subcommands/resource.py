"""Contains generic command functionality for common actions."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
import click
from saltant.exceptions import BadHttpRequestError
from .utils import (
    combine_filter_json,
    generate_table,
    generate_list_display,
)


def generic_get_command(manager_name, attrs, ctx, id):
    """Performs a generic get command.

    Args:
        manager_name: A string containing the name of the
            saltant.client.Client's manager to use. For example,
            "task_queues".
        attrs: An iterable containing the attributes of the object to
            use when displaying it.
        ctx: A click.core.Context object containing information about
            the Click session.
        id: A string or int (depending on the object type) containing
            the primary identifier of the object to get.
    """
    # Get the client from the context
    client = ctx.obj['client']

    # Query for the object
    try:
        manager = getattr(client, manager_name)
        object = manager.get(id)

        # Output a pretty table
        output = generate_list_display(object, attrs)
    except BadHttpRequestError:
        # Bad request
        output = "not found"

    click.echo(output)


def generic_list_command(
        manager_name,
        attrs,
        ctx,
        filters,
        filters_file):
    """Performs a generic list command.

    Args:
        manager_name: A string containing the name of the
            saltant.client.Client's manager to use. For example,
            "task_queues".
        attrs: An iterable containing the attributes of the object to
            use when displaying the list.
        ctx: A click.core.Context object containing information about
            the Click session.
        filters: A JSON-encoded string containing filter information.
        filters_file: A string containing a path to a JSON-encoded file
            specifying filter information.
    """
    # Get the client from the context
    client = ctx.obj['client']

    # Build up JSON filters to use
    combined_filters = combine_filter_json(filters, filters_file)

    # Query for objects
    manager = getattr(client, manager_name)
    object_list = manager.list(combined_filters)

    # Output a pretty table
    output = generate_table(object_list, attrs)

    click.echo_via_pager(output)
