"""This file contains tests of the different functions used in cli_help_maker.generator.HelpGenerator.

Some tests may be better as unit tests, but others are interconected to other calls,
so all the tests for the class are written here.
"""


import random

import pytest

import cli_help_maker.generator as gen
from cli_help_maker.utils import highlight_message

FIXED_SEED = 6798


@pytest.fixture()
def help_generator_default():
    yield gen.HelpGenerator(
        indent_spaces=4,
        prob_name_capitalized=0,
        total_width=78,
        description_before=True,
        description_after=False,
        program_description_prob=0.5,
        usage_section=True,
        usage_pattern_capitalized=True,
        commands_section=False,
        commands_header=False,
        commands_capitalized=0,
        commands_documented_prob=0.01,
        arguments_section=False,
        arguments_header=False,
        arguments_style="between_brackets",
        argument_repeated=0.0,
        argument_documented_prob=0.9,
        arguments_pattern_capitalized=True,
        argument_capitalized_prob=0,
        argument_optional_prob=0.5,
        options_style={},
        options_section=False,
        options_header=False,
        option_documented_prob=0.9,
        options_pattern_capitalized=True,
        option_argument_separator=False,
        option_argument_required=False,
        options_mutually_exclusive_prob=0.0,
        options_mutually_exclusive_group=0,
        read_from_stdin=False,  # TODO: Not taken into account yet
        options_shortcut=1,
        options_shortcut_capitalized_prob=0.001,
        options_shortcut_all_caps=0,
        exclusive_group_optional_prob=0.5,
        number_of_commands=1,
        number_of_arguments=2,
        number_of_options=3,
        exclusive_programs=1,
    )


# Some basic tests just to ensure they are covered
def test_help_message(help_generator_default):
    assert help_generator_default.help_message == ""
    assert help_generator_default._current_length == 0
    help_generator_default.help_message = "some text"
    assert help_generator_default.help_message == "some text"
    assert help_generator_default._current_length == len("some text")


# Some basic tests just to ensure they are covered
def test_number_of_commands(help_generator_default):
    assert help_generator_default.number_of_commands == 1


def test_number_of_arguments(help_generator_default):
    assert help_generator_default.number_of_arguments == 2


def test_number_of_options(help_generator_default):
    assert help_generator_default.number_of_options == 3


@pytest.mark.parametrize(
    "help_gen, value, expected",
    [
        ("help_generator_default", 0, (0, 0)),
        ("help_generator_default", 1, (1, 1)),
        ("help_generator_default", 2, (2, 2)),
        ("help_generator_default", [0, 2], (0, 2)),
        ("help_generator_default", [1, 2], (1, 2)),
        ("help_generator_default", [3], (3, 3)),
        ("help_generator_default", "bad value", (3, 3)),
    ],
)
def test_check_number_of_elements(help_gen, value, expected, request):
    help_gen = request.getfixturevalue(help_gen)
    if isinstance(value, str):
        with pytest.raises(ValueError):
            help_gen._check_number_of_elements(value)

    else:
        opt = help_gen._check_number_of_elements(value)
        assert opt == expected


def test_description(help_generator_default):
    assert isinstance(help_generator_default._description(), str)


def test_program_name(help_generator_default):
    assert isinstance(help_generator_default._program_name(), str)


def test_commands(help_generator_default):
    cmds = help_generator_default._commands(total=-1)
    assert len(cmds) == 0
    assert len(help_generator_default._command_names) == 0
    cmds = help_generator_default._commands(total=0)
    assert len(cmds) == 0
    assert len(help_generator_default._command_names) == 0
    cmds = help_generator_default._commands(total=1)
    assert len(cmds) == 1
    cmds = help_generator_default._commands(total=9)
    assert len(cmds) == 9
    assert len(help_generator_default._command_names) == 10


@pytest.mark.parametrize(
    "help_gen, values, expected",
    [
        ("help_generator_default", ({}, False, False), "-P <untholeable>"),
        ("help_generator_default", ({}, False, True), "-P <untholeable>"),
        ("help_generator_default", ({}, True, True), "-d <tara-myxopoda>"),
        ("help_generator_default", ({}, True, True), "-d <tara-myxopoda>"),
    ],
)
def test_option(help_gen, values, expected, request):
    help_gen = request.getfixturevalue(help_gen)
    random.seed(FIXED_SEED)
    opt = help_gen._option(*values)
    assert opt == expected


