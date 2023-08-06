"""Tests for cli_help_maker.cli functionalities. """

import pathlib

import pytest

from cli_help_maker import main

root = pathlib.Path(__file__).resolve().parent.parent.parent
dataset_path = root / "tests" / "data" / "dataset.yaml"


def test_read_config():
    conf = main.read_config(dataset_path)
    assert isinstance(conf, dict)
    assert len(conf.keys()) == 3
    keys = set(["version", "size", "arguments"])
    assert all([k in keys for k in conf.keys()])
    assert len(conf["arguments"]) == 34
    assert [
        callable(f) and f.__name__ == "<lambda>" for f in conf["arguments"].values()
    ]


def test_get_distribution():
    constant_dist = {"dist": "constant", "parameters": {"value": 1}}
    assert main.get_distribution(constant_dist)() == 1
    range_dist = {"dist": "set", "parameters": {"values": [2, 4]}}
    assert isinstance(main.get_distribution(range_dist)(), int)
    custom_dist = {"dist": "custom", "parameters": {"p": [0.2, 0.8], "values": [0, 1]}}
    assert isinstance(main.get_distribution(custom_dist)(), int)
    uniform_continuous_dist = {
        "dist": "uniform-continuous",
        "parameters": {"min": 0, "max": 1},
    }
    assert isinstance(main.get_distribution(uniform_continuous_dist)(), float)
    uniform_discrete_dist = {
        "dist": "uniform-discrete",
        "parameters": {"min": 0, "max": 10},
    }
    assert isinstance(main.get_distribution(uniform_discrete_dist)(), int)


@pytest.mark.parametrize(
    "a",
    [
        {},
        {"dist": "constant", "parameters": {"v": 1}},
        {"dist": "set", "parameters": {"v": 1}},
        {"dist": "uniform-discrete", "parameters": {"v": 1}},
        {"dist": "uniform-continuous", "parameters": {"v": 1}},
        {"dist": "custom", "parameters": {"v": 1}},
    ],
)
def test_get_distribution_errored(a):
    with pytest.raises(ValueError):
        assert main.get_distribution(a)() == 1


def test_argument_generator():
    conf = main.read_config(dataset_path)
    output = main.argument_generator(conf["size"], conf["arguments"])
    element = next(output)
    assert isinstance(element, dict)
    assert len(element) == 33
