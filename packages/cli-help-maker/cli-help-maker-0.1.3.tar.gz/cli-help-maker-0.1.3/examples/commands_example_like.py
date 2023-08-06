"""Example script generating a message similar to:
https://github.com/jazzband/docopt-ng/blob/master/examples/options_example.py
but including commands

$ python examples/commands_example_like.py

TODO: ADAPT TO INCLUDE COMMAND SECTION
"""

from cli_help_maker import generator as gen
from cli_help_maker.utils import highlight_message

generator = gen.HelpGenerator(
    indent_spaces=2,
    program_description_prob=1,
    commands_header=True,
    commands_section=True,
    commands_capitalized=1,
    commands_documented_prob=0.5,
    arguments_style="all_caps",
    argument_repeated=0.9,
    arguments_header=True,
    arguments_section=True,
    argument_documented_prob=1.0,
    options_section=True,
    options_header=True,
    option_documented_prob=1,
    options_style={"style": "all_caps"},
    options_mutually_exclusive_prob=1 / 15,
    options_mutually_exclusive_group=2,
    number_of_commands=[1, 3],
    number_of_options=[1, 8],
    number_of_arguments=[0, 1],
    exclusive_programs=3,
)


if __name__ == "__main__":
    annot = generator.annotations
    highlight_message(annot)
