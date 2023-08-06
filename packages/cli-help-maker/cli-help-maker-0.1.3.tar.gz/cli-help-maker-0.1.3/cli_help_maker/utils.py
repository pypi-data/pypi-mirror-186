"""Helper functions to allow generating different parts of
a help message and more.
"""

import random
from itertools import accumulate
from warnings import warn

from rich.console import Console
from rich.text import Text

try:
    from nltk.corpus import words

    word_list = words.words()

except ModuleNotFoundError:  # pragma: no cover
    import textwrap

    msg = textwrap.dedent(
        """
        To generate words for the command arguments, and options
        you need the nltk's `words` dataset, otherwise `get_word`
        function will fail.
 
        Please use the NLTK Downloader to obtain the resource:

        >>> import nltk
        >>> nltk.download('words')
        """
    )
    warn(msg)


# A bool to change between text generated from letter frequencies
# or selected from the nltk corpus. If True, uses statistics
TEXT_FROM_STATISTICS = False


def get_word() -> str:
    """Selects a word from the wordlist corpora defined in:
    https://www.nltk.org/book/ch02.html#code-unusual
    """
    return word_list[random.randint(0, len(word_list))].lower()


# Letter frequency, obtained from the following link with the "script":
# https://www3.nd.edu/~busiforc/handouts/cryptography/letterfrequencies.html
# import requests
# from bs4 import BeautifulSoup
# req = requests.get(r"https://www3.nd.edu/~busiforc/handouts/cryptography/letterfrequencies.html")
# soup = BeautifulSoup(req.content, "html.parser")
# table = soup.find_all("table")[-1].find_all("tr")
# letters = []
# freqs = []
# for row in table:
#     cols = [c for c in row.find_all("td")]
#     letters.append(cols[0].text)
#     letters.append(cols[3].text)
#     freqs.append(float(cols[1].text.replace("%", "")))
#     freqs.append(float(cols[4].text.replace("%", "")))

cap_letters = [
    "E",
    "M",
    "A",
    "H",
    "R",
    "G",
    "I",
    "B",
    "O",
    "F",
    "T",
    "Y",
    "N",
    "W",
    "S",
    "K",
    "L",
    "V",
    "C",
    "X",
    "U",
    "Z",
    "D",
    "J",
    "P",
    "Q",
]
LETTERS = [l.lower() for l in cap_letters]
LETTER_FREQUENCIES = [
    11.1607,
    3.0129,
    8.4966,
    3.0034,
    7.5809,
    2.4705,
    7.5448,
    2.072,
    7.1635,
    1.8121,
    6.9509,
    1.7779,
    6.6544,
    1.2899,
    5.7351,
    1.1016,
    5.4893,
    1.0074,
    4.5388,
    0.2902,
    3.6308,
    0.2722,
    3.3844,
    0.1965,
    3.1671,
    0.1962,
]

# Idea for the word length from:
# https://math.wvu.edu/~hdiamond/Math222F17/Sigurd_et_al-2004-Studia_Linguistica.pdf
# Function for probability of a word of length x (in letters).
# -> f = lambda x: 11.74 * (x ** 3) * (0.4 ** x)
f = lambda x: 11.74 * (x**3) * (0.4**x)
_word_length_probs = list(accumulate([f(x) for x in range(1, 30)]))
# Adjust the values to be in the range [0, 1], and remove those which are over 100.
WORD_LENGTH_PROBABILITIES = [i for i in _word_length_probs if i < 100] + [100]

g = lambda x: 1.1 * x * 0.9**x
_sentence_length_probs = list(accumulate([f(x) for x in range(1, 80)]))
SENTENCE_LENGTH_PROBABILITIES = [i for i in _sentence_length_probs if i < 100] + [100]


argument_styles = {
    "between_brackets": lambda w: f"<{w}>",
    "all_caps": lambda w: w.upper(),
}


def capitalize(content: str, probability: float = 0.5) -> str:
    """Capitalizes a string string with a given probability."""
    if random.random() > 1 - probability:
        return content.capitalize()
    return content


