"""
Atlas AI Operating System
=========================

Module:
    IService

Purpose:
    Defines the standard lifecycle contract for every Atlas service.

Author:
    Atlas Development Team

Version:
    1.0.0
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Dict


class IService(ABC):
    """
    Base interface implemented by every Atlas service.
    """

    @abstractmethod
    def initialize(self) -> None:
        """
        Allocate internal resources.

        Called once before configuration.
        """
        raise NotImplementedError

    @abstractmethod
    def configure(self, configuration: Dict[str, Any]) -> None:
        """
        Apply configuration.

        Parameters
        ----------
        configuration:
            Dictionary containing service configuration.
        """
        raise NotImplementedError

    @abstractmethod
    def validate(self) -> bool:
        """
        Validate the service.

        Returns
        -------
        bool
            True if valid.
        """
        raise NotImplementedError

    @abstractmethod
    def start(self) -> None:
        """
        Start the service.
        """
        raise NotImplementedError

    @abstractmethod
    def pause(self) -> None:
        """
        Pause the service.
        """
        raise NotImplementedError

    @abstractmethod
    def resume(self) -> None:
        """
        Resume execution.
        """
        raise NotImplementedError

    @abstractmethod
    def stop(self) -> None:
        """
        Stop the service.
        """
        raise NotImplementedError

    @abstractmethod
    def shutdown(self) -> None:
        """
        Release all resources.
        """
        raise NotImplementedError

    @abstractmethod
    def health(self) -> Dict[str, Any]:
        """
        Return current health information.
        """
        raise NotImplementedError

    @abstractmethod
    def metrics(self) -> Dict[str, Any]:
        """
        Return runtime metrics.
        """
        raise NotImplementedError

    @abstractmethod
    def version(self) -> str:
        """
        Return service version.
        """
        raise NotImplementedError

    @abstractmethod
    def information(self) -> Dict[str, Any]:
        """
        Return descriptive information.

        Example:
            {
                "name": "Kernel",
                "author": "Atlas",
                "version": "1.0.0"
            }
        """
        raise NotImplementedError