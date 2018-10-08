"""Contains command group for users."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
import click
from saltant.exceptions import BadHttpRequestError
from tabulate import tabulate
from .utils import (
    combine_filter_json,
    list_options,
)


@click.group()
@click.pass_context
def users(ctx):
    """Command group to interface with users."""
    pass


@users.command(name='get')
@click.argument(
    'username',
    nargs=1,
    type=click.STRING,)
@click.pass_context
def get_user(ctx, username):
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


@users.command(name='list')
@list_options
@click.pass_context
def list_users(ctx, filters, filters_file):
    """List users matching filter parameters."""
    # Get the client from the context
    client = ctx.obj['client']

    # Build up JSON filters to use
    combined_filters = combine_filter_json(filters, filters_file)

    # Query for users
    user_list = client.users.list(combined_filters)

    # Output a pretty table
    output = tabulate(
        [[user.username, user.email] for user in user_list],
        headers=['username', 'email'],
    )

    click.echo_via_pager(output)
