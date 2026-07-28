"""
Command dispatcher.
"""

from __future__ import annotations

from .command import Command
from .registry import CommandRegistry
from .result import CommandResult


class CommandDispatcher:

    def __init__(
        self,
        registry: CommandRegistry,
    ) -> None:

        self._registry = registry

    def dispatch(
        self,
        command: Command,
    ) -> CommandResult:

        handler = self._registry.get(
            type(command)
        )

        return handler.handle(command)