"""
Command bus.
"""

from __future__ import annotations

from .command import Command
from .command_context import CommandContext
from .command_registry import CommandRegistry
from .command_result import CommandResult
from .exceptions import CommandNotFoundError


class CommandBus:
    """
    Dispatches commands.
    """

    def __init__(
        self,
        registry: CommandRegistry,
    ) -> None:

        self._registry = registry

    def dispatch(
        self,
        command: Command,
        context: CommandContext | None = None,
    ) -> CommandResult:

        if context is None:
            context = CommandContext()

        command_type = type(command)

        if not self._registry.contains(command_type):
            raise CommandNotFoundError(
                command_type.__name__
            )

        handler = self._registry.resolve(
            command_type
        )

        return handler.handle(
            command,
            context,
        )