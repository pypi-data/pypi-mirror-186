"""
SPDX-FileCopyrightText: 2022-2023. Thomas Mahe <contact@tmahe.dev>
SPDX-License-Identifier: MIT

This work is licensed under the terms of the MIT license.
For a copy, see <https://opensource.org/licenses/MIT>.
"""

import argparse
import inspect
import os
import sys
import textwrap
import typing

from .command import Command
from .helpers import get_command_description, get_filtered_args


class VolunorHelpFormatter(argparse.RawTextHelpFormatter):

    def __init__(self, prog: str):
        super().__init__(prog, width=80, max_help_position=35)

    def _format_action(self, action):
        if type(action) == argparse._SubParsersAction:
            # inject new class variable for subcommand formatting
            subactions = action._get_subactions()
            invocations = [self._format_action_invocation(a) for a in subactions]
            self._subcommand_max_length = max(len(i) for i in invocations)

        if type(action) == argparse._SubParsersAction._ChoicesPseudoAction:
            # format subcommand help line
            subcommand = self._format_action_invocation(action)  # type: str
            width = self._subcommand_max_length
            help_text = ""
            if action.help:
                help_text = self._expand_help(action)

            if len(help_text) > 0:
                first_section = "  {} {} ".format(subcommand, "." * (width + 4 - len(subcommand)))
                return "{}{}\n".format(first_section,
                                       textwrap.shorten(help_text, width=80 - len(first_section), placeholder="..."),
                                       width=width)
            else:
                return "  {}\n".format(subcommand, width=width)

        elif type(action) == argparse._SubParsersAction:
            # process subcommand help section
            msg = ''
            for subaction in action._get_subactions():
                msg += self._format_action(subaction)
            return msg
        else:
            return super(VolunorHelpFormatter, self)._format_action(action)

    def _format_action_invocation(self, action: argparse.Action):
        if not action.option_strings:
            metavar, = self._metavar_formatter(action, action.dest)(1)
            return metavar
        else:
            parts = []
            if action.nargs == 0:
                parts.extend(action.option_strings)
            else:
                default = action.dest.upper()
                args_string = self._format_args(action, default)
                for option_string in action.option_strings:
                    parts.append('%s' % option_string)
                parts[-1] += ' %s' % args_string
            return ', '.join(parts)


class Cli(object):
    _cli: argparse.ArgumentParser = None

    def __init__(self, descriptor, prog=os.path.basename(sys.argv[0])):
        self._descriptor = descriptor
        self._parser = argparse.ArgumentParser(prog=prog, add_help=False, formatter_class=VolunorHelpFormatter)
        self._optional_args = self._parser.add_argument_group("optional arguments")
        self._optional_args.add_argument("-h", "--help", action="help", help="show this help message and exit")
        self._parser.add_argument('--_VOLUNOR_CURRENT_PARSER', required=False, default=self._parser,
                                  help=argparse.SUPPRESS)

        if isinstance(descriptor, typing.Dict):
            self._cli = self._from_dict(self._parser, descriptor)

        if issubclass(type(descriptor), Command.__class__):
            self._cli = self._from_dict(self._parser, descriptor)

    def _from_dict(self, parser: argparse.ArgumentParser, descriptor=None, level=0):
        if issubclass(type(descriptor), Command.__class__):
            parser.description = get_command_description(descriptor)
            parser.add_argument('--_VOLUNOR_CALLABLE_COMMAND', required=False, default=descriptor,
                                help=argparse.SUPPRESS)

            required_args = parser.add_argument_group("required arguments")
            optional_args = parser.add_argument_group("optional arguments")
            descriptor.volunor_args(descriptor, required_args, optional_args)

        elif callable(descriptor) and descriptor.__name__ == "<lambda>":
            parser.description = get_command_description(descriptor)
            parser.add_argument('--_VOLUNOR_CALLABLE_COMMAND', required=False, default=descriptor,
                                help=argparse.SUPPRESS)

            required_args = parser.add_argument_group("required arguments")
            optional_args = parser.add_argument_group("optional arguments")

            for param, e in inspect.signature(descriptor).parameters.items():
                if e.default is not inspect._empty:
                    optional_args.add_argument('--' + param, type=type(e.default), default=e.default,
                                               metavar=str(type(e.default)).upper()[8:-2],
                                               help=f'lambda parameter (default: {e.default})')
                else:
                    required_args.add_argument(param, help=f"lambda parameter (str)")

        if isinstance(descriptor, typing.Dict) and descriptor.keys().__len__() > 0:
            sub_parser = parser.add_subparsers(title="commands", metavar="COMMAND")

            for key, item in descriptor.items():
                command_sub_parser = sub_parser.add_parser(name=key,
                                                           help=get_command_description(item, single_line=True),
                                                           formatter_class=VolunorHelpFormatter, add_help=False)
                _optional_args = command_sub_parser.add_argument_group("optional arguments")
                _optional_args.add_argument("-h", "--help", action="help", help="show this help message and exit")
                command_sub_parser.add_argument('--_VOLUNOR_CURRENT_PARSER', required=False, default=command_sub_parser,
                                                help=argparse.SUPPRESS)
                self._from_dict(command_sub_parser, item, level + 1)

        return parser

    def big_gang(self):
        args = self._cli.parse_args()
        if hasattr(args, "_VOLUNOR_CALLABLE_COMMAND"):
            if issubclass(type(args._VOLUNOR_CALLABLE_COMMAND), Command.__class__):
                args._VOLUNOR_CALLABLE_COMMAND()(**get_filtered_args(args))
            elif callable(args._VOLUNOR_CALLABLE_COMMAND) and args._VOLUNOR_CALLABLE_COMMAND.__name__ == "<lambda>":
                args._VOLUNOR_CALLABLE_COMMAND(**get_filtered_args(args))
        else:
            args._VOLUNOR_CURRENT_PARSER.print_help()
        sys.exit(0)