@pytest.mark.parametrize(
    "help_gen, values, expected",
    [
        ("help_generator_default", (0, False, False), 0),
        ("help_generator_default", (1, False, False), 1),
        ("help_generator_default", (2, False, False), 2),
    ],
)
def test_options(help_gen, values, expected, request):
    help_gen = request.getfixturevalue(help_gen)
    opt = help_gen._options(*values)
    assert len(opt) == expected


@pytest.mark.parametrize(
    "help_gen, value, expected",
    [
        ("help_generator_default", 0, "[<areel-spaniellike>]"),
        ("help_generator_default", 1, "<areel-spaniellike>"),
    ],
)
def test_argument(help_gen, value, expected, request):
    help_gen = request.getfixturevalue(help_gen)
    random.seed(FIXED_SEED)
    arg = help_gen._argument(value)
    assert arg == expected


def test_argument_repeated(help_generator_default):
    assert len(help_generator_default._argument_names) == 0
    help_generator_default._argument_names.append("[<areel-spaniellike>]")
    assert help_generator_default._argument_names[0] == "[<areel-spaniellike>]"
    random.seed(FIXED_SEED)
    arg = help_generator_default._argument(0)
    assert arg == "[<areel-spaniellike>]"


@pytest.mark.parametrize(
    "help_gen, values, expected",
    [
        ("help_generator_default", (0, False), 0),
        ("help_generator_default", (1, False), 1),
        ("help_generator_default", (2, False), 2),
        ("help_generator_default", (2, True), 2),
    ],
)
def test_arguments(help_gen, values, expected, request):
    help_gen = request.getfixturevalue(help_gen)
    help_gen._argument_repeated = values[1]
    args = help_gen._arguments(total=values[0])
    if values[1] is True:
        assert args[-1].endswith("...")
    assert len(args) == expected


@pytest.mark.parametrize(
    "help_gen, values, expected",
    [
        ("help_generator_default", ("program", 0, True, True), 1),
        ("help_generator_default", ("program", 1, True, True), 2),
        ("help_generator_default", ("program", 2, True, True), 3),
        ("help_generator_default", ("program", 2, True, False), 2),
        ("help_generator_default", ("program", 1, True, False), 1),
    ],
)
def test_add_programs(help_gen, values, expected, request):
    # Tests for the number of programs generated.
    # Removes the trailing whitespaces and sets all the string to lower,
    # Then splits by usage: , which should be the initial string in the
    # message, and grabs the second piece (anything but the usage section),
    # then splits by jump of lines and grabs from the first (which doesn't have
    # anything) up to the last, to count the programs
    help_gen = request.getfixturevalue(help_gen)
    help_gen._exclusive_programs = values[1]
    help_gen._options_section = values[2]
    help_gen._usage_section = values[3]
    help_gen._add_programs(values[0])
    print("msg before", help_gen.help_message)
    msg = help_gen.help_message.lstrip().lower().split("usage: ")[1].split("\n")[1:]
    print("msg after strip", msg)
    assert len(msg) == expected


@pytest.mark.parametrize(
    "help_gen, values, expected",
    [
        (
            "help_generator_default",
            ("program", True, 0, False, False),
            "program [options]",
        ),
        (
            "help_generator_default",
            ("program", True, 1, False, False),
            "program impermanent [options] <chink>",
        ),
        ("help_generator_default", ("program", True, 10, False, False), 1),
        (
            "help_generator_default",
            ("program", True, 1, True, False),
            "program commercialist [options] -- <dispart>",
        ),
        (
            "help_generator_default",
            ("program", True, 1, True, True),
            "program parasubstituted [options] [--] [<atoke-semiconvergent>]",
        ),
    ],
)
def test_add_program(help_gen, values, expected, request):
    help_gen = request.getfixturevalue(help_gen)
    help_gen.number_of_commands = values[2]
    help_gen.number_of_arguments = values[2]
    help_gen.number_of_options = values[2]
    help_gen._option_argument_separator = values[3]
    help_gen._option_argument_required = values[4]
    help_gen._add_program(values[0], options_in_section=values[1])
    msg = help_gen.help_message
    print("Help:")
    print(msg)
    if isinstance(expected, str):
        assert msg == expected
    else:
        # The last parametrized test only checks the program has more than one
        # line, by checking the split by \n. 10 as with this much content, for the
        # total width set, there must be more than one line
        assert len(msg.split("\n")) > expected


