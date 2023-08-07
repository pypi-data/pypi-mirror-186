"""
SPDX-FileCopyrightText: 2022-2023. Thomas Mahe <contact@tmahe.dev>
SPDX-License-Identifier: MIT

This work is licensed under the terms of the MIT license.
For a copy, see <https://opensource.org/licenses/MIT>.
"""
import argparse
import inspect

from volunor import Command


def get_command_description(c, single_line=False):
    out = ""
    if issubclass(type(c), Command.__class__):
        out = inspect.getdoc(c)

    elif callable(c) and c.__name__ == "<lambda>":
        comments = inspect.getcomments(c)
        if comments is None:
            comments = ""
        filtered_comments = ""
        for line in comments.split('\n'):
            if len(line) > 0 and line[0] == '#':
                filtered_comments += line[1:].strip() + '\n'

        out = filtered_comments

    elif isinstance(c, dict):
        out = 'Subcommand group'

    if single_line and out is not None:
        return out.strip().split('\n')[0]
    return out


def get_filtered_args(p: argparse.Namespace):
    out = p.__dict__.copy()
    # Remove reserved pre-populated arguments
    for key in p.__dict__.keys():
        if '_VOLUNOR_' == key[:9]:
            del out[key]
    return out
