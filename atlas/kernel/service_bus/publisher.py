from kernel.service_bus.message import Message
from kernel.service_bus.envelope import Envelope


class Publisher:
    """
    Base Publisher for Atlas Service Bus.
    """

    def __init__(self, bus):

        self.bus = bus

    def publish(
        self,
        topic: str,
        payload,
        priority: int = 3,
        sender: str = "",
        receiver: str = "",
    ):

        message = Message(
            topic=topic,
            payload=payload,
            priority=priority,
        )

        envelope = Envelope(
            message=message,
            sender=sender,
            receiver=receiver,
        )

        self.bus.publish(envelope)