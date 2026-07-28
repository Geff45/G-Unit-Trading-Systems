"""
Application lifetime manager.
"""

from __future__ import annotations


class HostLifetime:
    """
    Tracks the running state of the host.
    """

    def __init__(self) -> None:
        self._started = False
        self._stopped = False

    @property
    def started(self) -> bool:
        return self._started

    @property
    def stopped(self) -> bool:
        return self._stopped

    def start(self) -> None:
        self._started = True
        self._stopped = False

    def stop(self) -> None:
        self._started = False
        self._stopped = True