"""Contains command for shell completion.

Mostly copied from an example from the click-completion repo; see here:
https://github.com/click-contrib/click-completion/blob/master/examples/click-completion-command
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
import click
import click_completion

CMD_HELP = (
    "Shell completion for click-completion-command. "
    + "Available shell types: "
    + ", ".join(k for k in sorted(click_completion.core.shells.keys()))
    + ". "
    + "Uses current shell type if not specified."
)


@click.group(help=CMD_HELP)
def completion():
    """Command group to generate shell command completions."""
    pass


@completion.command()
@click.option(
    "--append/--overwrite",
    help="Append the completion code to the file",
    default=None,
)
@click.argument(
    "shell",
    required=False,
    type=click_completion.DocumentedChoice(click_completion.core.shells),
)
@click.argument("path", required=False)
def install(append, shell, path):
    """Install the click-completion-command completion."""
    # Install
    shell, path = click_completion.core.install(
        shell=shell, path=path, append=append
    )

    # Report back
    click.echo("%s completion installed in %s" % (shell, path))
