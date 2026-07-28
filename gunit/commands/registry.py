"""
Command registry.
"""

from __future__ import annotations

from typing import Type

from .command import Command
from .handler import CommandHandler


class CommandRegistry:

    def __init__(self) -> None:

        self._handlers: dict[
            Type[Command],
            CommandHandler,
        ] = {}

    def register(
        self,
        command: Type[Command],
        handler: CommandHandler,
    ) -> None:

        self._handlers[command] = handler

    def get(
        self,
        command: Type[Command],
    ) -> CommandHandler:

        return self._handlers[command]