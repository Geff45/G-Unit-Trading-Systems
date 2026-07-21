"""
G-UNIT Platform Kernel

Event Bus

Internal communication system.
"""


from typing import Dict, List, Callable


from .event import PlatformEvent



class EventBus:
    """
    Publish and subscribe event system.
    """



    def __init__(self):

        self.listeners: Dict[
            str,
            List[Callable]
        ] = {}



    def subscribe(
        self,
        event_name: str,
        callback: Callable
    ):
        """
        Subscribe to an event.
        """


        if event_name not in self.listeners:

            self.listeners[event_name] = []


        self.listeners[event_name].append(
            callback
        )



    def publish(
        self,
        event: PlatformEvent
    ):
        """
        Broadcast event.
        """


        subscribers = self.listeners.get(
            event.name,
            []
        )


        for callback in subscribers:

            callback(event)



    def unsubscribe(
        self,
        event_name: str,
        callback: Callable
    ):

        if event_name in self.listeners:

            self.listeners[event_name].remove(
                callback
            )



    def list_events(self):

        return list(
            self.listeners.keys()
        )