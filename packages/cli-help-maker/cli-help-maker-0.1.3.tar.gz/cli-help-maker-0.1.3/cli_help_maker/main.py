"""CLI module to create a dataset of help messages. """

import random
import textwrap
from itertools import accumulate
from pathlib import Path
from typing import Callable, Iterable, Optional

import srsly
import typer
from pydantic import BaseModel
from rich.progress import track

from cli_help_maker.generator import HelpGenerator

try:
    from ruamel.yaml import YAML

except ModuleNotFoundError:  # pragma: no cover
    # TODO: Extend this message for any library outside of the main
    # dependencies.
    from warnings import warn

    warn(
        textwrap.dedent(
            """To create a dataset from a yaml config file,
        first you need to install ruaml.yaml, either installing
        all the dependencies:

        $ pip install cli-help-maker[all]

        or installing ruaml.yaml:

        $ pip install ruaml.yaml
        """
        )
    )


app = typer.Typer()


class ArgumentField(BaseModel):
    """Pydantic model representing any of the values for an argument.

    Example:
        {'dist': 'range', 'parameters': {'values': [2, 4]}}
    """

    dist: str
    parameters: dict[str, list[float] | int | list[int] | list[str]]


class DatasetConfig(BaseModel):
    """Pydantic model to validate the fields in the .yaml file used to create a dataset.

    The attributes defined are those expected in the dataset.yaml file,
    and the values inside each argument are checked via ArgumentField.
    """

    version: str
    size: int
    arguments: dict[str, ArgumentField]


def read_config(config: Path) -> dict[str, str]:
    """Reads a configuration file with the parameters to create a dataset
    of help messages.

    Parses the values and sets the generator functions for each argument.

    TODO: Document each argument in dataset.yaml:
    For example, indent spaces has a dist parameter which defines the type
    of distribution that should be used to generate the data.
    allowed ones are `uniform` and `constant` for the moment.
    Each dist has arguments, that would depend on the distribution.
    dist:
      uniform
    arguments:
      min: 2
      max: 4

    Args:
        config (Path) Path to the yaml config file.

    Notes
        An example of this file can be seen [here](https://github.com/plaguss/cli-help-maker/dataset.yaml)
    """
    yaml = YAML(typ="safe")  # default, if not specfied, is 'rt' (round-trip)
    with open(config, "r") as f:
        config = yaml.load(f)

    dataset_config = DatasetConfig(**config)

    conf = {
        "version": dataset_config.version,
        "size": dataset_config.size,
        "arguments": {},
    }
    for k, v in dataset_config.arguments.items():
        conf["arguments"][k] = get_distribution(v.dict())

    return conf


def get_distribution(data: dict[str, str | dict[str, int]]) -> Callable:
    """Get the distribution of an argument from the config yaml.

    Args:
        data (dict[str, str | dict[str, int]]):
            Corresponds to an argument in yaml parsed:
            dist: uniform-continuous
            parameters:
                min: 0
                max: 1

    Raises:
        ValueError: When a value is not allowed.
            Mainly checks the values expected in the parameters field for each
            of the 'distributions' selected.

    Returns:
        generator (Callable): A function to generate values according to
            the distribution selected.
    """
    dist, parameters = data.get("dist"), data.get("parameters")

    if dist == "constant":
        if "value" not in parameters.keys():
            raise ValueError(
                f"'constant' dist expects a key 'value', you have: {parameters.keys()}"
            )
        return lambda: parameters["value"]
    elif dist == "set":
        if "values" not in parameters.keys():
            raise ValueError(
                f"'range' dist expects a key 'values', you have: {parameters.keys()}"
            )
        return lambda: random.choice(parameters["values"])
    elif dist == "uniform-discrete":
        if "min" not in parameters.keys() or "max" not in parameters.keys():
            raise ValueError(
                f"'uniform-discrete' dist expects key 'min' and 'max', you have: {parameters.keys()}"
            )
        return lambda: random.randint(parameters["min"], parameters["max"])
    elif dist == "uniform-continuous":
        if "min" not in parameters.keys() or "max" not in parameters.keys():
            raise ValueError(
                f"'uniform-continuous' dist expects key 'min' and 'max', you have: {parameters.keys()}"
            )
        return (
            lambda: parameters["min"]
            + (parameters["max"] - parameters["min"]) * random.random()
        )
    elif dist == "custom":
        if "values" not in parameters.keys() or "p" not in parameters.keys():
            raise ValueError(
                f"'custom' dist expects key 'values' and 'p', you have: {parameters.keys()}"
            )
        return lambda: random.choices(
            population=parameters["values"],
            cum_weights=list(accumulate(parameters["p"])),
        )[0]
    else:
        raise ValueError(f"`dist` field not defined: {dist}")


