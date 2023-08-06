"""Example script generating a message similar to:
https://github.com/jazzband/docopt-ng/blob/master/examples/options_example.py

$ python examples/options_example_like.py
I li. Nnnfeenhca. Talmonsao rsi. H arc ylwslreneol.

Usage: 
  lbdef ro --iiispn-atinn=OOCSID --lgt=NRO [-C] [-a] (-m=M-P | -e)
  lbdef edr [--rmkni S] [--ign-tmua-ccop] [-a] GDABN-ATS...
  lbdef oneib --whua=EPKSSL [-e] --crbheus [-s] -m [-t] [--y-rhiart=INYA]
                   -t=PRLHL

Arguments:
  GDABN-ATS  Tuilnbm r liob peae. Gisox houheiee lhdp roc.

Options:
  --iiispn-atinn=OOCSID  Ossecn eao lsson kte.
  --lgt=NRO              Pitn affde tme or aieba pnca. Shupi oewslaer wcarrtcbm ohzobr
                         s.
  -C                     Oa awg aowdc fet e.
  -a                     Fndvrc eejo oie. Oniank dhmtccfm hger teonie
                         ochmpasnnempl akyebsn. Onnr rlwnrllngb eegty. Nrn
                         ijvrrlg.
  -m=M-P                 Vaiioop owp aca r cnrp aataemeegp. P elci golu ytom ntn.
  -e                     Vdiemdue elerr eoiapf t ri ratet isagfd nawae eflialk
                         nocu aioa. Evivri ic tio. W.
  --rmkni S              Tae sdoyott sr roehi vwpo. Oam dcldii. Ge uhin isre ew.
  --ign-tmua-ccop        Ea nee ars go elesi aoislg. Lanf r.
  -a                     Ao ietc rh osi. Uo tr oaopbpi hrs bc ufyeerdo. Yyst
                         nhaksriat rbeveu rmtenpq smu wr.
  --whua=EPKSSL          Eoyksyq eyoo rlt oaain nhdn. Vd. Mir orhea csiseal moi.
  -e                     Yaa ngad aioeer. Artieop tc. Laer habc. All sde ls tt
                         er rbe. Gnerp elet lmunh cf gua lb pen tx ngrlepe.
                         Cnu emopck daubt tc sn.
  --crbheus              Baecy aueerhbul conx rce oren. Tph toeble oo cpuort nyeno na
                         paainob.
  -s                     Olbhccna ery. Aa rst koosnsrae fak le.
  -m                     Eiud egtncts gleeee eae lao cl odoe.
  -t                     Rla hso l olhir. Lplesn rl.
  --y-rhiart=INYA        Ip ato utoeuh lemre ir csaouet tcanhor. T ons ktzmatcr. Eeml thcroud
                         lrooa rarri iopob acuu.
  -t=PRLHL               Gspel urrrrt icf. M hnbnsot pubs pas. S st mmau. Kyhaupt
                         ooci. Leradop iaae.

"""

from cli_help_maker import generator as gen
from cli_help_maker.utils import highlight_message

generator = gen.HelpGenerator(
    indent_spaces=2,
    program_description_prob=1,
    arguments_style="all_caps",
    argument_repeated=0.9,  # TODO: Needs a probability
    arguments_header=True,
    arguments_section=True,
    argument_documented_prob=1.0,
    options_section=True,
    options_header=True,
    option_documented_prob=1,
    options_style={"style": "all_caps"},
    options_mutually_exclusive_prob=1/15,
    options_mutually_exclusive_group=2,
    number_of_commands=1,
    number_of_options=[1, 8],
    number_of_arguments=[0, 1],
    exclusive_programs=3,
)


if __name__ == "__main__":
    annot = generator.annotations
    highlight_message(annot)
