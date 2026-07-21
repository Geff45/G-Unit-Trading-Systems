"""
Atlas Forge Lifecycle Manager

Controls startup and shutdown phases
of Forge services.

Version: 1.0.0
"""


from typing import Callable, List


class LifecycleManager:
    """
    Manages application lifecycle events.

    Handles:
    - Startup hooks
    - Shutdown hooks
    - Service initialization order
    """

    def __init__(self):
        self._startup_hooks: List[Callable] = []
        self._shutdown_hooks: List[Callable] = []

        self.started = False


    def register_startup(self, callback: Callable) -> None:
        """
        Register a startup function.
        """

        self._startup_hooks.append(callback)


    def register_shutdown(self, callback: Callable) -> None:
        """
        Register a shutdown function.
        """

        self._shutdown_hooks.append(callback)


    def start(self) -> None:
        """
        Execute startup sequence.
        """

        if self.started:
            return

        for hook in self._startup_hooks:
            hook()

        self.started = True


    def stop(self) -> None:
        """
        Execute shutdown sequence.
        """

        if not self.started:
            return

        for hook in reversed(self._shutdown_hooks):
            hook()

        self.started = False