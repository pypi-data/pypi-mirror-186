"""Tests for the expected data from calling the command line programs.

To see all the prints:
pytest -s -v tests/integration

"""

import pathlib
import subprocess
import tempfile
from collections import Counter

import srsly
from typer.testing import CliRunner

from cli_help_maker import utils
from cli_help_maker.main import app

root = pathlib.Path(__file__).resolve().parent.parent.parent
dataset_path = root / "dataset.yaml"

runner = CliRunner()


def test_main():
    with tempfile.TemporaryDirectory() as tmpdir:
        tmpdir = pathlib.Path(tmpdir)
        input_path = root / "tests" / "data" / "dataset.yaml"
        output_path = root / "tests" / "data" / tmpdir

        # subprocess.run(["cli-help-maker", str(input_path), str(output_path)], capture_output=True)
        # Written to capture the print messages while testing
        subprocess.run(
            ["cli-help-maker", str(input_path), str(output_path)], stdout=True
        )
        # result = runner.invoke(app, [str(input_path), str(output_path)])
        arguments = tmpdir / "arguments.jsonl"
        dataset = tmpdir / "dataset.jsonl"
        assert arguments.is_file()
        assert dataset.is_file()
        args = list(srsly.read_jsonl(arguments))
        assert len(args) == 100
        data = list(srsly.read_jsonl(dataset))

        # Every dataset generated should have annotations inside the message,
        # otherwise there are labels that were annotated but weren't written
        # to the final message
        for i, line in enumerate(data):
            message, annotations = line["message"], line["annotations"]
            print("**" * 10)
            utils.highlight_message(line)
            print("**" * 10)

            if len(Counter([tuple(a) for a in annotations])) != len(annotations):
                utils.highlight_message(line)
                print("annotations", annotations)
                assert False, "There are repeated labels"

            if len(message) <= annotations[-1][-1]:
                utils.highlight_message(line)
                print("annotations", annotations)
                assert False, "A message has an annotation out of the content"

        # TODO: Add test to check the labels are not overlapping
