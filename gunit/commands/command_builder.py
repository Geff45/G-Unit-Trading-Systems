"""
Command framework builder.
"""

from __future__ import annotations

from .command_bus import CommandBus
from .command_registry import CommandRegistry


class CommandBuilder:
    """
    Builds the command framework.
    """

    def __init__(self) -> None:

        self._registry = CommandRegistry()

    @property
    def registry(self) -> CommandRegistry:

        return self._registry

    def build(self) -> CommandBus:

        return CommandBus(
            self._registry
        )