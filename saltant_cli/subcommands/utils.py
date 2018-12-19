"""Contains utility functions to reduce repetitive code."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
import ast
import json
import click
from tabulate import tabulate


class PythonLiteralOption(click.Option):
    """Thanks to Stephen Rauch on stack overflow.

    See https://stackoverflow.com/a/47730333
    """

    def type_cast_value(self, ctx, value):
        try:
            return ast.literal_eval(value)
        except:
            raise click.BadParameter(value)


def list_options(func):
    """Adds in --filters and --filters-file options for a command.

    Args:
        func: The function to be enclosed.

    Returns:
        The enclosed function.
    """
    filters_option = click.option(
        "--filters",
        help="Filter keys and values encoded in JSON.",
        default=None,
    )
    filters_file_option = click.option(
        "--filters-file",
        help="Filter keys and values encoded in a JSON file.",
        default=None,
        type=click.Path(),
    )

    return filters_option(filters_file_option(func))


def combine_filter_json(filters, filters_file):
    """Combines filter JSON sources for a list command.

    Args:
        filters: A JSON-encoded string containing filter information.
        filters_file: A string containing a path to a JSON-encoded file
            specifying filter information.

    Returns:
        A dictionary to be encoded into JSON containing the filters
        combined from the above sources.
    """
    combined_filters = {}

    if filters is not None:
        combined_filters.update(json.loads(filters))

    if filters_file is not None:
        with open(filters_file) as f:
            combined_filters.update(json.load(f))

    return combined_filters


def generate_table(objects, attrs):
    """Generate a table for object(s) based on some attributes.

    Args:
        objects: An iterable of objects which have specific attributes.
        attrs: An interable object of strings containing attributes to
            get from the above objects.

    Returns:
        A string containing the tabulated objects with respect to the
        passed in attributes.
    """
    return tabulate(
        [[getattr(object, attr) for attr in attrs] for object in objects],
        headers=attrs,
    )


def generate_list_display(object, attrs):
    """Generate a display string for an object based on some attributes.

    Args:
        object: An object which has specific attributes.
        attrs: An interable of strings containing attributes to get from
            the above object.

    Returns:
        A string containing a list display of the object with respect to
        the passed in attributes.
    """
    return "\n".join(
        click.style(attr, bold=True) + ": %s" % getattr(object, attr)
        for attr in attrs
    )
