from abc import ABC, abstractmethod

from kernel.service_bus.envelope import Envelope


class Subscriber(ABC):
    """
    Base class for all Atlas Service Bus subscribers.

    Every engine, AI module, service, plugin,
    broker connector, or research module inherits
    from this class.
    """

    def __init__(self, topic: str):

        self.topic = topic

    @abstractmethod
    def receive(self, envelope: Envelope):

        """
        Called whenever a message is delivered
        to this subscriber.
        """

        pass