# fmt: off
labels = [
    [],  # 0
    [('CMD', 5, 16), ('OPT', 17, 21), ('ARG', 22, 33)],  # 1
    [('CMD', 5, 16), ('CMD', 17, 31), ('OPT', 32, 36), ('OPT', 37, 41), ('ARG', 42, 62), ('ARG', 63, 75)],  # 2
    [
        ('CMD', 5, 16), ('CMD', 17, 31), ('CMD', 32, 48), ('OPT', 49, 51), ('OPT', 52, 54), ('OPT', 55, 59),
        ('ARG', 60, 70), ('ARG', 79, 95), ('ARG', 96, 106)
    ],  # 3
    [
        ('CMD', 5, 16), ('CMD', 17, 31), ('CMD', 32, 48), ('CMD', 49, 59), ('OPT', 60, 62), ('OPT', 63, 65),
        ('OPT', 66, 70), ('OPT', 71, 75), ('ARG', 84, 93), ('ARG', 94, 106), ('ARG', 107, 118), ('ARG', 119, 130)
    ],  # 4
    [
        ('CMD', 5, 16), ('CMD', 17, 31), ('CMD', 32, 48), ('CMD', 49, 59), ('CMD', 60, 68), ('OPT', 69, 73), 
        ('OPT', 74, 78), ('OPT', 87, 91), ('OPT', 92, 96), ('OPT', 97, 101), ('ARG', 102, 124), ('ARG', 125, 138), 
        ('ARG', 139, 150), ('ARG', 159, 168), ('ARG', 169, 180)
    ],  # 5
    [
        ('CMD', 5, 16), ('CMD', 17, 31), ('CMD', 32, 48), ('CMD', 49, 59), ('CMD', 60, 68), ('CMD', 77, 90), 
        ('OPT', 91, 95), ('OPT', 96, 98), ('OPT', 99, 103), ('OPT', 104, 106), ('OPT', 107, 111), ('OPT', 112, 160), 
        ('ARG', 161, 170), ('ARG', 171, 188), ('ARG', 189, 202), ('ARG', 203, 213), ('ARG', 222, 239), ('ARG', 240, 261)
    ],  # 6
    [
        ('CMD', 5, 16), ('CMD', 17, 31), ('CMD', 32, 48), ('CMD', 49, 59), ('CMD', 60, 68), ('CMD', 77, 90), 
        ('CMD', 91, 102), ('OPT', 103, 107), ('OPT', 108, 159), ('OPT', 160, 176), ('OPT', 177, 179), 
        ('OPT', 180, 182), ('OPT', 183, 252), ('OPT', 253, 268), ('ARG', 277, 297), ('ARG', 298, 323), 
        ('ARG', 324, 338), ('ARG', 347, 371), ('ARG', 372, 382), ('ARG', 383, 391), ('ARG', 392, 431)
    ],  # 7
    [
        ('CMD', 5, 16), ('CMD', 17, 31), ('CMD', 32, 48), ('CMD', 49, 59), ('CMD', 60, 68), 
        ('CMD', 77, 90), ('CMD', 91, 102), ('CMD', 103, 113), ('OPT', 114, 116), ('OPT', 117, 166), 
        ('OPT', 167, 185), ('OPT', 186, 190), ('OPT', 191, 195), ('OPT', 196, 265), ('OPT', 266, 279), 
        ('OPT', 280, 311), ('ARG', 312, 333), ('ARG', 334, 358), ('ARG', 367, 390), ('ARG', 391, 411), 
        ('ARG', 412, 437), ('ARG', 446, 469), ('ARG', 470, 495), ('ARG', 496, 507)
    ],  # 8  # Mal
    [
        ('CMD', 5, 16), ('CMD', 17, 31), ('CMD', 32, 48), ('CMD', 49, 59), ('CMD', 60, 68), ('CMD', 77, 90), 
        ('CMD', 91, 102), ('CMD', 103, 113), ('CMD', 114, 127), ('OPT', 128, 178), ('OPT', 179, 199), 
        ('OPT', 200, 218), ('OPT', 227, 231), ('OPT', 232, 236), ('OPT', 237, 295), ('OPT', 304, 319), 
        ('OPT', 320, 343), ('OPT', 344, 361), ('ARG', 362, 373), ('ARG', 382, 397), ('ARG', 398, 421), 
        ('ARG', 422, 463), ('ARG', 464, 477), ('ARG', 478, 490), ('ARG', 491, 528), ('ARG', 529, 540), 
        ('ARG', 541, 566)
    ],  # 9
    [
        ('CMD', 5, 16), ('CMD', 17, 31), ('CMD', 32, 48), ('CMD', 49, 59), ('CMD', 60, 68), 
        ('CMD', 77, 90), ('CMD', 91, 102), ('CMD', 103, 113), ('CMD', 114, 127), ('CMD', 128, 133), 
        ('OPT', 134, 184), ('OPT', 185, 203), ('OPT', 204, 220), ('OPT', 229, 233), ('OPT', 234, 238), 
        ('OPT', 239, 297), ('OPT', 306, 319), ('OPT', 320, 345), ('OPT', 346, 363), ('OPT', 364, 366), 
        ('ARG', 375, 389), ('ARG', 390, 404), ('ARG', 405, 416), ('ARG', 417, 440), ('ARG', 449, 463), 
        ('ARG', 464, 484), ('ARG', 485, 500), ('ARG', 501, 531), ('ARG', 532, 554), ('ARG', 555, 572)
    ],  # 10
    [
        ('CMD', 5, 16), ('CMD', 17, 31), ('CMD', 32, 48), ('CMD', 49, 59), ('CMD', 60, 68), 
        ('CMD', 77, 90), ('CMD', 91, 102), ('CMD', 103, 113), ('CMD', 114, 127), ('CMD', 128, 133), 
        ('CMD', 134, 145), ('CMD', 154, 167), ('CMD', 168, 172), ('CMD', 173, 181), ('CMD', 182, 195), 
        ('OPT', 196, 198), ('OPT', 199, 203), ('OPT', 204, 208), ('OPT', 209, 253), ('OPT', 254, 281), 
        ('OPT', 282, 312), ('OPT', 313, 329), ('OPT', 330, 357), ('OPT', 366, 383), ('OPT', 384, 388), 
        ('OPT', 389, 407), ('OPT', 408, 429), ('OPT', 430, 434), ('OPT', 443, 459), ('OPT', 460, 462), 
        ('ARG', 463, 478), ('ARG', 479, 495), ('ARG', 496, 529), ('ARG', 530, 541), ('ARG', 542, 551), 
        ('ARG', 552, 560), ('ARG', 561, 585), ('ARG', 594, 610), ('ARG', 611, 622), ('ARG', 623, 649), 
        ('ARG', 658, 681), ('ARG', 682, 694), ('ARG', 695, 710), ('ARG', 711, 753), ('ARG', 754, 765)
    ],  # 11 # Mal, solo captura algunos comandos
]
# fmt: on

