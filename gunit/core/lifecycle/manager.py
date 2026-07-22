"""
Lifecycle Manager.

Controls the startup and shutdown
of the G-Unit platform.
"""

from __future__ import annotations

from .state import LifecycleState


class LifecycleManager:
    """
    Controls the entire platform lifecycle.
    """

    def __init__(self):

        self._state = LifecycleState.CREATED

        self._kernel = None


    @property
    def state(self):

        return self._state


    @property
    def kernel(self):

        return self._kernel


    def start(self, kernel=None):

        self._state = LifecycleState.INITIALIZING

        if kernel:
            self._kernel = kernel

        self._state = LifecycleState.RUNNING


    def stop(self):

        if self._kernel:

            if hasattr(self._kernel, "stop"):
                self._kernel.stop()

        self._state = LifecycleState.STOPPED


    @property
    def running(self):

        return self._state is LifecycleState.RUNNING