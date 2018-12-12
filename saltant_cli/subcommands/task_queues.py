"""Contains command group for task queues."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
import click
from .resource import (
    generic_create_command,
    generic_get_command,
    generic_list_command,
    generic_put_command,
)
from .utils import list_options

TASK_QUEUE_LIST_ATTRS = (
    "id",
    "user",
    "name",
    "private",
    "active",
    "description",
)
TASK_QUEUE_GET_ATTRS = (
    "id",
    "user",
    "name",
    "description",
    "private",
    "runs_executable_tasks",
    "runs_docker_container_tasks",
    "runs_singularity_container_tasks",
    "active",
)


@click.group()
def task_queues():
    """Command group for task queues."""
    pass


@task_queues.command(name="get")
@click.argument("id", nargs=1, type=click.INT)
@click.pass_context
def get_task_queue(ctx, id):
    """Get task queue based on ID."""
    generic_get_command("task_queues", TASK_QUEUE_GET_ATTRS, ctx, id)


@task_queues.command(name="list")
@list_options
@click.pass_context
def list_task_queues(ctx, filters, filters_file):
    """List task queues matching filter parameters."""
    generic_list_command(
        "task_queues", TASK_QUEUE_LIST_ATTRS, ctx, filters, filters_file
    )


@task_queues.command(name="create")
@click.option("--name", help="The name of the task queue.", required=True)
@click.option(
    "--description", help="A description of the task queue.", default=""
)
@click.option(
    "--private",
    help="Whether the task queue is exclusive to the creator.",
    default=False,
    show_default=True,
    type=click.BOOL,
)
@click.option(
    "--runs-executable-tasks",
    help="Whether the task queue runs executable tasks.",
    default=True,
    show_default=True,
    type=click.BOOL,
)
@click.option(
    "--runs-docker-container-tasks",
    help="Whether the task queue runs Docker container tasks.",
    default=True,
    show_default=True,
    type=click.BOOL,
)
@click.option(
    "--runs-singularity-container-tasks",
    help="Whether the task queue runs Singularity container tasks.",
    default=True,
    show_default=True,
    type=click.BOOL,
)
@click.option(
    "--active",
    help="Whether the task queue is active.",
    default=True,
    show_default=True,
    type=click.BOOL,
)
@click.pass_context
def create_task_queue(ctx, **kwargs):
    """Create a task queue."""
    generic_create_command("task_queues", TASK_QUEUE_GET_ATTRS, ctx, **kwargs)


@task_queues.command(name="put")
@click.argument("id", nargs=1, type=click.INT)
@click.option("--name", help="The name of the task queue.", required=True)
@click.option(
    "--description", help="A description of the task queue.", default=""
)
@click.option(
    "--private",
    help="Whether the task queue is exclusive to the creator.",
    default=False,
    show_default=True,
    type=click.BOOL,
)
@click.option(
    "--runs-executable-tasks",
    help="Whether the task queue runs executable tasks.",
    default=True,
    show_default=True,
    type=click.BOOL,
)
@click.option(
    "--runs-docker-container-tasks",
    help="Whether the task queue runs Docker container tasks.",
    default=True,
    show_default=True,
    type=click.BOOL,
)
@click.option(
    "--runs-singularity-container-tasks",
    help="Whether the task queue runs Singularity container tasks.",
    default=True,
    show_default=True,
    type=click.BOOL,
)
@click.option(
    "--active",
    help="Whether the task queue is active.",
    default=True,
    show_default=True,
    type=click.BOOL,
)
@click.pass_context
def put_task_queue(ctx, id, **kwargs):
    """Update a task queue, overwritting all its attributes."""
    generic_put_command("task_queues", TASK_QUEUE_GET_ATTRS, ctx, id, **kwargs)
