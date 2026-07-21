"""
Atlas Forge Command Loader

Automatically discovers CLI commands.

Version: 2.0.0
"""

from __future__ import annotations

import inspect
import pkgutil
import importlib

from .base.command import Command
from .registry import CommandRegistry


class CommandLoader:

    def __init__(self, registry: CommandRegistry):

        self._registry = registry

    def discover(self):

        package = "forge.cli.commands"

        for _, module_name, _ in pkgutil.iter_modules(
            importlib.import_module(package).__path__
        ):

            module = importlib.import_module(
                f"{package}.{module_name}"
            )

            for _, obj in inspect.getmembers(module):

                if (
                    inspect.isclass(obj)
                    and issubclass(obj, Command)
                    and obj is not Command
                ):

                    self._registry.register(obj())