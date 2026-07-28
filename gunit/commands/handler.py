"""
Command handler.
"""

from __future__ import annotations

from abc import ABC, abstractmethod

from .command import Command
from .result import CommandResult


class CommandHandler(ABC):
    """
    Base command handler.
    """

    @abstractmethod
    def handle(
        self,
        command: Command,
    ) -> CommandResult:
        ...