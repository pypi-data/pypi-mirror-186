"""
SPDX-FileCopyrightText: 2022. Thomas Mahe <contact@tmahe.dev>
SPDX-License-Identifier: MIT

This work is licensed under the terms of the MIT license.
For a copy, see <https://opensource.org/licenses/MIT>.


We expose a minimal "public" API directly from `volunor`.
This covers the basic use-cases:
    from volunor import (
        Command,
        Cli,
    )
Other access should target the submodules directly
"""

from .core.command import Command
from .core.cli import Cli
