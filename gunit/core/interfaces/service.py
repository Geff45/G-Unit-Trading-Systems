"""
G-UNIT Enterprise Platform

Base Service Contract
"""

from __future__ import annotations

from abc import ABC, abstractmethod


class IService(ABC):
    """Base interface for every platform service."""

    @property
    @abstractmethod
    def id(self) -> str:
        """Unique service identifier."""

    @property
    @abstractmethod
    def name(self) -> str:
        """Display name."""

    @property
    @abstractmethod
    def version(self) -> str:
        """Service version."""

    @abstractmethod
    def initialize(self) -> None:
        """Prepare service."""

    @abstractmethod
    def start(self) -> None:
        """Start service."""

    @abstractmethod
    def stop(self) -> None:
        """Stop service."""

    @abstractmethod
    def shutdown(self) -> None:
        """Shutdown service."""