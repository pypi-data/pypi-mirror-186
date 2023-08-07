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
from wmul_click_utils import RequiredUnless
from wmul_test_utils import make_namedtuple, \
    generate_true_false_matrix_from_list_of_strings


required_unless_params, required_unless_ids = \
    generate_true_false_matrix_from_list_of_strings(
        "required_unless",
        [
            "use_list"
        ]
    )

@pytest.fixture(scope="function", params=required_unless_params, 
                ids=required_unless_ids)
def setup_required_unless(request):
    params = request.param

    bar_req_unless = "foo"
    if params.use_list:
        bar_req_unless = [bar_req_unless]

    @click.command()
    @click.option("--foo", type=str, help="foo help")
    @click.option("--bar", type=str, cls=RequiredUnless, 
        required_unless=bar_req_unless, help="bar help")
    def cli(foo, bar):
        if foo:
            click.echo(f"foo={foo}")
        else:
            click.echo(f"bar={bar}")

    runner = CliRunner()

    return make_namedtuple(
        "setup_required_unless",
        cli=cli,
        runner=runner
    )


def test_both_present(setup_required_unless):
    result = setup_required_unless.runner.invoke(
        setup_required_unless.cli, 
        ["--foo", "foobaz", "--bar", "barbaz"]
    )

    assert not result.exception
    assert "foo=foobaz" in result.output


def test_help(setup_required_unless):
    result = setup_required_unless.runner.invoke(
        setup_required_unless.cli, 
        ["--help"]
    )

    assert "foo help" in result.output
    assert "bar help" in result.output
    

def test_foo_not_present(setup_required_unless):
    result = setup_required_unless.runner.invoke(
        setup_required_unless.cli, 
        ["--bar", "barbaz"]
    )

    assert not result.exception
    assert "bar=barbaz" in result.output


def test_bar_not_present(setup_required_unless):
    result = setup_required_unless.runner.invoke(
        setup_required_unless.cli, 
        ["--foo", "foobaz"]
    )

    assert "foo=foobaz" in result.output
    assert not result.exception


def test_neither_present(setup_required_unless):
    result = setup_required_unless.runner.invoke(
        setup_required_unless.cli, 
        []
    )

    assert result.exception
    assert "Illegal usage: bar is required unless one of 'foo' is supplied."


@pytest.fixture(scope="function", params=required_unless_params, 
                ids=required_unless_ids)
def setup_required_unless_both_required(request):
    params = request.param

    foo_req_unless = "bar"
    bar_req_unless = "foo"

    if params.use_list:
        foo_req_unless = [foo_req_unless]
        bar_req_unless = [bar_req_unless]

    @click.command()
    @click.option("--foo", type=str, cls=RequiredUnless, 
        required_unless=foo_req_unless, help="foo help")
    @click.option("--bar", type=str, cls=RequiredUnless, 
        required_unless=bar_req_unless, help="bar help")
    def cli(foo, bar):
        if foo:
            click.echo(f"foo={foo}")
        else:
            click.echo(f"bar={bar}")

    runner = CliRunner()

    return make_namedtuple(
        "setup_required_unless_both_required",
        cli=cli,
        runner=runner
    )


def test_both_present_both_required(setup_required_unless_both_required):
    result = setup_required_unless_both_required.runner.invoke(
        setup_required_unless_both_required.cli, 
        ["--foo", "foobaz", "--bar", "barbaz"]
    )

    assert not result.exception
    assert "foo=foobaz" in result.output


def test_help_both_required(setup_required_unless_both_required):
    result = setup_required_unless_both_required.runner.invoke(
        setup_required_unless_both_required.cli, 
        ["--help"]
    )

    assert "foo help" in result.output
    assert "bar help" in result.output
    

def test_foo_not_present_both_required(setup_required_unless_both_required):
    result = setup_required_unless_both_required.runner.invoke(
        setup_required_unless_both_required.cli, 
        ["--bar", "barbaz"]
    )

    assert not result.exception
    assert "bar=barbaz" in result.output


def test_bar_not_present_both_required(setup_required_unless_both_required):
    result = setup_required_unless_both_required.runner.invoke(
        setup_required_unless_both_required.cli, 
        ["--foo", "foobaz"]
    )

    assert "foo=foobaz" in result.output
    assert not result.exception


