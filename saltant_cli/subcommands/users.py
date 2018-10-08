"""Contains command group for users."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
import json
import click
from saltant.exceptions import BadHttpRequestError
from tabulate import tabulate


@click.group()
@click.pass_context
def users(ctx):
    """Command group to interface with users."""
    pass


@users.command()
@click.argument(
    'username',
    nargs=1,
    type=click.STRING,)
@click.pass_context
def get(ctx, username):
    """Get user based on username."""
    # Get the client from the context
    client = ctx.obj['client']

    # Query for the user
    try:
        user = client.users.get(username)

        # Output a pretty table
        output = tabulate(
            [[user.username, user.email]],
            headers=['username', 'email'],
        )
    except BadHttpRequestError:
        output = "%s not found" % username

    click.echo_via_pager(output)


@users.command()
@click.option(
    '--filters',
    help="Filter keys and values encoded in JSON.",
    default=None,
    type=click.STRING,)
@click.option(
    '--filters-file',
    help="Filter keys and values encoded in a JSON file.",
    default=None,
    type=click.Path(),)
@click.pass_context
def list(ctx, filters, filters_file):   # pylint: disable=redefined-builtin
    """List users matching filter parameters."""
    # Get the client from the context
    client = ctx.obj['client']

    # Build up JSON filters to use
    if filters is not None:
        filters = json.loads(filters)
    else:
        filters = {}

    if filters_file is not None:
        with open(filters_file) as f:
            filters.update(json.load(f))

    # Query for users
    user_list = client.users.list(filters)

    # Output a pretty table
    output = tabulate(
        [[user.username, user.email] for user in user_list],
        headers=['username', 'email'],
    )

    click.echo_via_pager(output)
