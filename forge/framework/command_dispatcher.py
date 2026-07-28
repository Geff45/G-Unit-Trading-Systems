from __future__ import annotations

from .command import Command
from .command_context import CommandContext
from .command_result import CommandResult


class CommandDispatcher:
    """
    Dispatches Forge commands.
    """

    def dispatch(
        self,
        command: Command,
        context: CommandContext,
    ) -> CommandResult:

        return command.run(context)


__all__ = ["CommandDispatcher"]
