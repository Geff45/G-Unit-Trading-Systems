"""
Atlas Forge Command Base

Version: 2.0.0
"""

from __future__ import annotations

from abc import ABC, abstractmethod


class Command(ABC):
    """
    Base class for every Forge CLI command.
    """

    NAME = ""
    ALIASES = []
    CATEGORY = "General"
    DESCRIPTION = ""
    USAGE = ""
    EXAMPLES = []
    VERSION = "2.0.0"
    HIDDEN = False

    @property
    def name(self):
        return self.NAME

    @property
    def aliases(self):
        return self.ALIASES

    @property
    def category(self):
        return self.CATEGORY

    @property
    def description(self):
        return self.DESCRIPTION

    @property
    def usage(self):
        return self.USAGE

    @property
    def examples(self):
        return self.EXAMPLES

    @abstractmethod
    def execute(self, args):
        """
        Execute the command.
        """
        raise NotImplementedError