"""Example script generating a message similar to `git checkout -h` as seen in:
https://github.com/jazzband/docopt-ng/blob/master/examples/git/git_checkout.py

$ python examples/git_checkout_like.py
usage: rokmpnt indeo [options] -- <hlls>...
       rokmpnt atlleu [options] -- <eaat>...


    -u ATENOIU-BRU        Sr nob m eo. Nsvncc yse urtoh. Lglple ar eak.
    -h LPIES-SYEMORR      Rhu wnerm yice. Om lon. Aatsi osz tsmell inpe ms.
    -n RU                 Siureek nfet. Ntctrlr rn.



    --xn=ANDI             Di sry oeei eoo ifunaa enl. Lnu meys ahot. Ilrr neftc rtnon.
                          Iihu tnsoanch. Mltu rgcsee ndd lii nvie oael .
    --it-wlbyfude=LASI-A  Tasj yia hb. Hres crlaas. Otelcl taec oootf lbe os nndleljldeiftsee.
                          Enplts tryrr rcnni lk lvkewli nmihpar chbg phbs.
                          Araee pitdpia nao. P.
    -a --ahulalasl-tuarlh
                          Vg rhhme ooid. Io an cfuste sau.
    -c                    Naasutohsi tlsdis aeist gmiholla ybeneaeam. Oed
                          rfsedraitu. Refh mca s l vcd.

"""

from cli_help_maker import generator as gen
from cli_help_maker.utils import highlight_message

generator = gen.HelpGenerator(
    indent_spaces=4,
    prob_name_capitalized=0,
    description_before=False,
    program_description_prob=0.0,
    usage_section=False,
    usage_pattern_capitalized=False,
    arguments_style="between_brackets",
    argument_repeated=True,
    options_section=True,
    options_header=False,
    option_documented_prob=1.0,
    options_shortcut=True,
    option_argument_separator=True,
    option_argument_required=False,
    number_of_commands=1,
    number_of_options=12,
    number_of_arguments=[1, 2],
    exclusive_programs=2,
)

if __name__ == "__main__":
    annot = generator.annotations
    highlight_message(annot)
