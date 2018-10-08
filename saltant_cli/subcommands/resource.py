"""Contains generic command functionality for common actions."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
import click
from saltant.exceptions import BadHttpRequestError
from .utils import (
    combine_filter_json,
    generate_table,
)


def generic_list_command(manager_name, attrs, ctx, filters, filters_file):
    """Performs a generic list command."""
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


def generic_get_command(manager_name, attrs, ctx, id):
    """Performs a generic get command."""
    # Get the client from the context
    client = ctx.obj['client']

    # Query for the object
    try:
        manager = getattr(client, manager_name)
        object = manager.get(id)

        # Output a pretty table
        output = generate_table(object, attrs)
    except BadHttpRequestError:
        # Bad request
        output = "not found"

    click.echo_via_pager(output)
