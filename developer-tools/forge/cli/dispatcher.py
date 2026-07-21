"""
Atlas Forge CLI Dispatcher

Routes CLI commands to their handlers.

Version: 2.0.0
"""

from __future__ import annotations

from .registry import CommandRegistry


class CommandDispatcher:

    def __init__(self, registry: CommandRegistry):

        self._registry = registry

    def dispatch(self, command_name: str, args=None):

        command_name = command_name.lower()

        if not self._registry.exists(command_name):
            raise ValueError(
                f"Unknown command: '{command_name}'"
            )

        command = self._registry.get(command_name)

        return command.execute(args)