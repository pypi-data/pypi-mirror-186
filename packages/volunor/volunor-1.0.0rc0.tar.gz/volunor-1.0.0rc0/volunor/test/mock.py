"""
SPDX-FileCopyrightText: 2022. Thomas Mahe <contact@tmahe.dev>
SPDX-License-Identifier: MIT

This work is licensed under the terms of the MIT license.
For a copy, see <https://opensource.org/licenses/MIT>.
"""
import contextlib
import io
import sys
from unittest.mock import patch

from . import CliTestCase


def with_exit_code(exit_code: int):
    def decorator_with_exit_code(func):
        def inner(self: CliTestCase, *args, **kwargs):
            with self.assertRaises(SystemExit) as ctx:
                self.exception_ctx = ctx
                self.expected_exit_code = exit_code
                return func(self, *args, **kwargs)
        return inner

    return decorator_with_exit_code


def with_captured_output(exit_code=None):
    def decorator_capture_output(func):
        def inner(self: CliTestCase, *args, **kwargs):
            output = io.StringIO()
            with contextlib.redirect_stdout(output):
                with contextlib.redirect_stderr(output):
                    self.captured_output = output
                    return func(self, *args, **kwargs)
        return inner
    return decorator_capture_output


def with_arguments(*args):
    arguments = list(args)

    def decorator_with_arguments(func):
        arguments.insert(0, str(func).split(' ')[1])

        def inner(*args, **kwargs):
            with patch.object(sys, 'argv', arguments):
                return func(*args, **kwargs)

        return inner

    return decorator_with_arguments