def usage_pattern(capitalized: bool = True, upper: bool = False) -> str:
    usage = "usage: "
    if capitalized:
        return usage.capitalize()
    if upper:
        return usage.upper()
    return usage


def section_pattern(section: str | None = "options", capitalized: bool = True) -> str:
    """Creates a section header.

    In general, the possible sections are `Arguments` or `Options`,
    but for example git has personalized headers on their sections.

    Args:
        section (str or None, optional): _description_. Defaults to 2.
        capitalized (float, optional): _description_. Defaults to 0.

    """
    if not section:
        section = make_word() + ":"
    else:
        section += ":"

    if capitalized:
        return section.capitalize()

    return section


def do_optional(content: str) -> str:
    """From http://docopt.org/

    Elements (options, arguments, commands) enclosed with square brackets
    "[ ]" are marked to be optional.

    Args:
        content (str): _description_

    Returns:
        str: _description_
    """
    return f"[{content}]"


def maybe_do_optional(content: str, probability: float = 0.5) -> str:
    """Calls `do_optional` with a probability given.

    Args:
        content (str): content as passed to `do_optional`
        probability (float, optional): _description_. Defaults to 0.5.

    Returns:
        str: _description_
    """
    if random.random() > (1 - probability):
        return do_optional(content)
    return content


def do_required(content: str) -> str:
    """From http://docopt.org/

    All elements are required by default, if not included in brackets "[ ]".
    However, sometimes it is necessary to mark elements as required explicitly
    with parens "( )".

    Args:
        content (str): _description_

    Returns:
        str: _description_
    """
    return f"({content})"


def maybe_do_required(content: str, probability: float = 0.5) -> str:
    """Equivalent to `maybe_do_optional` with `do_required`."""
    if random.random() > (1 - probability):
        return do_required(content)
    return content


def do_mutually_exclusive(content: list[str]) -> str:
    """Joins multiple options via pipes to create mutually exlusive
    elements.

    Args:
        content (list[str]): list of elements to join.

    Returns:
        str: _description_

    Note:
        Visit [docopt](https://github.com/jazzband/docopt-ng) pipe docs.
    """
    return " | ".join(content)


def do_mutually_exclusive_groups(
    elements: list[str],
    probability: float = 0.5,
    groups: list[int] = [0, 2],
    optional_probability: float = 0.5,
) -> list[str]:
    """Creates groups of mutually exclusive elements

    Args:
        elements (list[str]): Content for the groups, should be the list of options
            generated for a program.
        probability (float, optional): Probability of creating a group. Defaults to 0.5.
        groups (list[int], optional): Size of the groups. Defaults to [0, 2].
        optional_probability (float): probability of the group being optional.
            Otherwise it will be required.

    Returns:
        list[str]: _description_

    Note:
        The algorithm may benefit from some speed up, but
        is ok for the moment.
    """
    if len(elements) < 2:
        # The groups only have sense if there are 2 or more.
        return elements

    new_elements = []
    to_group = []
    group_size = random.choice(groups)
    for e in elements:
        to_group.append(e)
        if (
            len(to_group) == group_size
        ):  # Start with a simple option, later will use `groups`

            if random.random() > (1 - probability):
                to_group = do_mutually_exclusive(to_group)
                if random.random() > (1 - optional_probability):
                    to_group = do_optional(to_group)
                else:
                    to_group = do_required(to_group)
                new_elements.append(to_group)

            else:
                new_elements.extend(to_group)

            to_group = []
            # Restart the group size to allow taking a range of possibilities
            group_size = random.choice(groups)

    # Take care of the last options which didn't fit into a group
    # to avoid losing them
    if len(to_group) > 0:
        new_elements.extend(to_group)

    return new_elements