# FIXME: A bug places the annotations separated by a single position in most cases
# (only when the program has more than 3 lines), and other times even full
@pytest.mark.parametrize(
    "help_gen, values, expected",
    [
        ("help_generator_default", ("prog", True, 0, False, False), labels[0]),
        ("help_generator_default", ("prog", True, 1, False, False), labels[1]),
        ("help_generator_default", ("prog", True, 2, False, False), labels[2]),
        ("help_generator_default", ("prog", True, 3, False, False), labels[3]),
        ("help_generator_default", ("prog", True, 4, False, False), labels[4]),
        ("help_generator_default", ("prog", True, 5, False, False), labels[5]),
        ("help_generator_default", ("prog", True, 6, False, False), labels[6]),
        ("help_generator_default", ("prog", True, 7, False, False), labels[7]),
        ("help_generator_default", ("prog", True, 8, False, False), labels[8]),
        ("help_generator_default", ("prog", True, 9, False, False), labels[9]),
        ("help_generator_default", ("prog", True, 10, False, False), labels[10]),
        ("help_generator_default", ("prog", True, 15, False, False), labels[11]),
        # ("help_generator_default", ("prog", True, 20, False, False), labels[12]),
        # ("help_generator_default", ("prog", True, 30, False, False), labels[13]),
        # ("help_generator_default", ("prog", True, 50, False, False), labels[14]),
    ],
)
def test_add_annotations(help_gen, values, expected, request):
    random.seed(FIXED_SEED)
    help_gen = request.getfixturevalue(help_gen)
    help_gen._options_shortcut = False
    help_gen.number_of_commands = values[2]
    help_gen.number_of_arguments = values[2]
    help_gen.number_of_options = values[2]
    help_gen._option_argument_separator = values[3]
    help_gen._option_argument_required = values[4]
    help_gen._add_program(values[0], options_in_section=values[1])
    msg = help_gen.help_message
    ann = help_gen._annotations
    # ann = 1
    print("annotations:")
    print(ann)
    print("highlight:")
    highlight_message({"message": msg, "annotations": ann})
    assert ann == expected
    if len(ann) > 0:
        assert len(msg) >= ann[-1][-1]


msgs = [
    "Commands:\n    longcommandname0000000000000000\n\
                          Pterobranchia deacetylate spiritland. Tara\n\
                          myxopoda microcellular ordinary napoleonite\n\
                          undersurface keratomycosis. Crossleted sturnoid\n\
                          jactitate opulency misestimate unpredisposed\n\
                          ruffle psychophysicist hymenic genitoria.\n"
]