HelpArgs = dict[str, int | float | bool | str | list[int]]


def argument_generator(
    size: int, input_generator: dict[str, Callable]
) -> Iterable[tuple[HelpArgs, HelpGenerator]]:
    """Helper function to pass the values from
    TODO: DESCRIBE

    The HelpArgs file can be read using pandas.read_json(lines=True)
    Args:
        conf (_type_): _description_
        input_generator (_type_): _description_

    Yields:
        _type_: _description_
    """
    for _ in track(range(size)):  # Value extracted from conf
        # TODO: Get the values from the input generator here to keep track
        # of the values that generated each message (for future use).
        kwargs = {
            "indent_spaces": input_generator["indent_spaces"](),
            "total_width": input_generator["total_width"](),
            "prob_name_capitalized": input_generator["prob_name_capitalized"](),
            "description_before": input_generator["description_before"](),
            "description_after": input_generator["description_after"](),
            "program_description_prob": input_generator["program_description_prob"](),
            "usage_section": input_generator["usage_section"](),
            "usage_pattern_capitalized": input_generator["usage_pattern_capitalized"](),
            "commands_section": input_generator["commands_section"](),
            "commands_header": input_generator["commands_header"](),
            "commands_capitalized": input_generator["commands_capitalized"](),
            "commands_documented_prob": input_generator["commands_documented_prob"](),
            "arguments_section": input_generator["arguments_section"](),
            "arguments_header": input_generator["arguments_header"](),
            "arguments_style": input_generator["arguments_style"](),
            "argument_repeated": input_generator["argument_repeated"](),
            "argument_documented_prob": input_generator["argument_documented_prob"](),
            "arguments_pattern_capitalized": input_generator[
                "arguments_pattern_capitalized"
            ](),
            "argument_capitalized_prob": input_generator["argument_capitalized_prob"](),
            "argument_optional_prob": input_generator["argument_optional_prob"](),
            "options_section": input_generator["options_section"](),
            "options_header": input_generator["options_header"](),
            "option_documented_prob": input_generator["option_documented_prob"](),
            "options_pattern_capitalized": input_generator[
                "options_pattern_capitalized"
            ](),
            "options_shortcut": input_generator["options_shortcut"](),
            "options_shortcut_capitalized_prob": input_generator[
                "options_shortcut_capitalized_prob"
            ](),
            "options_shortcut_all_caps": input_generator["options_shortcut_all_caps"](),
            "exclusive_group_optional_prob": input_generator[
                "exclusive_group_optional_prob"
            ](),
            "options_mutually_exclusive_prob": input_generator[
                "options_mutually_exclusive_prob"
            ](),
            "number_of_commands": input_generator["number_of_commands"](),
            "number_of_arguments": input_generator["number_of_arguments"](),
            "number_of_options": input_generator["number_of_options"](),
            "exclusive_programs": input_generator["exclusive_programs"](),
        }
        yield kwargs


@app.command()
def main(
    input_path: Path = typer.Argument(
        ..., exists=True, dir_okay=False, help="Path pointing to the .yaml file."
    ),
    output_path: Optional[Path] = typer.Argument(
        None,
        help="Dirname of the output path. If not given, creates a directory with the version number",
    ),
):
    """Function to generate a dataset of cli help messages from a .yaml file
    with the info.

    A folder will be generated containing two jsonl files:

    - arguments.jsonl:
        Contains the arguments that were generated, these can be associated to each
        help message for further analysis.

    - dataset.jsonl:
        A dataset of help messages with annotations.
    """

    conf = read_config(input_path)
    input_generator = conf["arguments"]
    if output_path is None:
        output_path = input_path.parent / ("dataset_v" + conf["version"])
        if not output_path.is_dir():
            output_path.mkdir()

    kwargs = list(argument_generator(conf["size"], input_generator))
    srsly.write_jsonl(
        path=output_path / "arguments.jsonl",
        lines=(kw for kw in kwargs),
    )
    srsly.write_jsonl(
        path=output_path / "dataset.jsonl",
        lines=(HelpGenerator(**kw).annotations for kw in kwargs),
    )
    print(f"Directory generated at: {output_path}")


if __name__ == "__main__":
    app()
