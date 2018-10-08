"""Contains command group for users."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
import click


@click.group()
@click.pass_context
def users(ctx):
    """Command group to interface with users."""
    pass


@users.command()
@click.pass_context
def list(ctx):
    """List users matching filter parameters."""
    # Get the client from the context
    client = ctx.obj['client']

    user_list = client.users.list()

    print(user_list)
