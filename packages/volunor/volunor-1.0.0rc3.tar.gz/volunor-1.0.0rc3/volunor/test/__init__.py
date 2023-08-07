"""
SPDX-FileCopyrightText: 2022-2023. Thomas Mahe <contact@tmahe.dev>
SPDX-License-Identifier: MIT

This work is licensed under the terms of the MIT license.
For a copy, see <https://opensource.org/licenses/MIT>.
"""

import io
from unittest import TestCase

from volunor.core.cli import Cli


class CliTestCase(TestCase):
    cli: Cli = None
    descriptor = None

    expected_output: str = None
    captured_output: io.StringIO = None

    exception_ctx = None
    expected_exit_code: int = None

    @classmethod
    def setUpClass(cls):
        cls.cli = Cli(prog=cls.__name__, descriptor=cls.descriptor)

    def tearDown(self) -> None:
        if self.expected_exit_code is not None:
            exited_with = self.exception_ctx.exception.code
            self.assertEqual(self.expected_exit_code, exited_with,
                             msg=f"SystemExit raised with code {exited_with} while {self.expected_exit_code} was expected")
        if self.expected_output is not None:
            self.assertEqual(self.expected_output, self.captured_output.getvalue())


