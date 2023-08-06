"""Example script as in:
https://github.com/jazzband/docopt-ng/blob/master/examples/naval_fate.py

$ python examples/naval_fate_like.py
Usage: 
  riui iou [--rciep] -r
  riui elmrd mty <ouni-areyt> [<edisne-too>]...
  riui en bva [--et-lkapdd] [-c] [<uohdvr>] <ktnin> [<odbrw>]...
  riui lgeaa <rpnetn-nel-cn> <ambos> [<olemf-oaeptsh>]...
  riui --nc-mrer-clete <tapi> [-n=<n>] [<trs>]...
  riui etsp -v <ys-ht> [<atls>]...

Options:
  --rciep                 Ylasgrt kdnw arrc aedacnd. S osr ut n dnoc. Or ntr. N neo
                          tecas zicln ewlansnl f.
  -r                      Eppm sasf gn pcmcy lpiypm rptipma nefneeb hnn. Hn.
  --et-lkapdd             Ourdepc ayc l eenp. B nud coe mae. Rcl zalfg atan musokar
                          rwrodt.
  -c                      Lpui lsk oeoo burwg. Gdtell aapto ie myeecp npda. Ioli
                          o ior ert. Dts lsit ls aonetst.
  --nc-mrer-clete <tapi>  Oy yot fce tpta albbie. H ietaa rrmrsroce eetu natu eless.
  -n=<n>                  Tstae tnge obe.
  -v <ys-ht>              Meertu o lsaht s nn tegr. Ens rtiunum rano tphke pi.

"""

from cli_help_maker import generator as gen
from cli_help_maker.utils import highlight_message

generator = gen.HelpGenerator(
    prob_name_capitalized=0.0,
    indent_spaces=2,
    usage_section=True,
    options_section=True,
    options_header=True,
    options_shortcut=False,
    arguments_style="between_brackets",
    argument_documented_prob=0.0,
    argument_repeated=True,
    option_documented_prob=1.0,
    description_before=False,
    program_description_prob=0.0,
    number_of_commands=[0, 2],
    number_of_options=[0, 2],
    number_of_arguments=[0, 3],
    exclusive_programs=6,
)


if __name__ == "__main__":
    annot = generator.annotations
    highlight_message(annot)
