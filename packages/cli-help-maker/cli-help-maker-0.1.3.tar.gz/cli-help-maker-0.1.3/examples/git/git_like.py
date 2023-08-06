"""Example script generating a message similar to `git -h` as seen in:
https://github.com/jazzband/docopt-ng/blob/master/examples/git/git.py

$ python examples/git/git_like.py
Usage: vstsacmai arase [-g] [-o <aiuv-rr-b>] [--cria-tan] [--aeawol] [-u <cwti-ercp>]
                       [-t] [--l] [--nmw-sried] [--tr] [--pn-aito] <utaem>
                       [<rarboee-ope>]
"""

from cli_help_maker import generator as gen
from cli_help_maker.utils import highlight_message

generator = gen.HelpGenerator(
    prob_name_capitalized=0.0,
    usage_section=False,
    options_section=False,
    options_header=False,
    arguments_style="between_brackets",
    argument_documented_prob=0.0,
    option_documented_prob=0.0,
    description_before=False,
    program_description_prob=0.0,
    number_of_commands=1,
    number_of_options=10,
    options_shortcut=False,
    number_of_arguments=2,
)


if __name__ == "__main__":
    annot = generator.annotations
    highlight_message(annot)
