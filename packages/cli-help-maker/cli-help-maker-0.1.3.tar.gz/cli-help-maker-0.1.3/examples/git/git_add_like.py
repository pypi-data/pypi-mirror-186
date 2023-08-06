"""Example script generating a message similar to `git add` as seen in:
https://github.com/jazzband/docopt-ng/blob/master/examples/git/git_add.py

$ python examples/git_add_like.py
usage: nyia in [options] [--] [<efxr-se>]...

    -E, --ecaf            Ni mdm. Ae tabcct roi yonrp. Cmcu liotci ir lbdoc udwcann dn
                          cbr. Eioieds scsftemll d.
    -o, --oeiur           Eg ks aic. Cpedrdna s grri.
    -w <oorp>
    -l O                  Thlu eli ih.
    -e OMS-EP             On lhayt olq sl.
    --ewdptte=<irtatl-lunoojon>
                          Ks uai eenatb ua hrcn eii elomnl. Es rfes tto.
                          Aiy nti.
    -c                    Ohswaewe dn iue cvre ouo.
    --tnir                Tca aiebrv php mee or oeeiab siegrmtw rgrf cnihw abp. Hrdm
                          siitbsao.
    -h --hdraexpio-ssoe-vicp
                          Esl mr uerlerm. Ratim slec eesdoietg. Neeahgn
                          ffrrvasta oarmm teia emi wmmeid mlsi ness ivleil
                          rci. Nfstir rhk aeo. Ck tnrxrneep.
    -i PRUSTNJ-T          Eb ccva vsis aninkvfmnd cdab ejp. Tu oics acee. Hpo tlbeoo
                          pmfyao oars eg.
    --ce=MASO             Ryhghrea is.
                      Inoha mad np lei. Sc taaa.

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
    number_of_options=13,
    option_argument_separator=True,
    option_argument_required=True,
    options_shortcut=True,
    number_of_arguments=1,
)


if __name__ == "__main__":
    annot = generator.annotations
    highlight_message(annot)
