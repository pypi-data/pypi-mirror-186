"""Tests for utility functions. """

import random

import pytest

import cli_help_maker.utils as ut

FIXED_SEED = 6798


def test_get_word():
    assert isinstance(ut.get_word(), str)


@pytest.mark.parametrize("p,expected", [(1, "Hello"), (0, "hello")])
def test_capitalize(p, expected):
    assert ut.capitalize("hello", probability=p) == expected


@pytest.mark.parametrize(
    "capitalized, upper, expected",
    [
        (False, False, "usage: "),
        (True, False, "Usage: "),
        (True, True, "Usage: "),
        (False, True, "USAGE: "),
    ],
)
def test_usage_pattern(capitalized, upper, expected):
    assert ut.usage_pattern(capitalized=capitalized, upper=upper) == expected


@pytest.mark.parametrize(
    "section, capitalized, expected",
    [("options", False, "options:"), ("options", True, "Options:"), (None, True, "")],
)
def test_section_pattern(section, capitalized, expected):
    if section is None:
        assert isinstance(
            ut.section_pattern(section=section, capitalized=capitalized), str
        )
    else:
        assert ut.section_pattern(section=section, capitalized=capitalized) == expected


@pytest.mark.parametrize(
    "c, p, expected",
    [("arg", 0, "arg"), ("arg", 1, "[arg]")],
)
def test_maybe_do_optional(c, p, expected):
    assert ut.maybe_do_optional(content=c, probability=p) == expected


@pytest.mark.parametrize(
    "c, p, expected",
    [("arg", 0, "arg"), ("arg", 1, "(arg)")],
)
def test_maybe_do_required(c, p, expected):
    assert ut.maybe_do_required(content=c, probability=p) == expected


@pytest.mark.parametrize(
    "c, expected",
    [(["arg"], "arg"), (["arg1", "arg2"], "arg1 | arg2"), ([""], "")],
)
def test_do_mutually_exclusive(c, expected):
    assert ut.do_mutually_exclusive(c) == expected


@pytest.mark.parametrize(
    "e, p, g, op, expected",
    [
        (["v1"], 0, [2], 0, ["v1"]),
        (["v1", "v2"], 0, [2], 0, ["v1", "v2"]),
        (["v1", "v2"], 1, [2], 0, ["(v1 | v2)"]),
        (["v1", "v2"], 1, [2], 1, ["[v1 | v2]"]),
        (["v1", "v2", "v3"], 1, [2], 0, ["(v1 | v2)", "v3"]),
        (["v1", "v2", "v3"], 0, [2], 0, ["v1", "v2", "v3"]),
    ],
)
def testdo_mutually_exclusive_groups(e, p, g, op, expected):
    assert (
        ut.do_mutually_exclusive_groups(
            e, probability=p, groups=g, optional_probability=op
        )
        == expected
    )


@pytest.mark.parametrize(
    "cp, ac, expected",
    [(0, False, "[options]"), (1, False, "[Options]"), (0, True, "[OPTIONS]")],
)
def test_options_shortcut(cp, ac, expected):
    assert ut.options_shortcut(capitalized_probability=cp, all_caps=ac) == expected


@pytest.mark.parametrize(
    "cp, s, an, expected",
    [
        (0, "between_brackets", False, "<areel-spaniellike>"),
        (1, "between_brackets", False, "<Areel-spaniellike>"),
        (0, "between_brackets", True, "<areel-spaniellike>..."),
        (0, "all_caps", False, "AREEL-SPANIELLIKE"),
        (0, "all_caps", True, "AREEL-SPANIELLIKE..."),
        (0, "undefined", True, "<areel-spaniellike>..."),
    ],
)
def test_make_argument(cp, s, an, expected):
    random.seed(FIXED_SEED)
    assert ut.make_argument(capitalized_prob=cp, style=s, any_number=an) == expected


make_options_args = []


