"""Example script generating a message similar to `git remote -h` as seen in:
https://github.com/jazzband/docopt-ng/blob/master/examples/git/git_remote.py

$ python examples/git_add_like.py
usage: ti td sy --ennr-i <e-dme-nyfg> -r <e> [--ynteeao <otd-mso>] [<eic>]
       ti lc [-u=<be-paaimey>] [-a=<aly>] -a=<ynvii-bhs> <arhi-rmuihr>
       ti ldidciheo mme [-o=OBOA-OOCGU] --rynei-nsomnna-ipuc [--lku EAANI] [<ie>]
       ti arueau [-i PT] [-n VBL-I] [-N] <ioroe>
       ti wa [--thtn-mnason] [--msh] [--ea] [<el>]
       ti trrnashhu ea <deeocoi-nrisof>
       ti oa yeiatto [--paph <ioaedcfemd-pyi>] <rffc>
       ti atrieumsmrar drsa -m <ralxo-fehntao> <ogo>
       ti em mrnutbgra --cdfss-sewr [--ers-d] <abcd-eettee>
       ti sysuo ko --enoe-i <tsicaha> [<hyiyaipbr>]
       ti nmuti <ugptt-eeg>
       ti id (-s=<slr-p> | --eni | -i=<ah>) [<euy>]

"""

from cli_help_maker import generator as gen
from cli_help_maker.utils import highlight_message

generator = gen.HelpGenerator(
    indent_spaces=4,
    prob_name_capitalized=0,
    description_before=False,
    program_description_prob=0.0,
    usage_section=False,
    options_section=False,
    options_header=False,
    arguments_style="between_brackets",
    argument_repeated=False,
    option_documented_prob=0.9,
    usage_pattern_capitalized=False,
    number_of_commands=[1, 2],
    number_of_options=[0, 3],
    option_argument_separator=False,
    option_argument_required=False,
    options_mutually_exclusive_group=[0, 3],
    options_mutually_exclusive_prob=7/13,
    options_shortcut=False,
    number_of_arguments=1,
    exclusive_programs=12,
)


if __name__ == "__main__":
    annot = generator.annotations
    highlight_message(annot)
