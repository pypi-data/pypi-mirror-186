"""Example script generating a message similar to `git_clone -h` as seen in:
https://github.com/jazzband/docopt-ng/blob/master/examples/git/git_clone.py

$ python examples/git_clone_like.py
usage: ssaeiihe u [options] -- [<reoyrtnsi>] [<bhsyslly>]

    --daeceit         Tii aiiee sauii kdsoal gp yad. E sobr ss tdg hmyg. Vwn rhc cso
                      rcoyo ulh r gnse hi v ptma.
    -i <eo>           Cai ehb lrmh bp lroy ied. Elishc misil ona nlpl dccnhr oaueky.

    --cei=<io-rit>    Rstryg oxom tip pt hn ecr hhieo hoc al obu igdea.
    -t                Mnglrc owem plu. Antsioehnrpi dayksn gchtt bex oeee
                      nttter. It abkflr esw reyuor. Nad rggia aw eipeb
                      fcetr hd. Ntan osty edia ag ieee ota.
    -E <hdro>         Aseglp cj nsk ersipn un.
    -f                Als neyn iuefewteothn riekhri naea. Ncbeof avmp oi
                      irlzlprnsslit bdobl dok peiseo sn. Duovpfuab taaa
                      ybnso rhoeey lor ahin eibvm iphl.
    -a                K ifo.

    -r <ulm-dpea>     Mn yg eaya. Os ne cchbs acciltc lctnr.
    -m <sclc>         Llelp ee iil. Faweibtfohr wgresh as.


    --nit             Ddcia e.
    -s <bceonuvm>     Icha panehs aapo ii iwwepw tbastpedkdb. Fickpoafi ig apypf th. Aanan
                      leraus ekreeoc oiiiu rsirr. Nprrfg eete osha. Iecuca
                      wtpiar rzh gotiedli gta eii.
    -h <nhel-afilur>  Smw lorl. Eealanoase dit. Iou s auew ioit ect lktb nlt. Oi utrtikdo
                      haian stlw ovvs. Hya loiwl rtaetgos ihpragheyr oslsi
                      aoreeukrdaei soabe.

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
    argument_repeated=False,
    option_documented_prob=1,
    usage_pattern_capitalized=False,
    number_of_commands=1,
    number_of_options=17,
    option_argument_separator=True,
    option_argument_required=False,
    options_shortcut=True,
    options_style={"style": "between_brackets"},
    number_of_arguments=2,
)


if __name__ == "__main__":
    annot = generator.annotations
    highlight_message(annot)
