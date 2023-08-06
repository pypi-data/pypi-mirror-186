"""Example script generating a message similar to `git branch -h` as seen in:
https://github.com/jazzband/docopt-ng/blob/master/examples/git/git_branch.py

$ python examples/git/git_branch_like.py
usage: aasn ekoefek -w [--sil] [-m CCGESB-HS]
       aasn qmrn (-r LRPY | -s) [--pmimaldf=ILAEI-DCA]
       aasn sm --on=<ltvl-eloirg> [-y SODNAG-FAEITO]
       aasn miar [-c <tc> | --nsueegror=TLAAR-MNSIOC] --loraos=ODRALER-RIFESNI --coce
                 <n>

    -w                    Luetkcll cuedc. R nx ty yee krme pa eeyl. Dfael ati
                          rew airvlprteegds ehb. Sva an aarngsaaa oe.
    --sil                 Tf ecyuethd. Ogm aecc atem uipbcdnis upos. Nirl sr kud.
    -m CCGESB-HS          Avrau eit aisumeueio sfee qer te. Issli eesedtl. Iounrfhblx
                          oyirn tdiu nsg torfl en t. Eehr yeu galt bsae as
                          ye.
    -r LRPY               Nsnf ooha halihrvh oool dks upvaelaan. Oteu duegae hge ade
                          ngaui nlnsne. Ymi tieib. Aase nic ryclnm ieaege
                          phahan al.
    -s                    Apeng djd otfooe cfic oaee aasi irlo chs g.
    --pmimaldf=ILAEI-DCA  Pre irpao wnlnsgnohon spu frnccr rpoitio ntil bcpsit. Nozb ucan.
                          Vihhbaom ec rwfji ffp rslxrldri nse gtil tceitp
                          oie ok.
    --on=<ltvl-eloirg>    Rdas opoosp bigi. Nhln apn otmelaxtn cc aat. Selsios ariyic aloyslaa
                          emtsc alieomepd ml.
    -y SODNAG-FAEITO      Yryoi y niw aerc lagep taos eteuy. Verts otiltwa ohaaurwau tsiglga
                          dnpto zcolag. Scaaein ie reeta cmvmiroioae laas
                          gdmstr rp emn yrmmm.
    -c <tc>               Aur clsmupr oia. Aows trrrba latbt oucimti a. Nicl ens wr
                          igtes cid omslri r pe oase.
    --nsueegror=TLAAR-MNSIOC
                          Slcetnp yyulea uma cru baaeos tat. Wrpne
                          slypnaat easm tmge erfe sesmset lsaaa ltsgfspb.
                          Rrat hcdvr derdr.
    --loraos=ODRALER-RIFESNI
                          Ikahbu. Scc te nki lop. Cubnier eoklb grn lcar r
                          tpwn mc yptl cpe .
    --coce                Uborsoi ngss reeyswue bu. Nac rpi xgi k eonoefnw snpn raor
                          nci ss. Opeeuperyt emddseo nr ddbismzq ortrr.

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
    argument_repeated=False,
    options_section=True,
    options_header=False,
    option_documented_prob=1.0,
    options_shortcut=False,
    options_mutually_exclusive_group=[0, 2],
    options_mutually_exclusive_prob=3/13,
    number_of_commands=1,
    number_of_options=[2, 4],
    number_of_arguments=[0, 2],
    exclusive_programs=4,
)


if __name__ == "__main__":
    annot = generator.annotations
    highlight_message(annot)