@pytest.mark.parametrize(
    "s, l, wv, scp, lcp, ss, ls, sls, pnc, pvc, st, an, expected",
    [
        (
            True,
            True,
            False,
            0,
            0,
            " ",
            "=",
            ", ",
            0,
            0,
            "between_brackets",
            False,
            "-a, --areel-spaniellike",
        ),
        (
            True,
            False,
            False,
            0,
            0,
            " ",
            "=",
            ", ",
            0,
            0,
            "between_brackets",
            False,
            "-a",
        ),
        (
            True,
            True,
            True,
            0,
            0,
            " ",
            "=",
            ", ",
            0,
            0,
            "between_brackets",
            False,
            "-a <pterobranchia>",
        ),
        # (False, False, False, 0, 0, " ", "=", ", ", 0, 0, "between_brackets", False, "-a, --areel-spaniellike"),  # returns ''
        # (False, False, True, 0, 0, " ", "=", ", ", 0, 0, "between_brackets", False, "-a, --areel-spaniellike"),  # returns ''
        (
            True,
            True,
            False,
            1,
            0,
            " ",
            "=",
            ", ",
            0,
            0,
            "between_brackets",
            False,
            "-A, --areel-spaniellike",
        ),
        (
            True,
            True,
            False,
            0,
            1,
            " ",
            "=",
            ", ",
            0,
            0,
            "between_brackets",
            False,
            "-a, --Areel-spaniellike",
        ),
        (
            True,
            True,
            False,
            1,
            1,
            " ",
            "=",
            ", ",
            0,
            0,
            "between_brackets",
            False,
            "-A, --Areel-spaniellike",
        ),
        (
            True,
            True,
            False,
            0,
            0,
            " ",
            "=",
            ", ",
            0,
            1,
            "between_brackets",
            False,
            "-a, --areel-spaniellike",
        ),  # repeated with previous
        (
            True,
            True,
            False,
            0,
            0,
            " ",
            "=",
            ", ",
            1,
            0,
            "between_brackets",
            False,
            "-A, --Areel-spaniellike",
        ),  # repeated with previous
        (
            True,
            True,
            False,
            0,
            0,
            " ",
            "=",
            ", ",
            1,
            1,
            "between_brackets",
            False,
            "-A, --Areel-spaniellike",
        ),
        (
            True,
            True,
            False,
            0,
            0,
            " ",
            " ",
            ", ",
            0,
            0,
            "between_brackets",
            False,
            "-a, --areel-spaniellike",
        ),
        (
            True,
            True,
            True,
            0,
            0,
            " ",
            "=",
            ", ",
            0,
            0,
            "all_caps",
            False,
            "-a PTEROBRANCHIA",
        ),
        (
            True,
            True,
            True,
            0,
            0,
            " ",
            "=",
            ", ",
            0,
            0,
            "all_caps",
            True,
            "-a PTEROBRANCHIA...",
        ),
        (
            False,
            True,
            True,
            0,
            0,
            " ",
            "=",
            ", ",
            0,
            0,
            "all_caps",
            True,
            "--areel-spaniellike=PTEROBRANCHIA...",
        ),
    ],
)
def test_make_option(s, l, wv, scp, lcp, ss, ls, sls, pnc, pvc, st, an, expected):
    random.seed(FIXED_SEED)
    assert (
        ut.make_option(
            short=s,
            long=l,
            with_value=wv,
            short_capitalized_prob=scp,
            long_capitalized_prob=lcp,
            short_separator=ss,
            long_separator=ls,
            short_long_separator=sls,
            probability_name_cap=pnc,
            probability_value_cap=pvc,
            style=st,
            any_number=an,
        )
        == expected
    )


@pytest.mark.parametrize(
    "e, n, expected",
    [
        (0, False, ("-", 1)),
        (1, False, ("-", 2)),
        (2, False, ("-", 3)),
        (2, True, ("-", 1)),
    ],
)
def test_make_list(e, n, expected):
    assert len(ut.make_list(elements=e, numbered=n).split(expected[0])) == expected[1]