def test_neither_present_both_required(setup_required_unless_both_required):
    result = setup_required_unless_both_required.runner.invoke(
        setup_required_unless_both_required.cli, 
        []
    )

    assert result.exception
    assert "Illegal usage: bar is required unless one of 'foo' is supplied."


@pytest.fixture(scope="function")
def setup_required_unless_three_required():
    @click.command()
    @click.option("--foo", type=str, cls=RequiredUnless, 
        required_unless=["bar", "baz"], help="foo help")
    @click.option("--bar", type=str, cls=RequiredUnless, 
        required_unless=["foo", "baz"], help="bar help")
    @click.option("--baz", type=str, cls=RequiredUnless, 
        required_unless=["bar", "foo"], help="baz help")
    def cli(foo, bar, baz):
        if foo:
            click.echo(f"foo={foo}")
        elif bar:
            click.echo(f"bar={bar}")
        else:
            click.echo(f"baz={baz}")

    runner = CliRunner()

    return make_namedtuple(
        "setup_required_unless_three_required",
        cli=cli,
        runner=runner
    )


def test_help_three_required(setup_required_unless_three_required):
    result = setup_required_unless_three_required.runner.invoke(
        setup_required_unless_three_required.cli, 
        ["--help"]
    )

    assert "foo help" in result.output
    assert "bar help" in result.output
    assert "baz help" in result.output


# 000
def test_none_present_three_required(setup_required_unless_three_required):
    result = setup_required_unless_three_required.runner.invoke(
        setup_required_unless_three_required.cli, 
        []
    )

    assert result.exception
    assert ("Illegal usage: 'foo' is required unless one of 'baz, bar' is "
        "supplied." in result.output) or ("Illegal usage: 'foo' is required "
        "unless one of 'bar, baz' is supplied." in result.output)


# 001
def test_foo_bar_not_present_three_required(
        setup_required_unless_three_required
    ):
    result = setup_required_unless_three_required.runner.invoke(
        setup_required_unless_three_required.cli, 
        ["--baz", "bazbaz"]
    )

    assert not result.exception
    assert "baz=bazbaz" in result.output


# 010
def test_foo_baz_not_present_three_required(
        setup_required_unless_three_required
    ):
    result = setup_required_unless_three_required.runner.invoke(
        setup_required_unless_three_required.cli, 
        ["--bar", "barbaz"]
    )

    assert not result.exception
    assert "bar=barbaz" in result.output


# 011
def test_foo_not_present_three_required(setup_required_unless_three_required):
    result = setup_required_unless_three_required.runner.invoke(
        setup_required_unless_three_required.cli, 
        ["--bar", "barbaz", "--baz", "bazbaz"]
    )

    assert not result.exception
    assert "bar=barbaz" in result.output


# 100
def test_bar_baz_not_present_three_required(setup_required_unless_three_required):
    result = setup_required_unless_three_required.runner.invoke(
        setup_required_unless_three_required.cli, 
        ["--foo", "foobaz"]
    )

    assert "foo=foobaz" in result.output
    assert not result.exception


# 101
def test_bar_not_present_three_required(setup_required_unless_three_required):
    result = setup_required_unless_three_required.runner.invoke(
        setup_required_unless_three_required.cli, 
        ["--foo", "foobaz", "--baz", "bazbaz"]
    )

    assert not result.exception
    assert "foo=foobaz" in result.output


# 110
def test_baz_not_present_three_required(setup_required_unless_three_required):
    result = setup_required_unless_three_required.runner.invoke(
        setup_required_unless_three_required.cli, 
        ["--foo", "foobaz", "--bar", "barbaz"]
    )

    assert not result.exception
    assert "foo=foobaz" in result.output


# 111
def test_all_three_present_three_required(setup_required_unless_three_required):
    result = setup_required_unless_three_required.runner.invoke(
        setup_required_unless_three_required.cli, 
        ["--foo", "foobaz", "--bar", "barbaz", "--baz", "bazbaz"]
    )

    assert not result.exception
    assert "foo=foobaz" in result.output
