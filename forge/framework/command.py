from __future__ import annotations

from abc import ABC, abstractmethod

from .command_context import CommandContext
from .command_result import CommandResult


class Command(ABC):
    """
    Base class for every Forge command.
    """

    name = "command"

    def run(
        self,
        context: CommandContext,
    ) -> CommandResult:

        self.validate(context)

        return self.execute(context)

    def validate(
        self,
        context: CommandContext,
    ) -> None:
        """
        Override when validation is required.
        """
        return

    @abstractmethod
    def execute(
        self,
        context: CommandContext,
    ) -> CommandResult:
        ...