def options_shortcut(
    capitalized_probability: float = 0.0, all_caps: bool = False
) -> str:
    """Returns the shortcut for any options.

    Args:
        capitalized_probability (float, optional): Probability of returning
            the first capital letter. Defaults to 0.
        all_caps (bool, optional): If True, all the letters are in uppercase.
            For example, click uses this option. Defaults to False.

    Returns:
        str: [options] section.

    Note:
        https://github.com/jazzband/docopt-ng
    """
    options = capitalize("options", probability=capitalized_probability)
    shortcut = f"[{options}]"
    if all_caps:
        return shortcut.upper()
    return shortcut


def word_length() -> int:
    """Generates the number of letters in a word using a more
    appropriate probability distribution than uniform.

    Returns:
        int: number of letters in a word.
    """
    return random.choices(
        range(1, len(WORD_LENGTH_PROBABILITIES) + 1),
        cum_weights=WORD_LENGTH_PROBABILITIES,
    )[0]


def sentence_length() -> int:
    """Like word length but for sentences.

    Returns:
        int: number of words in a sentence.
    """
    return random.choices(
        range(1, len(SENTENCE_LENGTH_PROBABILITIES) + 1),
        cum_weights=SENTENCE_LENGTH_PROBABILITIES,
    )[0]


def paragraph_length() -> int:
    # The number of sentences per paragraph is totally made up.
    return random.choices(
        range(1, 7),
        weights=[10.0, 25.0, 30.0, 20.0, 10.0, 5.0],
    )[0]


def make_word() -> str:
    """Creates a random word from made up letters. The letters
    are obtained from observed frequencies.

    Note:
        See https://math.wvu.edu/~hdiamond/Math222F17/Sigurd_et_al-2004-Studia_Linguistica.pdf
    """
    return "".join(random.choices(LETTERS, weights=LETTER_FREQUENCIES, k=word_length()))


def make_sentence(use_statistics: bool = TEXT_FROM_STATISTICS) -> str:
    """Creates a sentence.

    Args:
        use_statistics (bool, optional):
            If set to True uses the statistical way, otherwise uses nltk corpus.
            Defaults to TEXT_FROM_STATISTICS.

    Returns:
        str: made up sentence to fill the messages with content.
    """
    gen = make_word if use_statistics else get_word
    return capitalize(
        " ".join([gen() for _ in range(sentence_length())]), probability=1
    )


def make_paragraph(use_statistics: bool = TEXT_FROM_STATISTICS) -> str:
    """Creates a paragraph, in a similar way as `make_sentence`.

    Args:
        use_statistics (bool, optional):
            If set to True uses the statistical way, otherwise uses nltk corpus.
            Defaults to TEXT_FROM_STATISTICS.

    Returns:
        str: made up sentence to fill the messages with content.
    """
    return (
        ". ".join(
            [
                make_sentence(use_statistics=use_statistics)
                for _ in range(paragraph_length())
            ]
        )[:-1]
        + "."
    )


def make_list(elements: int = 2, numbered: bool = False) -> str:
    """Creates a list of elements.

    Args:
        elements (int, optional):
            Number of elements in the list. Defaults to 2.
        numbered (bool, optional):
            Whether the list is numbered or not. Defaults to False. 

    Notes:
        It can creates list as in markdown.
        Each element would be a sentence. Helper function to create descriptions of
        a program behavior, i.e.

            Usage:   
            pip install [options] <requirement specifier> [package-index-options] ...
            pip install [options] -r <requirements file> [package-index-options] ...
            pip install [options] [-e] <vcs project url> ...
            pip install [options] [-e] <local project path> ...
            pip install [options] <archive url/path> ...

            Description:
            Install packages from:
            
            - PyPI (and other indexes) using requirement specifiers.
            - VCS project urls.
            - Local project directories.
            - Local or remote source archives.
            
            pip also supports installing from "requirements files", which provide
            an easy way to specify a whole environment to be installed.
    """
    content = []
    for i in range(elements):
        if numbered:
            content.append(f"{i + 1}. {make_sentence()}")
        else:
            content.append(f"- {make_sentence()}")

    return "\n".join(content)


