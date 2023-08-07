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
from wmul_click_utils import RequiredIf
from wmul_test_utils import make_namedtuple


@pytest.fixture(scope="function")
def setup_required_if():
    @click.command()
    @click.option("--foo", type=str, cls=RequiredIf, required_if="bar", 
                  help="foo help")
    @click.option("--bar", type=str, cls=RequiredIf, required_if="foo", 
                  help="bar help")
    def cli(foo, bar):
        click.echo(f"foo={foo} bar={bar}")

    runner = CliRunner()

    return make_namedtuple(
        "setup_required_if",
        cli=cli,
        runner=runner
    )


def test_both_present(setup_required_if):
    result = setup_required_if.runner.invoke(
        setup_required_if.cli, 
        ["--foo", "foobaz", "--bar", "barbaz"]
    )

    assert not result.exception
    assert result.output == "foo=foobaz bar=barbaz\n"


def test_help(setup_required_if):
    result = setup_required_if.runner.invoke(
        setup_required_if.cli, 
        ["--help"]
    )

    assert "foo help" in result.output
    assert "bar help" in result.output
    

def test_foo_not_present(setup_required_if):
    result = setup_required_if.runner.invoke(
        setup_required_if.cli, 
        ["--bar", "barbaz"]
    )

    assert result.exception
    assert "Illegal usage: foo is required when bar is supplied." in \
        result.output

def test_bar_not_present(setup_required_if):
    result = setup_required_if.runner.invoke(
        setup_required_if.cli, 
        ["--foo", "foobaz"]
    )

    assert result.exception
    assert "Illegal usage: bar is required when foo is supplied." in \
        result.output


def test_neither_present(setup_required_if):
    result = setup_required_if.runner.invoke(
        setup_required_if.cli, 
        []
    )

    assert not result.exception
    assert result.output == "foo=None bar=None\n"