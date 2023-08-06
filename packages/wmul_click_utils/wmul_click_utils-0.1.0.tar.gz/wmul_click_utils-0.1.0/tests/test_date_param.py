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
from wmul_click_utils import DATE
from wmul_test_utils import make_namedtuple


@pytest.fixture(scope="function")
def setup_date():
    @click.command()
    @click.option("--foo", type=DATE, help="foo help")
    def cli(foo):
        click.echo(f"foo={foo.strftime('%Y-%m-%d')}")

    runner = CliRunner()

    return make_namedtuple(
        "setup_date",
        cli=cli,
        runner=runner
    )


def test_good_date(setup_date):
    result = setup_date.runner.invoke(
        setup_date.cli, 
        ["--foo", "2023-01-17"]
    )

    assert not result.exception
    assert "foo=2023-01-17" in result.output

def test_incomplete_date(setup_date):
    result = setup_date.runner.invoke(
        setup_date.cli, 
        ["--foo", "2023-01"]
    )

    assert result.exception
    assert "2023-01 is not a valid Date Type. It must be in the format "\
        "YYYY-MM-DD." in result.output


def test_gibberish_date(setup_date):
    result = setup_date.runner.invoke(
        setup_date.cli, 
        ["--foo", "Earth"]
    )

    assert result.exception
    assert "Earth is not a valid Date Type. It must be in the format "\
        "YYYY-MM-DD." in result.output
