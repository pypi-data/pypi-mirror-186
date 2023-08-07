"""
@Author = 'Michael Stanley'

These are utilities for use with Python's Click cli library.

MXWith based upon https://stackoverflow.com/a/44349292/521402 
and https://stackoverflow.com/a/51235564/521402

============ Change Log ============
01/19/2023 = Modify MXWith and RequiredUnless to accept either a string for a 
             single other option, or a list of other options.

01/18/2023 = Added RequiredUnless

01/17/2023 = Extracted to separate package.

============ License ============
Copyright (C) 2020-2023 Michael Stanley

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
__version__ = "0.1.1"
import click
from datetime import datetime

class RequiredIf(click.Option):
    def __init__(self, *args, **kwargs):
        self.required_if = kwargs.pop('required_if')
        assert self.required_if, "'required_if' parameter required"
        kwargs['help'] = f"{kwargs.get('help', '')} NOTE: This argument is " \
                         f"required if {self.required_if} is supplied.".strip()
        super(RequiredIf, self).__init__(*args, **kwargs)

    def handle_parse_result(self, ctx, opts, args):
        we_are_present = self.name in opts
        other_present = self.required_if in opts

        if other_present:
            if not we_are_present:
                raise click.UsageError(
                    f"Illegal usage: {self.name} is required when "
                    f"{self.required_if} is supplied."
                )
            else:
                self.prompt = None

        return super(RequiredIf, self).handle_parse_result(ctx, opts, args)


class RequiredUnless(click.Option):
    def __init__(self, *args, **kwargs):
        req_unless = kwargs.pop('required_unless')
        if isinstance(req_unless, str):
            req_unless = { req_unless }
        else:
            req_unless = set(req_unless)
        self.required_unless = req_unless
        assert self.required_unless, "'required_unless' parameter required"

        kwargs_help = kwargs.get('help', '')
        req_unless_keys = ", ".join(self.required_unless)
        req_unless_help = " NOTE: This option is required unless "\
                          f"one of {req_unless_keys} is supplied."
        kwargs['help'] = f"{kwargs_help}{req_unless_help}".strip()

        super(RequiredUnless, self).__init__(*args, **kwargs)

    def handle_parse_result(self, ctx, opts, args):
        current_opt = self.name in opts

        if not current_opt:
            if self.required_unless.isdisjoint(opts):
                raise click.UsageError(
                    f"Illegal usage: '{self.name}' is required unless "
                    f"one of '{', '.join(self.required_unless)}' is "
                        "supplied."
                )
            else:
                self.prompt = None

        return super(RequiredUnless, self).handle_parse_result(ctx, opts, args)


class MXWith(click.Option):
    def __init__(self, *args, **kwargs):
        mx_with = kwargs.pop('mx_with')
        if isinstance(mx_with, str):
            mx_with = [mx_with]
        self.mx_with = mx_with
        assert self.mx_with, "'mx_with' parameter required"

        kwargs_help = kwargs.get('help', '')
        other_mx_keys = ", ".join(self.mx_with)
        mx_help = f" NOTE: This option is mutually exclusive with {other_mx_keys}"
        kwargs['help'] = f"{kwargs_help}{mx_help}".strip()

        super(MXWith, self).__init__(*args, **kwargs)

    def handle_parse_result(self, ctx, opts, args):
        current_opt = self.name in opts

        for mx_opt in self.mx_with:
            if mx_opt in opts:
                if current_opt:
                    raise click.UsageError(
                        f"Illegal usage: '{self.name}' is mutually exclusive "
                        f"with '{mx_opt}'." 
                    )
                else:
                    self.prompt = None

        return super(MXWith, self).handle_parse_result(ctx, opts, args)


class PairedParamType(click.ParamType):
    name = "Paired Type"

    def convert(self, value, param, ctx):
        value_casefold = value.casefold()
        value_list = value_casefold.split()
        number_of_values = len(value_list)
        if number_of_values % 2 == 0:
            return value_list
        else:
            self.fail(
                f"{value} is not a valid Paired Type. The number of "
                 "space-separated values must be even. E.G. '.wav .mp3' and "
                 "'.wav .mp3 .doc .docx' are valid, while '.wav .mp3 .ogg' is "
                 "not.", 
                 param, 
                 ctx
            )

PAIRED = PairedParamType()


class DateParamType(click.ParamType):
    name = "Date Type"

    def convert(self, value, param, ctx):
        try:
            return datetime.strptime(value, "%Y-%m-%d").date()
        except ValueError:
            self.fail(
                f"{value} is not a valid Date Type. It must be in the format "\
                "YYYY-MM-DD.",
                param,
                ctx
            )

DATE = DateParamType()