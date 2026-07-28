"""
Background service implementation.
"""

from __future__ import annotations

from .hosted_service import HostedService


class BackgroundService(HostedService):
    """
    Base implementation for long-running services.
    """

    def __init__(self) -> None:
        self._running = False

    @property
    def running(self) -> bool:
        return self._running

    def start(self) -> None:
        self._running = True

    def stop(self) -> None:
        self._running = False