"""
Atlas Forge CLI Registry

Stores all available CLI commands.

Version: 2.0.0
"""

from __future__ import annotations

from typing import Dict, List

from .base.command import Command


class CommandRegistry:

    def __init__(self):

        self._commands: Dict[str, Command] = {}

    def register(self, command: Command) -> None:

        name = command.name.lower()

        if name in self._commands:
            raise ValueError(
                f"Command '{name}' already exists."
            )

        self._commands[name] = command

    def unregister(self, name: str) -> None:

        self._commands.pop(name.lower(), None)

    def exists(self, name: str) -> bool:

        return name.lower() in self._commands

    def get(self, name: str) -> Command:

        return self._commands[name.lower()]

    def all(self) -> List[Command]:

        return list(self._commands.values())

    def names(self) -> List[str]:

        return sorted(self._commands.keys())

    def count(self) -> int:

        return len(self._commands)