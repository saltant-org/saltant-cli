"""Contains command group for users."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
import click
from .resource import generic_get_command, generic_list_command
from .utils import list_options

USER_ATTRS = ("username", "email")


@click.group()
def users():
    """Command group for users."""
    pass


@users.command(name="get")
@click.argument("username", nargs=1)
@click.pass_context
def get_user(ctx, username):
    """Get user based on username."""
    generic_get_command("users", USER_ATTRS, ctx, username)


@users.command(name="list")
@list_options
@click.pass_context
def list_users(ctx, filters, filters_file):
    """List users matching filter parameters."""
    generic_list_command("users", USER_ATTRS, ctx, filters, filters_file)
