"""Example script generating a message similar to `git commit -h` as seen in:
https://github.com/jazzband/docopt-ng/blob/master/examples/git/git_commit.py

$ python examples/git_clone_like.py

TODO: Still needs to split options in different sections
"""

from cli_help_maker import generator as gen
from cli_help_maker.utils import highlight_message

generator = gen.HelpGenerator(
    indent_spaces=4,
    prob_name_capitalized=0,
    description_before=False,
    program_description_prob=0.0,
    usage_section=False,
    options_section=True,
    options_header=False,
    arguments_style="between_brackets",
    argument_repeated=True,
    option_documented_prob=0.9,
    usage_pattern_capitalized=False,
    number_of_commands=1,
    number_of_options=30,
    option_argument_separator=True,
    option_argument_required=True,
    options_shortcut=True,
    number_of_arguments=1,
)


if __name__ == "__main__":
    annot = generator.annotations
    highlight_message(annot)
