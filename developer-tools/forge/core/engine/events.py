"""
Atlas Forge Event System

Provides internal event communication
between Forge components.

Version: 1.0.0
"""

from typing import Callable, Dict, List, Any


class EventBus:
    """
    Central event dispatcher for Atlas Forge.
    """

    def __init__(self):
        self._listeners: Dict[str, List[Callable]] = {}


    def subscribe(self, event_name: str, callback: Callable) -> None:
        """
        Register a listener for an event.
        """

        if event_name not in self._listeners:
            self._listeners[event_name] = []

        self._listeners[event_name].append(callback)


    def emit(self, event_name: str, data: Any = None) -> None:
        """
        Trigger an event.
        """

        listeners = self._listeners.get(event_name, [])

        for callback in listeners:
            callback(data)


    def unsubscribe(self, event_name: str, callback: Callable) -> None:
        """
        Remove a listener.
        """

        if event_name in self._listeners:
            if callback in self._listeners[event_name]:
                self._listeners[event_name].remove(callback)


    def clear(self) -> None:
        """
        Remove all events.
        """

        self._listeners.clear()