"""Module in charge of generating CLI help messages. 

Currently only docopt is allowed.
"""

import difflib
import random
import textwrap
from textwrap import indent

from .utils import (
    capitalize,
    do_mutually_exclusive_groups,
    do_optional,
    get_word,
    make_argument,
    make_list,
    make_option,
    make_paragraph,
    maybe_do_optional,
    options_shortcut,
    section_pattern,
    usage_pattern,
)

text_wrapper = textwrap.TextWrapper(width=78)


"""Labels for the pieces to find in the message. """
CMD = "CMD"  # Command
ARG = "ARG"  # Argument
OPT = "OPT"  # Option


class HelpGenerator:
    """Class in charge of generating a help message and
    keep track of the steps involved to obtain the labeled
    content.

    If the option arguments_in_section is set to False,
    argument_documented_prob won't be used as they won't
    be documented.

    Multiple program lines after the usage pattern mean
    several exclusive patterns.
    When exclusive_programs is used, the number of commands, options
    and arguments would be used for each exclusive program.
    """

    def __init__(
        self,
        indent_spaces: int = 2,
        prob_name_capitalized: float = 0,
        total_width: int = 78,
        description_before: bool = True,
        description_after: bool = False,
        program_description_prob: float = 0.5,
        usage_section: bool = True,
        usage_pattern_capitalized: str = True,
        commands_section: bool = False,
        commands_header: bool = False,
        commands_capitalized: float = 0,
        commands_documented_prob: float = 0.01,
        arguments_section: bool = False,
        arguments_header: bool = False,
        arguments_style: str = "between_brackets",
        argument_repeated: float = 0.0,
        argument_documented_prob: float = 0.9,
        arguments_pattern_capitalized: str = True,
        argument_capitalized_prob: float = 0,
        argument_optional_prob: float = 0.5,
        options_style: dict = {},
        options_section: bool = False,
        options_header: bool = False,
        option_documented_prob: float = 0.9,
        options_pattern_capitalized: str = True,
        option_argument_separator: bool = False,
        option_argument_required: bool = False,
        options_mutually_exclusive_prob: float = 0.0,
        options_mutually_exclusive_group: int = 0,
        read_from_stdin: bool = False,  # TODO: Not taken into account yet
        options_shortcut: float = 0,
        options_shortcut_capitalized_prob: float = 0.001,
        options_shortcut_all_caps: float = 0,
        exclusive_group_optional_prob: float = 0.5,
        number_of_commands: int | list[int] = 0,
        number_of_arguments: int | list[int] = 0,
        number_of_options: int | list[int] = 0,
        exclusive_programs: int = 1,
    ) -> None:
        """_summary_

        Args:
            indent_spaces (int, optional): _description_. Defaults to 2.
            prob_name_capitalized (float, optional): Probability of the program name
                being capitalized. Defaults to 0.
            total_width (int): Total width allowed for the message. Defaults to 80
            description_before (bool): Whether to add description for the program
                before or after the program name.
            program_description_prob (float) TODO
            usage_section (bool) Determines the layout for the programs.
                It True, the programs are generated as a section, similar
                to optiosn and arguments. Defaults to True.
            options_style (dict, optional): _description_. Defaults to {}.
            options_header (bool, optional): _description_. Defaults to True.
            REMOVE usage_first_line_aligned (bool, optional): _description_. Defaults to False.
            argument_repeated (bool, optional): If given, the last argument
                can have any number of arguments. Defaults to False.
            arguments_documented (bool, optional): Whether an argument
                is documented. CHANGE TO A PROBABILITY. Defaults to False
            arguments_in_section (bool, optional): If True, writes the arguments
                on its own section, otherwise they are written as single
                line programs. Defaults to False
            option_documented_prob (float): Probability of documenting each
                option. Defaults to 0.9.
            options_mutually_exclusive (dict[str, float | int])
                Dict containing info with the probabilities of arguments being
                grouped. `probability` defines the probability of the elements
                being grouped, and `group` refers to the possible elements being
                grouped. The possible values are checked just like for number_of_...
                arguments. Wheter the grouped elements are optional or not, will
                be determined via the probability of the elements being optional.
                A list with a range of [0, 2] means at most 2 elements could
                be grouped.
            options_style (dict). Used to pass determined options' arguments instead
                of taking them randomly.
            exclusive_programs (int): Number of exclusive programs, according
                to the usage pattern. When only one is given, a single program
                definition occurs. Used to differentiate between different subcommands
                or different meaning of the arguments. Defaults to 1.
        """
        self._help_message = ""
        self._current_length = 0
        self._annotations = []
        # To keep track of the options and arguments, in case
        # they are added as a single line and documented on
        # a different section.
        self._command_names = []
        self._option_names = []
        self._argument_names = []
        # Layout options
        self._total_width = int(total_width)
        self._prob_name_capitalized = prob_name_capitalized
        self._options_style = options_style
        self._indent_spaces = int(indent_spaces)
        self._usage_section = usage_section  # Used to split the programs in a section
        # or in the same line with indentation.
        self._usage_pattern_capitalized = usage_pattern_capitalized

        self._commands_section = commands_section
        self._commands_header = commands_header
        self._commands_capitalized = commands_capitalized
        self._commands_documented_prob = commands_documented_prob

        self._arguments_section = arguments_section
        self._arguments_header = arguments_header
        self._arguments_style = arguments_style
        self._argument_repeated = argument_repeated
        self._argument_documented_prob = argument_documented_prob
        self._arguments_pattern_capitalized = arguments_pattern_capitalized
        self._argument_capitalized_prob = argument_capitalized_prob
        self._argument_optional_prob = argument_optional_prob

        self._options_section = options_section
        self._options_header = options_header
        self._option_documented_prob = option_documented_prob
        self._option_argument_separator = option_argument_separator
        self._option_argument_required = option_argument_required
        self._options_pattern_capitalized = options_pattern_capitalized
        self._options_mutually_exclusive_prob = options_mutually_exclusive_prob
        self._options_mutually_exclusive_group = self._check_number_of_elements(
            options_mutually_exclusive_group
        )
        self._options_shortcut = random.random() > (1 - options_shortcut)
        self._options_shortcut_capitalized_prob = options_shortcut_capitalized_prob
        self._options_shortcut_all_caps = options_shortcut_all_caps

        self._exclusive_group_optional_prob = exclusive_group_optional_prob
        # Program description probability
        self._description_before = description_before
        self._description_after = description_after
        self._program_description_prob = program_description_prob
        self._read_from_stdin = read_from_stdin
        self._exclusive_programs = int(exclusive_programs)

        # Explain this is to allow working with a number of
        # exclusive_programs > 1
        self.number_of_commands = number_of_commands
        self.number_of_arguments = number_of_arguments
        # If options_shortcut is True, write at least one option
        if self._options_shortcut:  # pragma: no cover
            number_of_options = max(1, number_of_options)

        self.number_of_options = number_of_options

        # Variables used to control the proper positioning
        # of the docs
        self._max_level_docs = int(1 / 3 * self._total_width)
        self._remaining_space_option_docs = int(
            self._total_width - self._max_level_docs
        )
        self._docs_limited = False

    @property
    def help_message(self) -> str:
        """Anytime the message is updated, the current lenght
        is updated when the setter is called."""
        return self._help_message

    @help_message.setter
    def help_message(self, msg: str) -> str:
        self._help_message = msg
        self._current_length = len(self._help_message)

    @property
    def number_of_commands(self) -> int:
        return self._number_of_commands()

    @number_of_commands.setter
    def number_of_commands(self, number: int | list[int]) -> None:
        l, h = self._check_number_of_elements(number)
        self._number_of_commands = lambda: random.randint(l, h)

    @property
    def number_of_arguments(self) -> int:
        return self._number_of_arguments()

    @number_of_arguments.setter
    def number_of_arguments(self, number: int | list[int]) -> None:
        l, h = self._check_number_of_elements(number)
        self._number_of_arguments = lambda: random.randint(l, h)

    @property
    def number_of_options(self) -> int:
        return self._number_of_options()

    @number_of_options.setter
    def number_of_options(self, number: int | list[int]) -> None:
        l, h = self._check_number_of_elements(number)
        self._number_of_options = lambda: random.randint(l, h)

    def _check_number_of_elements(self, number: int | list[int]) -> tuple[int, int]:
        """Checks the inputs given on number of commands or options.

        This arguments are expected to be an int, a list with one or two ints.
        """
        if isinstance(number, (int, float)):
            l, h = int(number), int(number)
        elif isinstance(number, list):
            if len(number) == 1:
                l, h = int(number[0]), int(number[0])
            else:
                l, h = int(number[0]), int(number[1])
        else:
            raise ValueError(f"Must be an int or a list of 2 ints, given: {number}")
        return l, h

    def _description(self) -> str:
        desc = make_paragraph()
        return textwrap.fill(
            desc, width=self._total_width, initial_indent="", subsequent_indent=""
        )

    @staticmethod
    def _program_name() -> str:
        """Returns a name for the app."""
        return get_word()

    def _commands(self, total: int = 0) -> list[str]:
        """Returns commands for the app."""
        commands = []
        while len(commands) < total:
            c = self._program_name()
            if len(c) > 2:
                commands.append(c)
                self._command_names.append(c)

        return commands

    def _option(
        self, options_arguments: dict, in_section: bool, from_program: bool
    ) -> str:
        """Creates an option for the message.

        A small subset of the arguments is generated here, those are allowed
        to behave differently across the same program.

        the names are stored in a internal variable to get them back.

        Args:
            options_arguments dict: Extra keyword arguments to be passed to make_options.
                Not used currently, they are overwritten.
            in_section (bool): Whether the option is generated for a section or not.
                For a section, every option is allowed, while if its in a program,
                only one of the options will be selected.
            from_program (bool): See _options for the description.

        Returns:
            str: optional argument.
        """
        # These are dependent of the point where they are generated:
        if in_section:
            kwargs = {
                "short": random.choice([True, False]),
                "long": random.choice([True, False]),
                "with_value": random.choice([True, False]),
            }

        else:
            short = random.choice([True, False])
            long = not short
            kwargs = {
                "short": short,
                "long": long,
                "with_value": random.choice([True, False]),
            }

        options_arguments.update(
            {
                "short_capitalized_prob": 0.1,
                "long_capitalized_prob": 0,
            },
            **kwargs,
        )
        options_arguments.update(**self._options_style)

        option = make_option(**options_arguments)

        # TODO: Consider using only the long name if available.
        self._option_names.append(option)

        if from_program:
            # Avoids inserting both a short and a long option in the
            # usage section
            new_opt = option.split(" --")
            if len(new_opt) == 2:
                option = "--" + new_opt[-1]

        return option

    def _options(
        self, total: int = 0, in_section: bool = False, from_program: bool = False
    ) -> list[str]:
        """Adds options to the help message.

        If `options_header` is set on construction, these will
        be written in a separate section.

        The options' layout is generated here to impose all the options
        for a program adhere to the same style.

        Args:
            total (int, optional): Number of options to generate. Defaults to 0.
            in_section (bool, optional): Whether the options are generated
                for a section or not. The arguments for the
                generator are slightly different. Defaults to False.
            from_program (bool, optional): Used to determine if the method
                is called from _add_program, to avoid inserting an option
                with both short and long option in the usage section.
                Defaults to False.

        Returns:
            list[str]: list of options to be added to the message.
        """
        kwargs = {
            "short_separator": random.choice(["=", " "]),
            "long_separator": random.choice(["=", " "]),
            "short_long_separator": random.choice([", ", " "]),
            "probability_name_cap": 0,
            "probability_value_cap": 0,
            "style": random.choice(["between_brackets", "all_caps"]),
        }
        # Easy way to remove optiosn which appear from make_option as ""
        options = []
        for _ in range(total):
            o = self._option(kwargs, in_section, from_program)
            if len(o) > 0:
                options.append(o)

        return options

    def _argument(self, optional_probability: float = 0.5) -> str:
        """Creates an argument for a program.

        Args:
            optional_probability (float, optional): probability of the argument
                being optional. Defaults to 0.5.

        Returns:
            str: argument name
        """
        # FIXME: Arguments capitalized exist?
        arg = make_argument(
            capitalized_prob=0,
            style=self._arguments_style,
        )
        # if the name was already generated (it can happen statistically...)
        # try again, just once and expect it doesn't happen again.
        if arg in self._argument_names:  # pragma: no cover
            arg = make_argument(
                capitalized_prob=0,
                style=self._arguments_style,
            )

        self._argument_names.append(arg)
        if random.random() > optional_probability:
            arg = do_optional(arg)

        return arg

    def _arguments(self, total: int = 0) -> list[str]:
        """Generates a list of arguments. The last one can be repeated

        Args:
            total (int, optional): Number of arguments. Defaults to 0.

        Returns:
            list[str]: list of arguments for the program.
        """
        args = [
            self._argument(optional_probability=self._argument_optional_prob)
            for _ in range(total)
        ]

        if random.random() > (1 - self._argument_repeated):
            if len(args) > 0:
                args[-1] = args[-1] + "..."

        return args

    def _add_programs(self, prog_name: str) -> None:
        """Creates a series of programs (line by line).

        The number of programs depends on the number written in
        self._exclusive_programs.

        Args:
            prog_name (str): Name of the program, this field is repeated
            for successive program examples.
        """
        usage = usage_pattern(capitalized=self._usage_pattern_capitalized)
        self.help_message += usage

        if self._usage_section:
            self.help_message += "\n"
            indent_level = self._indent_spaces
        else:
            indent_level = len(usage)

        # If there are no exclusive programs, dont't do anything.
        # It there is one, let the options generated to be different
        # (as if added in a section).
        # Otherwise, generate multiple programs as is.
        def add_prog(indent_level, prog_name, options_in_section):
            self.help_message += " " * indent_level
            self._add_program(prog_name, options_in_section=options_in_section)
            self.help_message += "\n"

        if self._exclusive_programs == 1:
            if self._usage_section:
                level = indent_level
            else:
                level = 0

            add_prog(level, prog_name, self._options_section)

        elif self._exclusive_programs > 1:
            for i in range(self._exclusive_programs):
                level = 0 if (i == 0 and not self._usage_section) else indent_level
                add_prog(level, prog_name, False)

    def _add_program(self, prog_name: str, options_in_section: bool = False) -> None:
        """Single line program generator.

        Uses the program name as this may be reused.

        TODO: Keep track of the elements for the labels
        Args:
            prog_name : str
            number : int. Number of program written.
                For the moment is a simple way of keeping track of the indentation.
        """
        program = prog_name
        # Initialize the start of the first label
        start = self._current_length + len(program) + 1
        # initial_length is a control variable to check the
        # length of the program before and after calling textwrap.
        initial_length = self._current_length
        annotations = []

        cmds = self._commands(total=self.number_of_commands)

        for i, c in enumerate(cmds):
            if i == 0:
                # In the first step, start counting from the current program
                # length, plus the program name, plus 1 for the initial ' '.
                end = start + len(c)
            else:
                start = end + 1
            end = start + len(c)
            program += " " + c
            annotations.append((CMD, start, end))

        # FIXME: THE INDENTATION HAS A MUCH BIGGER LENGTH AND FORCES textwrap
        # TO WRITE EVERYTHING IN A COLUMN
        # For the length of the indentation, the relevant part are the program
        # name and subcommands
        subsequent_indent = (
            # len(program)  # TODO: when a program is to long, this forces to indent the text as a column
            +len(usage_pattern(capitalized=self._usage_pattern_capitalized))
            + 1
        )
        if self._options_shortcut:
            program += " " + options_shortcut(
                capitalized_probability=self._options_shortcut_capitalized_prob,
                all_caps=self._options_shortcut_all_caps,
            )

        if self._option_argument_separator:
            sep = "--"
            if self._option_argument_required:
                sep = maybe_do_optional(sep, probability=0.5)

            # TODO: Not yet decided if this should be annotated
            program += " " + sep

        # 3) options
        opts = self._options(
            total=self.number_of_options,
            in_section=options_in_section,
            from_program=True,
        )
        # If there are elements to group, do it first, then keep going:
        opts = do_mutually_exclusive_groups(
            elements=opts,
            probability=self._options_mutually_exclusive_prob,
            groups=self._options_mutually_exclusive_group,
            optional_probability=self._exclusive_group_optional_prob,
        )
        # With options shortcut, these get written directly in a section
        if self._options_shortcut:
            self._option_names = opts
            opts = []

        for i, o in enumerate(opts):
            # Only add the option if contained anything.
            if len(o) > 0:  # pragma: no cover
                if not "|" in o:
                    # Check for the pipe operator to avoid possibly making
                    # the argument twice optional.
                    o = maybe_do_optional(o, probability=0.5)

                if (i == 0) and (len(cmds) == 0):
                    start = self._current_length + len(program) + 1
                else:
                    # If there was at least one command added, start
                    # from there
                    start = end + 1

                end = start + len(o)
                program += " " + o
                annotations.append((OPT, start, end))

        # 4) arguments
        args = self._arguments(total=self.number_of_arguments)

        for i, a in enumerate(args):
            if i == 0:
                start = (
                    self._current_length + len(program) + 1
                )  # Program plus the previous space
            else:
                start = end + 1
            end = start + len(a)
            program += " " + a
            annotations.append((ARG, start, end))

        # FIXME: AS THE TEXT IS WRAPPED TO HAVE A NICE ERROR MESSAGE,
        # THE ANNOTATIONS ARE MISPLACED AND THE POSITIONS MUST BE
        # CORRECTED TO BE PROPERLY POSITIONED

        filled_program = textwrap.fill(
            program,
            width=self._total_width,
            initial_indent="",
            subsequent_indent=" " * subsequent_indent,
        )
        self.help_message += filled_program
        self._add_annotations(program, filled_program, annotations, initial_length)

    def _add_annotations(
        self,
        program: str,
        filled_program: str,
        annotations: list[tuple[str, int, int]],
        initial_length: int,
    ) -> None:
        """Corrects the annotations if necessary and stores them.

        Args:
            program (str): Original program as a string.
            filled_program (str): Program corrected by textwrapper. May be the same as
                program if the total_width wasn't exceeded.
            annotations (list[tuple[str, int, int]]): List with 3 element tuple that
                represents the label, the start and end of the label in the program.
            initial_length (int): Initial length of the program name as a string.
        """
        # Compare only the length to see if they are the same
        if len(program) == len(filled_program):
            [
                self._annotations.append((label, start, end))
                for label, start, end in annotations
            ]
            return

        # Obtain the blocks which allow to place the annotations
        # generated in the original program on the "filled" program
        blocks = list(
            difflib.SequenceMatcher(a=program, b=filled_program, autojunk=False).get_matching_blocks()
        )[:-1]

        remain = 0  # Variable to avoid checking again blocks in the inner block.
        inc = 0  # increment in the positions from the original program to the filled one.
        # TODO: New variable to control the positions of the blocks,
        # it is used when in a given line we have to access the following block
        j = 0
        for label, start, end in annotations:
            for i, b in enumerate(blocks[remain:]):
                if b.a == b.b == 0:
                    # Corresponds to the first line of a program, doesn't need adjustment
                    if end <= (b.size + initial_length):
                        # Example: (start 9, end 15) Match(a=0, b=0, size=78)
                        # The following print is just let for possible debugging
                        # print(
                        #     "first block",
                        #     (start, end),
                        #     b,
                        #     program[(start - initial_length) : (end - initial_length)],
                        # )
                        self._annotations.append((label, start, end))

                    elif (start <= (b.size + initial_length)) and (
                        end >= (b.size + initial_length)
                    ):
                        # Starts in the first line and continues to the next (an
                        # element which spans for more than one line)
                        # Adjusts for the indentation added, and grabs the next block
                        # Example: (start 77, end 110) Match(a=0, b=0, size=78)
                        idx = j if (j + 1) >= len(blocks) else (j+1)
                        b = blocks[idx]
                        inc = b.b - b.a
                        self._annotations.append((label, start, end + inc))
                        remain += 1
                        j += 1

                    else:
                        # This one is the first case from the next block.
                        # Behaves as the previous block, but increments both the start
                        # and the end of the span, as this one pertains completely
                        # to a single line
                        # Example: (start 86, end 99) Match(a=0, b=0, size=78)
                        # To avoid requesting a block over the last one
                        idx = j if (j + 1) >= len(blocks) else (j+1)
                        b = blocks[idx]
                        inc = b.b - b.a
                        self._annotations.append((label, start + inc, end + inc))
                        remain += 1
                        j += 1

                    break

                else:
                    # Second line plus.
                    if (start > b.a + initial_length) and (
                        end <= (b.a + b.size + initial_length)
                    ):
                        # General case
                        # Example: (start 86, end 99) Match(a=0, b=0, size=78)
                        self._annotations.append((label, start + inc, end + inc))

                    elif (start <= b.a + b.size + initial_length) and (
                        end > (b.a + b.size + initial_length)
                    ):
                        old_inc = inc
                        b = blocks[j + 1]
                        inc = b.b - b.a
                        self._annotations.append((label, start + old_inc, end + inc))
                        remain += 1
                        j += 1

                    else:
                        # Example: (start 86, end 99) Match(a=0, b=0, size=78)
                        # To avoid requesting a block over the last one
                        idx = j if (j + 1) >= len(blocks) else (j+1)

                        b = blocks[idx]
                        inc = b.b - b.a  # - 1  # Add one for the \n ?
                        self._annotations.append((label, start + inc, end + inc))
                        remain += 1
                        j += 1

                    break

    def _add_section(
        self,
        elements: list[str],
        has_header: bool,
        section_name: str,
        capitalized: bool,
        documented_prob: float,
    ) -> None:
        """Adds a section with options or arguments to list and maybe explain (document)
        the elements.

        Args:
            elements (list[str]) Contains the commands, arguments or options to add.
            has_header (bool) Whether to insert a header or not.
            section_name (str) 'arguments' or 'options' by default. TBD, not prepared
                to add random named section.
            capitalized (bool) 'arguments' or 'options' by default. TBD, not prepared
                to add random named section.
            documented_prob (float) Probability of options or arguments being documented.
        """
        if len(elements) > 0:
            if len(elements[0]) == 0:
                # To avoid writing a section header in the case that only one
                # option is generated and has no content
                return

            if has_header:
                self.help_message += section_pattern(
                    section_name, capitalized=capitalized
                )
                self.help_message += "\n"

            elem_lengths = [len(e) + self._indent_spaces + 2 for e in elements]
            longest_opt = max(elem_lengths)

            if any(l > self._max_level_docs for l in elem_lengths):
                self._docs_limited = True
                longest_opt = self._max_level_docs

            for e, length in zip(elements, elem_lengths):
                # FIXME: This should be controlled in the moment the string is created
                if len(e) == 0:  # pragma: no cover
                    continue
                elem = indent(e, " " * self._indent_spaces)

                start = self._current_length + len(" " * self._indent_spaces)
                end = start + len(e)

                if section_name == "options":
                    label = OPT
                elif section_name == "arguments":
                    label = ARG
                else:
                    label = CMD

                self._annotations.append((label, start, end))

                elem = self._add_documentation(
                    elem,
                    longest_opt,
                    length,
                    documented_prob,
                )

                self.help_message += elem + "\n"

            self._docs_limited = False

    def _add_documentation(
        self, element: str, longest_elem: int, length: int, probability: float
    ) -> str:
        """Adds documentation to an alement.

        Can be used in commands, arguments or options.

        Args:
            element (str): A command, argument or an option.
            longest_elem (int): The number of characters of the longest element.
            length (int): The number of characters of the current element.
            probability (float): Probability of adding docs to the element.

        Returns:
            str: Element with the description attached.
        """
        if random.random() > (1 - probability) and len(element) > 0:
            next_line = False
            if length > longest_elem:
                next_line = True
                length = longest_elem

            if self._docs_limited and next_line:
                element += "\n"
                initial_indent = subsequent_indent = self._max_level_docs
            else:
                initial_indent = longest_elem - length + 2
                subsequent_indent = longest_elem

            wp = textwrap.TextWrapper(
                width=self._total_width - self._indent_spaces,
                initial_indent=" " * initial_indent,
                subsequent_indent=" " * subsequent_indent,
            )
            docs = make_paragraph()
            pieces = wp.wrap(docs)
            # TODO: Not controlled yet
            # To control the length of the first line,
            # otherwise, given the smaller initial indent, doesn't
            # know the total length and the content is displaced to the right.
            # The first line is splitted to allow TextWrapper to wrap it correctly.
            # if len(pieces[0]) > (self._total_width - self._max_level_option_docs):
            #     pieces_ = [pieces[0][:self._remaining_space_option_docs],  " " * subsequent_indent + pieces[0][self._remaining_space_option_docs:]]
            #     if len(pieces) > 1:
            #         pieces = pieces_ + pieces[1:]
            #     else:
            #         pieces = pieces_
            description = "\n".join(pieces)
            # description = wp.fill(docs)
            element += description
        return element

    def _add_program_description(self) -> None:
        """Add the program description.

        There is a probability of 1/5 of having a list of items in the description.
        """
        if random.random() > (1 - self._program_description_prob):
            desc = self._description()
        else:
            desc = ""

        if len(desc) > 0:

            if random.random() > 0.2:
                desc += (
                    "\n" * 2
                    + make_list(
                        elements=random.randint(2, 5),
                        numbered=bool(random.randint(0, 1)),
                    )
                    + "\n"
                )

            msg = ""
            if self._description_before:
                msg = desc + "\n" * 2
            if self._description_after:
                msg = "\n" + desc + "\n"

            self.help_message += msg

    def sample(self) -> str:
        """Generates a sample help message.

        Returns:
            str: random help message.
        """
        if self._description_before:
            self._add_program_description()

        prog_name = capitalize(
            self._program_name(), probability=self._prob_name_capitalized
        )
        self._add_programs(prog_name)

        if self._description_after:
            self._add_program_description()

        def add_section(
            section_name,
            elements,
            number_of_elements,
            elements_header,
            elements_capitalized,
            elements_doc_prob,
        ): # pragma: no cover
            if section_name == "commands":
                f = self._commands
                kwargs = {"total": number_of_elements}
            elif section_name == "arguments":
                f = self._arguments
                kwargs = {"total": number_of_elements}
            else:
                f = self._options
                kwargs = {"total": number_of_elements, "in_section": True}

            self.help_message += "\n"

            if not elements:  # If no element was previously defined, do it here
                elements = f(**kwargs)

            self._add_section(
                elements=elements,
                has_header=elements_header,
                section_name=section_name,
                capitalized=elements_capitalized,
                documented_prob=elements_doc_prob,
            )

        if self._commands_section:
            add_section(
                "commands",
                self._command_names,
                self.number_of_commands,
                self._commands_header,
                self._commands_capitalized,
                self._commands_documented_prob,
            )

        if self._arguments_section:
            add_section(
                "arguments",
                self._argument_names,
                self.number_of_arguments,
                self._arguments_header,
                self._arguments_pattern_capitalized,
                self._argument_documented_prob,
            )

        if self._options_section:
            add_section(
                "options",
                self._option_names,
                self.number_of_options,
                self._options_header,
                self._options_pattern_capitalized,
                self._option_documented_prob,
            )

        return self.help_message

    @property
    def annotations(self) -> dict[str, str | list[tuple[str, int, int]]]:
        """Returns the message ready as an input for a NER model.
        Its a dict with the content in the message key, and
        the labels in the annotations key. The annotations correspond
        to a list of tuples with 3 elements, the label, the character where
        the label starts in the string, and the end.
        This object is easily written to a jsonl file.
        """
        self._help_message = ""
        msg = self.sample()
        return {"message": msg, "annotations": self._annotations}
