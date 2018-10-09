[![Build Status](https://travis-ci.com/mwiens91/saltant-cli.svg?branch=master)](https://travis-ci.com/mwiens91/saltant-cli)
[![codecov](https://codecov.io/gh/mwiens91/saltant-cli/branch/master/graph/badge.svg)](https://codecov.io/gh/mwiens91/saltant-cli)
[![PyPI](https://img.shields.io/pypi/v/saltant-cli.svg)](https://pypi.org/project/saltant-cli/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/saltant-cli.svg)](https://pypi.org/project/saltant-cli/)

# saltant CLI

### Work in progress D:

saltant-cli is a CLI for [saltant](https://github.com/mwiens91/saltant)
written on top of [saltant-py](https://github.com/mwiens91/saltant-py).
It lets you interface with a saltant API conveniently from a terminal.

## Installation

Using pip,

```
pip install saltant-cli
```

or, from source, after cloning this repository, run

```
python setup.py install
```

where `python` is in versions 2.7 or 3.5+.

However you chose to install saltant-cli, make sure that the binary
resulting from the above commands are somewhere on your `$PATH`. On some
systems, this may involve running the above commands as root.

### Running from source

Alternatively, instead of installing saltant-cli you can run it directly
from source using the script [`run_saltant_cli.py`](run_saltant_cli.py).

### Setting up a configuration file

In order to run saltant-cli, it needs to know where your saltant server
is and how to authenticate your user. To get this information,
saltant-cli looks for a config file located at
`$XDG_CONFIG_HOME/saltant-cli/config.yaml`; if `$XDG_CONFIG_HOME` isn't
defined, `$HOME/.config` is used instead. Alternatively, you can use a
`config.yaml` file at the root of the project's repository, which is
useful when running from source.

The easiest way to set up a config file is to run

```
saltant-cli --setup
```

which interactively constructs and writes a config file to
`$XDG_CONFIG_HOME/saltant-cli/config.yaml`.

Alternatively, you can copy the example config file,
[`config.yaml.example`](config.yaml.example), to where it needs to go,
and fill in the file with your favourite text editor:

```
mkdir -p $XDG_CONFIG_HOME/saltant-cli
cp config.yaml.example $XDG_CONFIG_HOME/saltant-cli/config.yaml
```

There may be times where it is advantageous to juggle multiple config
files; to do so, you can specify the `--config-path` option, like so:

```
saltant-cli --config-path /path/to/config.yaml mycommandhere
```

### Shell command completion

Assuming you installed normally, i.e., you aren't running from source,
saltant-cli supports command completion for
[Bash](https://www.gnu.org/software/bash/), [Zsh](https://www.zsh.org/),
[fish](https://fishshell.com/), and
[PowerShell](https://docs.microsoft.com/en-us/powershell/scripting/powershell-scripting?view=powershell-6).

To install any of these, run

```
saltant-cli completion install my-shell-type
```

where `my-shell-type` is either `bash`, `zsh`, `fish`, or `powershell`
(or blank if you want to use the current shell type).

## Usage

Here you're going to find `--help` your best friend. Run this at any
stage of the command tree to learn more about what to do!

### Commmand tree

Here's a sketch of what you can do. Again, supply `--help` at any point
to figure out how to use a given command.

```
saltant-cli
├── completion
│   └── install
├── container-task-instances
│   ├── clone
│   ├── create
│   ├── get
│   ├── list
│   ├── terminate
│   └── wait
├── container-task-types
│   ├── create
│   ├── get
│   └── list
├── executable-task-instances
│   ├── clone
│   ├── create
│   ├── get
│   ├── list
│   ├── terminate
│   └── wait
├── executable-task-types
│   ├── create
│   ├── get
│   └── list
├── task-queues
│   ├── create
│   ├── get
│   └── list
└── users
    ├── get
    └── list
```

### Examples

Let's go through a few examples. First, let's list some container task
types using some API filters:

```
saltant-cli container-task-types list --filters '{"user_username_in": ["matt", "daniel"]}'
```

Great! This will show us the container task types created by Matt and
Daniel! Secondly, let's create a task queue:

```
saltant-cli task-queues create --name "amazing-task-queue" --description "Seriously best task queue ever."
```

If we got confused about how to use this command, all we need to do is
drop in `--help`. Thirdly: let's do just that:

```
saltant-cli task-queues create --help
```

which will give us

```
$ saltant-cli task-queues create --help
Usage: saltant-cli task-queues create [OPTIONS]

  Create a task queue.

Options:
  --name TEXT         The name of the task queue.  [required]
  --description TEXT  A description of the task queue.
  --private BOOLEAN   Whether the task queue is exclusive to the creator.
                      [default: False]
  --active BOOLEAN    Whether the task queue is active.  [default: True]
  --help              Show this message and exit.
```

## See also

[saltant-py](https://github.com/mwiens91/saltant-py/), a saltant SDK for
Python.
