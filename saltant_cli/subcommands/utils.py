"""Contains utility functions to reduce repetitive code."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
import json
import click


def list_options(func):
    """Adds in --filters and --filters-file options for a command."""
    filters_option = click.option(
        '--filters',
        help="Filter keys and values encoded in JSON.",
        default=None,
        type=click.STRING,)
    filters_file_option = click.option(
        '--filters-file',
        help="Filter keys and values encoded in a JSON file.",
        default=None,
        type=click.Path(),)

    return filters_option(filters_file_option(func))


def combine_filter_json(filters, filters_file):
    """Combines filter JSON sources for a list command."""
    combined_filters = {}

    if filters is not None:
        combined_filters.update(json.loads(filters))

    if filters_file is not None:
        with open(filters_file) as f:
            combined_filters.update(json.load(f))

    return filters
