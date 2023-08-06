"""Example script generating a message similar to:
https://github.com/jazzband/docopt-ng/blob/master/examples/quick_example.py

$ python examples/quick_example_like.py
Usage: 
  tn sela ianlh [-e <oo>] [-t AYL-MST] [-p] <dttl>
  tn nnrne iro [--adrvni=HALMALE-DC] [--aiv-ce] <cbwn-hudv-egshm>
  tn orn iiihigeycu [-M <rsa-ost>] [<qoti>]

"""

from cli_help_maker import generator as gen
from cli_help_maker.utils import highlight_message

generator = gen.HelpGenerator(
    indent_spaces=2,
    usage_section=True,
    program_description_prob=0.0,
    arguments_section=False,
    options_section=False,
    usage_pattern_capitalized=True,
    number_of_commands=2,
    number_of_options=[1, 3],
    number_of_arguments=[1, 2],
    arguments_style="between_brackets",
    exclusive_programs=3,
)


if __name__ == "__main__":
    annot = generator.annotations
    highlight_message(annot)
