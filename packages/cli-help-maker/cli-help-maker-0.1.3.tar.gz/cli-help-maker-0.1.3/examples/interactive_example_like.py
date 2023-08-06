"""Example script as in:
https://github.com/jazzband/docopt-ng/blob/master/examples/naval_fate.py

$ python examples/naval_fate_like.py
Til it chi. Ncrqeea imtreea lar erpdcoa fucsa oied colmsl omeris urec nno e
eieit. H tlle urip bncsh sw pnhl ais il newt. Stcn re ailaluionrtt anhvocm.
Trkli ya.

Usage: 
    ebec ovai [-x <ntute-li>] [<naai>]
    ebec [--ashu <ecn> | --prrn-ebb-cetp | -n] <cria-eoaecoi>
    ebec --oep=<snfl> <ilreeeeai-ef>
    ebec --agai-ion <ntes-atonfpts> --ut-aas [-p] [<niohy-oaw>]

Options:
    -x <ntute-li>         Dlaaior stiigaleigyn ht.
    --ashu <ecn>          Namcs iupet mo n gucinv. Ccn ebre rin tn mpu.
    --prrn-ebb-cetp
    -n                    Ggin otucypwe ehay sthcpgcn. Savcl pla nygsyts oah
                          horeaam. Vrighr iw.
    --oep=<snfl>          Vhlontlin nbnys cp ninynhek dc. Ocn tb. Bisco ttio. Ridsrre rbil
                          irike gkaccee sdeue ih sr.
    --agai-ion <ntes-atonfpts>
                          Lsrpcs rcr znkan. Per rl elc shct irte. Eels
                          nieen mscy.
    --ut-aas
    -p                    Mtsj chloii. Rgla eicuye sdr. Eto gebnbsr. S neebmi
                          aatu nhhc. Atnc rrpnclut otpnrb ieoe ltri shia.

"""

from cli_help_maker import generator as gen
from cli_help_maker.utils import highlight_message

generator = gen.HelpGenerator(
    indent_spaces=4,
    usage_section=True,
    usage_pattern_capitalized=True,
    description_before=True,
    program_description_prob=1.0,
    arguments_style="between_brackets",
    options_section=True,
    options_header=True,
    options_style={"style": "between_brackets"},
    options_mutually_exclusive_prob=0.5,
    options_mutually_exclusive_group=3,
    number_of_commands=[0, 1],
    number_of_options=[1, 3],
    number_of_arguments=1,
    exclusive_programs=4,
)


if __name__ == "__main__":
    annot = generator.annotations
    highlight_message(annot)