@pytest.mark.parametrize(
    "help_gen, values, expected",
    [
        ("help_generator_default", ([], True, "Commands", True, 0.0), ""),
        (
            "help_generator_default",
            (["cmd1"], True, "Commands", True, 0.0),
            "Commands:\n    cmd1\n",
        ),
        (
            "help_generator_default",
            (["cmd1", "cmd2", "cmd3"], True, "Commands", True, 0.0),
            "Commands:\n    cmd1\n    cmd2\n    cmd3\n",
        ),
        ("help_generator_default", ([""], True, "Commands", True, 0.0), ""),
        (
            "help_generator_default",
            (["longcommandname0000000000000000"], True, "Commands", True, 1.0),
            msgs[0],
        ),
        ("help_generator_default", (["", "", ""], True, "Commands", True, 0.0), ""),
        (
            "help_generator_default",
            (["arg1"], True, "arguments", True, 0.0),
            "Arguments:\n    arg1\n",
        ),
        (
            "help_generator_default",
            (["opt1"], True, "options", True, 0.0),
            "Options:\n    opt1\n",
        ),
    ],
)
def test_add_section(help_gen, values, expected, request):
    random.seed(FIXED_SEED)
    elements, has_header, section_name, capitalized, documented_prob = values
    help_gen = request.getfixturevalue(help_gen)
    # help_gen.number_of_commands = values[2]
    # help_gen.number_of_arguments = values[2]
    # help_gen.number_of_options = values[2]
    # help_gen._option_argument_separator = values[3]
    # help_gen._option_argument_required = values[4]

    help_gen._add_section(
        elements, has_header, section_name, capitalized, documented_prob
    )
    msg = help_gen.help_message
    assert msg == expected


docs = [
    "name  Pterobranchia deacetylate spiritland. Tara myxopoda microcellular\n\
 ordinary napoleonite undersurface keratomycosis. Crossleted sturnoid\n\
 jactitate opulency misestimate unpredisposed ruffle psychophysicist\n\
 hymenic genitoria."
]


@pytest.mark.parametrize(
    "help_gen, values, expected",
    [
        ("help_generator_default", ("name", 1, 1, 0.0), "name"),
        ("help_generator_default", ("name", 1, 1, 1.0), docs[0]),
    ],
)
def test_add_documentation(help_gen, values, expected, request):
    random.seed(FIXED_SEED)
    elements, longest_elem, length, probability = values
    help_gen = request.getfixturevalue(help_gen)
    elem = help_gen._add_documentation(elements, longest_elem, length, probability)
    assert elem == expected


@pytest.mark.parametrize(
    "help_gen, values, expected",
    [
        ("help_generator_default", (0.0, False, False), 0),
        ("help_generator_default", (0.0, True, True), 0),
        ("help_generator_default", (1.0, False, False), 0),
        ("help_generator_default", (1.0, True, False), 0),
        ("help_generator_default", (1.0, False, True), 0),
        ("help_generator_default", (1.0, True, True), 0),
    ],
)
def test_add_program_description(help_gen, values, expected, request):
    desc_prob, desc_before, desc_after = values
    help_gen = request.getfixturevalue(help_gen)
    help_gen._program_description_prob = desc_prob
    help_gen._description_before = desc_before
    help_gen._description_after = desc_after
    help_gen._add_program_description()
    elem = help_gen.help_message
    if (desc_prob > 0) and (desc_before is True or desc_after is True):
        assert len(elem) > expected
    else:
        assert len(elem) == expected


@pytest.mark.parametrize(
    "help_gen, values, expected",
    [
        ("help_generator_default", (False, False, False), "commands:"),
        ("help_generator_default", (True, False, False), "commands:"),
        ("help_generator_default", (False, True, False), "arguments:"),
        ("help_generator_default", (False, False, True), "options:"),
    ],
)
def test_sample(help_gen, values, expected, request):
    commands_section, arguments_section, options_section = values
    help_gen = request.getfixturevalue(help_gen)
    help_gen._commands_section = commands_section
    help_gen._commands_header = commands_section
    help_gen._arguments_section = arguments_section
    help_gen._arguments_header = arguments_section
    help_gen._options_section = options_section
    help_gen._options_header = options_section
    msg = help_gen.sample().lower()
    if any(values):
        assert expected in msg
    else:
        assert expected not in msg


def test_annotations(help_generator_default):
    ann = help_generator_default.annotations
    assert isinstance(ann, dict)
    keys = ["message", "annotations"]
    assert all([k in keys for k in ann.keys()])
