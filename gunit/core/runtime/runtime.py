"""
Runtime manager.
"""

from __future__ import annotations


class Runtime:
    """
    Core runtime controller.
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