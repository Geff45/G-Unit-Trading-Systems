"""
Command registry.
"""

from __future__ import annotations

from typing import Dict, Type

from .command import Command
from .command_handler import CommandHandler
from .exceptions import DuplicateCommandError


class CommandRegistry:
    """
    Stores command handlers.
    """

    def __init__(self) -> None:

        self._handlers: Dict[
            Type[Command],
            CommandHandler,
        ] = {}

    def register(
        self,
        command: Type[Command],
        handler: CommandHandler,
    ) -> None:

        if command in self._handlers:
            raise DuplicateCommandError(
                command.__name__
            )

        self._handlers[command] = handler

    def contains(
        self,
        command: Type[Command],
    ) -> bool:

        return command in self._handlers

    def resolve(
        self,
        command: Type[Command],
    ) -> CommandHandler:

        return self._handlers[command]