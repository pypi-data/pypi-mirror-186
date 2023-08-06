r"""Example script generating a message similar to:
https://github.com/jazzband/docopt-ng/blob/master/examples/arguments_example.py

$ python examples/arguments_example_like.py 
Usage: 
  itetoia od n [-m <hroivwek>] [-o CE] CUIR-AOO
  itetoia imgad nhl [-a <nce-ustn>] [--nth] [--pave=BLET-EIITOMNFEO] [CHKN]

Fn eouho bwxs ocolioar asrie la. Ww u.

Arguments:
  CUIR-AOO  Uvfa rf au. Iwi mlmrveoe. Tnovvr omd rore.
  CHKN      Eteo eeeas raabl stin dld utl.

Options:
  -m <hroivwek>           Osn dga zuysm dtr. Opnnmoa amsc nadtee yyni ieccb sn.
  -o CE                   Sju ten rece rstg pc. Ag irek lsrhscan. Bublfie reic oc
                          ntfdd fpki rdrno rccnb. Dics coene.
  -a <nce-ustn>           Frr sefh sat vtri tthc. Vengtd sgrlh. Aele dlrfceagcu. Meor aemra
                          ok. Hn oe uoaityn alht lllk. Irn sol.
  --nth                   Israwo lbu lpie onhc rcaerrrs. Yrd ru peio.
  --pave=BLET-EIITOMNFEO  Utei s ttht dehrid tcu uap cfyoetri soylcrnosdioirp. Eieao om ty. Npoei
                          utoge.

"""

from rich import print

from cli_help_maker import generator as gen
from cli_help_maker.utils import highlight_message

generator = gen.HelpGenerator(
    indent_spaces=2,
    usage_section=True,
    usage_pattern_capitalized=True,
    program_description_prob=1.0,
    description_before=False,
    arguments_section=True,
    arguments_header=True,
    arguments_style="all_caps",
    options_section=True,
    options_header=True,
    number_of_commands=2,
    number_of_options=[1, 3],
    number_of_arguments=1,
    exclusive_programs=2,
)


if __name__ == "__main__":
    annot = generator.annotations
    highlight_message(annot)
