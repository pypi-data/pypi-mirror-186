"""
@Author = 'Michael Stanley'

============ Change Log ============
01/17/2023 = Created

============ License ============
Copyright (C) 2023 Michael Stanley

This file is part of wmul_click_utils.

wmul_click_utils is free software: you can redistribute it and/or modify it 
under the terms of the GNU General Public License as published by the Free 
Software Foundation, either version 3 of the License, or (at your option) any 
later version.

wmul_click_utils is distributed in the hope that it will be useful, but WITHOUT 
ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS 
FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with 
wmul_click_utils. If not, see <https://www.gnu.org/licenses/>. 
"""
import click
import pytest
from click.testing import CliRunner
from wmul_click_utils import PAIRED
from wmul_test_utils import make_namedtuple


@pytest.fixture(scope="function")
def setup_paired():
    @click.command()
    @click.option("--foo", type=PAIRED, help="foo help")
    def cli(foo):
        click.echo(", ".join(foo))

    runner = CliRunner()

    return make_namedtuple(
        "setup_paired",
        cli=cli,
        runner=runner
    )


def test_two_given(setup_paired):
    result = setup_paired.runner.invoke(
        setup_paired.cli, 
        ["--foo", "foobaz barbaz"]
    )

    assert not result.exception
    assert "foobaz, barbaz" in result.output


def test_help(setup_paired):
    result = setup_paired.runner.invoke(
        setup_paired.cli, 
        ["--help"]
    )

    assert "foo help" in result.output


def test_only_one_given(setup_paired):
    result = setup_paired.runner.invoke(
        setup_paired.cli, 
        ["--foo", "barbaz"]
    )

    assert result.exception
    assert "barbaz is not a valid Paired Type. The number of space-separated " \
        "values must be even. E.G. '.wav .mp3' and '.wav .mp3 .doc .docx' " \
        "are valid, while '.wav .mp3 .ogg' is not." in result.output


def test_three_given(setup_paired):
    result = setup_paired.runner.invoke(
        setup_paired.cli, 
        ["--foo", "foobaz barbaz bazbaz"]
    )

    assert result.exception
    assert "foobaz barbaz bazbaz is not a valid Paired Type. The number of space-separated " \
        "values must be even. E.G. '.wav .mp3' and '.wav .mp3 .doc .docx' " \
        "are valid, while '.wav .mp3 .ogg' is not." in result.output


def test_four_given(setup_paired):
    result = setup_paired.runner.invoke(
        setup_paired.cli, 
        ["--foo", "foobaz barbaz bazbaz foofoo"]
    )

    assert not result.exception
    assert "foobaz, barbaz, bazbaz, foofoo" in result.output
