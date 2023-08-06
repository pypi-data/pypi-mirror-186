# cli-help-maker
Command Line Interface help message generator.

![ci workflow](https://github.com/plaguss/cli-help-maker/actions/workflows/ci.yml/badge.svg)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![License](https://img.shields.io/badge/github/license/plaguss/cli-help-maker.svg)](https://github.com/plaguss/cli-help-maker)

<!-- [![codecov](https://codecov.io/gh/plaguss/cli-help-maker/branch/main/graph/badge.svg?token=AVKH6TS7G7)](https://codecov.io/gh/plaguss/cli-help-maker) -->

---

This repo contains a CLI to create simulated help messages with the positions annotated
of the commands, arguments and options. Its created as a separated package, but its intended use is to generate datasets to be used in [helpner-core](https://github.com/plaguss/helpner-core), which deals with the model that powers [helpner](https://github.com/plaguss/helpner).

## What range of help messages covers?

For the moment, it indents to recreate messages like those found in the examples of [docopt-ng](https://github.com/jazzband/docopt-ng).
This should cover CLI apps created in python using for example [argparse](https://docs.python.org/3/library/argparse.html), [click](https://click.palletsprojects.com/en/8.1.x/) or [typer](https://typer.tiangolo.com/)*.

*[typer](https://typer.tiangolo.com/) uses click underneath, but when `rich` its is installed, the message has a special (and prettier) layout, currently not in the scope.*

A proper list of items covered is yet to be made.

## Installation

(Once in PyPI, currently not uploaded):

`pip install cli-help-maker`

This creates the following CLI:

```console
❯ cli-help-maker --help
                                                                                                
 Usage: cli-help-maker [OPTIONS] INPUT_PATH [OUTPUT_PATH]                                       
                                                                                                
 Function to generate a dataset of cli help messages from a .yaml file with the info.           
 A folder will be generated containing two jsonl files:                                         
 - arguments.jsonl:     Contains the arguments that were generated, these can be associated to  
 each     help message for further analysis.                                                    
 - dataset.jsonl:     A dataset of help messages with annotations.                              
                                                                                                
╭─ Arguments ──────────────────────────────────────────────────────────────────────────────────╮
│ *    input_path       FILE           Path pointing to the .yaml file. [default: None]        │
│                                      [required]                                              │
│      output_path      [OUTPUT_PATH]  Dirname of the output path. If not given, creates a     │
│                                      directory with the version number                       │
│                                      [default: None]                                         │
╰──────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Options ────────────────────────────────────────────────────────────────────────────────────╮
│ --install-completion        [bash|zsh|fish|powershell|pwsh]  Install completion for the      │
│                                                              specified shell.                │
│                                                              [default: None]                 │
│ --show-completion           [bash|zsh|fish|powershell|pwsh]  Show completion for the         │
│                                                              specified shell, to copy it or  │
│                                                              customize the installation.     │
│                                                              [default: None]                 │
│ --help                                                       Show this message and exit.     │
╰──────────────────────────────────────────────────────────────────────────────────────────────╯
```

## Examples

The folder [examples](https://github.com/plaguss/cli-help-maker/tree/main/examples) contains a rough recreation of some of the examples found in `docopt-ng` repo, to see an example, run any of them, for example:

```bash
python examples/arguments_example_like.py
```

This would create a random help message with a layout similar to the one found in [docopt-ng](https://github.com/jazzband/docopt-ng/blob/master/examples/arguments_example.py) (approximately).

It highlights the labels using rich.


## Development

TBD
