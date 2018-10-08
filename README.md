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

However you choose to install saltant-cli, make sure that the binary
resulting from the above commands are somehwere on your `$PATH`. On some
systems, this may involve running the above commands as root.

### Running from source

Alternatively, instead of installing saltant-cli you can run it directly
from source using the script [`run_saltant_cli.py`](run_saltant_cli.py).

### Shell completion

Assuming you installed normally, i.e., you aren't running from source,
saltant-cli comes with command completion for
[Bash](https://www.gnu.org/software/bash/), [Zsh](https://www.zsh.org/),
[fish](https://fishshell.com/), and
[PowerShell](https://docs.microsoft.com/en-us/powershell/scripting/powershell-scripting?view=powershell-6).

To install any of these, run

```
saltant-cli completion install <my-shell-type>
```

where `my-shell-type` is either `bash`, `zsh`, `fish`, or `powershell`
(or ``—blank—if you want to use the current shell type).
