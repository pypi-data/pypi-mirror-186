"""
SPDX-FileCopyrightText: 2022-2023. Thomas Mahe <contact@tmahe.dev>
SPDX-License-Identifier: MIT

This work is licensed under the terms of the MIT license.
For a copy, see <https://opensource.org/licenses/MIT>.
"""

import abc
import argparse


class Command(object):

    @abc.abstractmethod
    def volunor_args(self, required_args: argparse.ArgumentParser, optional_args: argparse.ArgumentParser):
        pass  # pragma nocover

    @abc.abstractmethod
    def __call__(self, *args, **kwargs):
        pass  # pragma nocover
