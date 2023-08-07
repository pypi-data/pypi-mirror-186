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
from wmul_click_utils import MXWith
from wmul_test_utils import make_namedtuple, \
    generate_true_false_matrix_from_list_of_strings


mx_with_two_params, mx_with_two_ids = \
    generate_true_false_matrix_from_list_of_strings(
        "mx_with_two",
        [
            "use_list"
        ]
    )

@pytest.fixture(scope="function", params=mx_with_two_params, 
                ids=mx_with_two_ids)
def setup_mx_with_two(request):
    params = request.param

    foo_mx_with = "bar"
    bar_mx_with = "foo"

    if params.use_list:
        foo_mx_with = [foo_mx_with]
        bar_mx_with = [bar_mx_with]

    @click.command()
    @click.option("--foo", type=str, cls=MXWith, mx_with=foo_mx_with, 
                  help="foo help")
    @click.option("--bar", type=str, cls=MXWith, mx_with=bar_mx_with, 
                  help="bar help")
    def cli(foo, bar):
        click.echo(f"foo={foo} bar={bar}")

    runner = CliRunner()

    return make_namedtuple(
        "setup_mx_with_two",
        cli=cli,
        runner=runner
    )


def test_both_present(setup_mx_with_two):
    result = setup_mx_with_two.runner.invoke(
        setup_mx_with_two.cli, 
        ["--foo", "foobaz", "--bar", "barbaz"]
    )

    assert result.exception
    assert "Illegal usage: 'foo' is mutually exclusive with 'bar'." in \
        result.output


def test_help(setup_mx_with_two):
    result = setup_mx_with_two.runner.invoke(
        setup_mx_with_two.cli, 
        ["--help"]
    )

    assert "foo help NOTE: This option is mutually exclusive with bar" in \
        result.output
    assert "bar help NOTE: This option is mutually exclusive with foo" in \
        result.output
    

def test_foo_not_present(setup_mx_with_two):
    result = setup_mx_with_two.runner.invoke(
        setup_mx_with_two.cli, 
        ["--bar", "barbaz"]
    )

    assert not result.exception
    assert "foo=None bar=barbaz" in result.output

def test_bar_not_present(setup_mx_with_two):
    result = setup_mx_with_two.runner.invoke(
        setup_mx_with_two.cli, 
        ["--foo", "foobaz"]
    )

    assert not result.exception
    assert "foo=foobaz bar=None" in result.output


def test_neither_present(setup_mx_with_two):
    result = setup_mx_with_two.runner.invoke(
        setup_mx_with_two.cli, 
        []
    )

    assert not result.exception
    assert result.output == "foo=None bar=None\n"
