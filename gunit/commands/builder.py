"""
Command builder.
"""

from __future__ import annotations

from typing import Type

from .command import Command
from .dispatcher import CommandDispatcher
from .handler import CommandHandler
from .registry import CommandRegistry


class CommandBuilder:

    def __init__(self) -> None:

        self._registry = CommandRegistry()

    def add(
        self,
        command: Type[Command],
        handler: CommandHandler,
    ) -> "CommandBuilder":

        self._registry.register(
            command,
            handler,
        )

        return self

    def build(
        self,
    ) -> CommandDispatcher:

        return CommandDispatcher(
            self._registry
        )