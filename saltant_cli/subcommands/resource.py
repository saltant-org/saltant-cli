"""Contains generic command functionality for common actions."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
import click
import click_spinner
from saltant.exceptions import BadHttpRequestError
from .utils import combine_filter_json, generate_table, generate_list_display


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
    client = ctx.obj["client"]

    # Query for the object
    try:
        manager = getattr(client, manager_name)
        object = manager.get(id)

        # Output a list display of the object
        output = generate_list_display(object, attrs)
    except BadHttpRequestError:
        # Bad request
        output = "not found"

    click.echo(output)


def generic_put_command(manager_name, attrs, ctx, id, **kwargs):
    """Performs a generic put command.

    Args:
        manager_name: A string containing the name of the
            saltant.client.Client's manager to use. For example,
            "task_queues".
        attrs: An iterable containing the attributes of the object to
            use when displaying it.
        ctx: A click.core.Context object containing information about
            the Click session.
        id: A string or int (depending on the object type) containing
            the primary identifier of the object to update.
        **kwargs: A dictionary of arbitrary keyword arguments which
            should match attributes used to update the object.
    """
    # Get the client from the context
    client = ctx.obj["client"]

    # Create the object
    manager = getattr(client, manager_name)
    object = manager.put(id, **kwargs)

    # Output a list display of the object created
    output = generate_list_display(object, attrs)

    click.echo(output)


def generic_create_command(manager_name, attrs, ctx, **kwargs):
    """Performs a generic create command.

    Args:
        manager_name: A string containing the name of the
            saltant.client.Client's manager to use. For example,
            "task_queues".
        attrs: An iterable containing the attributes of the object to
            use when displaying it.
        ctx: A click.core.Context object containing information about
            the Click session.
        **kwargs: A dictionary of arbitrary keyword arguments which
            should match attributes used to create the object.
    """
    # Get the client from the context
    client = ctx.obj["client"]

    # Create the object
    manager = getattr(client, manager_name)
    object = manager.create(**kwargs)

    # Output a list display of the object created
    output = generate_list_display(object, attrs)

    click.echo(output)


def generic_list_command(manager_name, attrs, ctx, filters, filters_file):
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
    client = ctx.obj["client"]

    # Build up JSON filters to use
    combined_filters = combine_filter_json(filters, filters_file)

    # Query for objects
    manager = getattr(client, manager_name)
    object_list = manager.list(combined_filters)

    # Output a pretty table
    output = generate_table(object_list, attrs)

    click.echo_via_pager(output)


def generic_clone_command(manager_name, attrs, ctx, uuid):
    """Performs a generic clone command for task instances.

    Args:
        manager_name: A string containing the name of the
            saltant.client.Client's manager to use. For example,
            "executable_task_instances".
        attrs: An iterable containing the attributes of the object to
            use when displaying it.
        ctx: A click.core.Context object containing information about
            the Click session.
        uuid: A string containing the uuid of the task instance to
            clone.
    """
    # Get the client from the context
    client = ctx.obj["client"]

    # Clone the task instance
    try:
        manager = getattr(client, manager_name)
        object = manager.clone(uuid)

        # Output a list display of the task instance
        output = generate_list_display(object, attrs)
    except BadHttpRequestError:
        # Bad request
        output = "task instance %s not found" % uuid

    click.echo(output)


def generic_terminate_command(manager_name, attrs, ctx, uuid):
    """Performs a generic terminate command for task instances.

    Args:
        manager_name: A string containing the name of the
            saltant.client.Client's manager to use. For example,
            "executable_task_instances".
        attrs: An iterable containing the attributes of the object to
            use when displaying it.
        ctx: A click.core.Context object containing information about
            the Click session.
        uuid: A string containing the uuid of the task instance to
            terminate.
    """
    # Get the client from the context
    client = ctx.obj["client"]

    # Terminate the task instance
    try:
        manager = getattr(client, manager_name)
        object = manager.terminate(uuid)

        # Output a list display of the task instance
        output = generate_list_display(object, attrs)
    except BadHttpRequestError:
        # Bad request
        output = "task instance %s not found" % uuid

    click.echo(output)


def generic_wait_command(manager_name, attrs, ctx, uuid, refresh_period):
    """Performs a generic wait command for task instances.

    Args:
        manager_name: A string containing the name of the
            saltant.client.Client's manager to use. For example,
            "executable_task_instances".
        attrs: An iterable containing the attributes of the object to
            use when displaying it.
        ctx: A click.core.Context object containing information about
            the Click session.
        uuid: A string containing the uuid of the task instance to
            wait for.
        refresh_period: A float specifying how many seconds to wait in
            between checking the task's status.
    """
    # Get the client from the context
    client = ctx.obj["client"]

    # Terminate the task instance
    try:
        manager = getattr(client, manager_name)

        # Wait for the task instance to finish
        with click_spinner.spinner():
            object = manager.wait_until_finished(uuid, refresh_period)

        # Output a list display of the task instance
        output = generate_list_display(object, attrs)
    except BadHttpRequestError:
        # Bad request
        output = "task instance %s not found" % uuid

    click.echo(output)