def make_composed_word() -> str:
    """Generator of composed words for arguments, with
    made-up probabilities."""
    return "-".join(
        [
            get_word()
            for _ in range(
                random.choices(
                    population=range(1, 5), cum_weights=[0.6, 0.95, 0.99, 1]
                )[0]
            )
        ]
    )


def make_argument(
    capitalized_prob: float = 0.01,
    style: str = "between_brackets",
    any_number: bool = False,
) -> str:
    """Currently equivalent to a name, wrapped in <_>."""
    styler = argument_styles.get(style)
    if styler is None:
        warn(f"style not defined: {style}, set by default: 'between_brackets'")
        styler = argument_styles["between_brackets"]

    arg = styler(capitalize(make_composed_word(), probability=capitalized_prob))

    if any_number:
        arg += "..."

    return arg


def make_option(
    short: bool = True,
    long: bool = True,
    with_value: bool = False,
    short_capitalized_prob: float = 0.1,
    long_capitalized_prob: float = 0,
    short_separator: str = " ",
    long_separator: str = "=",
    short_long_separator: str = ", ",
    probability_name_cap: float = 0,
    probability_value_cap: float = 0,
    style: str = "between_brackets",
    any_number: bool = False,
):
    """Optional argument generator.

    If short, long and with_value are True, only the short option will be
    generated and returned.

    TODO:
        Possibilities not developed yet:
        - Multiple possibilities: [-p | --paginate | -P | --no-pager]

    Args:
        short (bool, optional):
            Add a short version (single dashed). Defaults to True.
        long (bool, optional):
            Add a long version (double dashed). Defaults to True.
        with_value (bool, optional):
            Add a default value for the . Defaults to False.
        short_capitalized_prob (float, optional):
            Probability of having the argument capitalized. Defaults to 0.1.
        long_capitalized_prob (float, optional):
            Equivalent to short_capitalized_prob for long option. Defaults to 0.
        short_separator (str, optional):
            Separator for the default value in the short option. Defaults to " ".
        long_separator (str, optional):
            Separator for the default value in the long option. Defaults to "=".
        short_long_separator (str, optional):
            Separator between both versions of an argument, i.e.
            -o, --option. The usual values are ", " or " ". Defaults to ",".
        probability_name_cap (float, optional):
            Probability of the name of the option being capitalized. Defaults to 0.
        probability_value_cap (float, optional)
            Probability of the default value of the option being capitalized.
            Defaults to 0.
        style (str, optional). Argument passed to make_argument, only applies to
            a value for the option.
        any_number (bool, optional). Argument passed to make_argument.
    """
    option = ""
    name = capitalize(make_composed_word(), probability=probability_name_cap)

    # The following block is not covered just to avoid mocking the name
    if len(name) == 1:  # pragma: no cover
        # In case the name generated has only one letter,
        # force it to be only a short option.
        short = True
        long = False

    value = make_argument(
        capitalized_prob=probability_value_cap, style=style, any_number=any_number
    )
    if short:
        option += "-" + capitalize(name[0], short_capitalized_prob)
        if with_value:
            option += short_separator + value
            return option

    if long:
        if short:
            option += short_long_separator
        option += "--" + capitalize(name, long_capitalized_prob)
        if with_value:
            option += long_separator + value
            return option

    if option == "":
        # In case it wasn't properly generated, return as default a single letter
        return "-" + name[0]

    return option


# Function not covered. It uses rich under the hood, works as long as
# the annotations are properly generated. Maybe will get back to this
# function in the future.
def highlight_message(
    annotations: dict[str, str | tuple[str, int, int]]
) -> None:  # pragma: no cover
    """Helper function to print a message with the different labels visualized
    in the console.

    Args:
        annotations (str): The output obtained from HelpGenerator.annotations
    """
    console = Console()

    msg = annotations["message"]
    text = Text(msg)
    labels = annotations["annotations"]
    for label, start, end in labels:
        if label == "CMD":
            text.stylize("underline light_salmon1", start, end)
        elif label == "ARG":
            text.stylize("underline slate_blue1", start, end)
        elif label == "OPT":
            text.stylize("underline spring_green3", start, end)

    console.print(text)
