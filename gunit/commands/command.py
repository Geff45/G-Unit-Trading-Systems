"""
Base command.
"""

from __future__ import annotations

from abc import ABC


class Command(ABC):
    """
    Base command type.
    """

    @property
    def name(self) -> str:
        return self.__class__.__name__