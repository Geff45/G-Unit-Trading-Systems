"""
Base command handler.
"""

from __future__ import annotations

from abc import ABC, abstractmethod

from .command import Command
from .command_context import CommandContext
from .command_result import CommandResult


class CommandHandler(ABC):
    """
    Base class for all command handlers.
    """

    @abstractmethod
    def handle(
        self,
        command: Command,
        context: CommandContext,
    ) -> CommandResult:
        """
        Handles a command.
        """
        raise NotImplementedError