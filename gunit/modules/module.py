"""
Atlas module base class.
"""

from __future__ import annotations

from abc import ABC, abstractmethod

from .module_context import ModuleContext


class Module(ABC):
    """
    Base class for Atlas modules.
    """

    @property
    @abstractmethod
    def name(self) -> str:
        """
        Module name.
        """

    @property
    def version(self) -> str:
        """
        Module version.
        """
        return "1.0.0"

    @abstractmethod
    def configure(self, context: ModuleContext) -> None:
        """
        Configure services.
        """

    def start(self, context: ModuleContext) -> None:
        """
        Called when the module starts.
        """

    def stop(self, context: ModuleContext) -> None:
        """
        Called when the module stops.
        """