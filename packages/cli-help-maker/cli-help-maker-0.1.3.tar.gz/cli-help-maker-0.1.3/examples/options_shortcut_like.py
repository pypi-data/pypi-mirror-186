"""Example script as in:
https://github.com/jazzband/docopt-ng/blob/master/examples/options_shortcut.py

$ python examples/options_shortcut_like.py
Iapje tloeo. Eoe il. Oar egt ea tnn ctia ai ncda metbi.

Usage: 
  em [options] <cnrmensr>

Options:

  -p, --pnsut   Eotstln luru aebmh rpsocg eyies sdofse. Ealtp ayorrsno qhfdrs gecr .
  -y=AENA       Uoa. Yu fcr v hl. Gcep. Lem aa ilegr rrgai f.
  -c            Ptci sltet hg eewiaer. Cbsri eeyu onvaol nbernd ieavsqn se wh
                ecrapc.
  -a, --a-tpys  Smusame em llrcb slrd hcagtl emaile iel. Moslee eypuuad rpmo nrsofnw. Rsw
                oacl smdrains. Otclsto hat dr t. Utt svtmf e.
  --im          Cccaol aehhhs. Aac cca l. Aese gyu mc hninec.


"""

from cli_help_maker import generator as gen
from cli_help_maker.utils import highlight_message

generator = gen.HelpGenerator(
    indent_spaces=2,
    program_description_prob=1,
    arguments_style="between_brackets",
    argument_documented_prob=1.0,
    options_section=True,
    options_header=True,
    options_shortcut=True,
    option_documented_prob=1,
    options_style={"style": "all_caps", "short_long_separator": ", "},
    options_mutually_exclusive_prob=1/15,
    options_mutually_exclusive_group=2,
    number_of_commands=0,
    number_of_options=6,
    number_of_arguments=1,
    exclusive_programs=1,
)


if __name__ == "__main__":
    annot = generator.annotations
    highlight_message(annot)
