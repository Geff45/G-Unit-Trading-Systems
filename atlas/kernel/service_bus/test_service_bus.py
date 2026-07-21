from kernel.service_bus.bus import ServiceBus
from kernel.service_bus.subscriber import Subscriber


class DecisionCouncil(Subscriber):

    def __init__(self):

        super().__init__(
            "market.trend.changed"
        )

    def receive(self, envelope):

        print()

        print("Atlas Enterprise Service Bus")

        print()

        print("Publisher:")

        print(envelope.sender)

        print()

        print("Topic:")

        print(envelope.message.topic)

        print()

        print("Subscriber:")

        print("Decision Council")

        print()

        print("Received:")

        print(envelope.message.payload)

        print()

        print("Status:")

        print("SUCCESS")


bus = ServiceBus()

decision = DecisionCouncil()

bus.subscribe(decision)

bus.publisher.publish(
    topic="market.trend.changed",
    payload="BUY EURUSD",
    sender="Trend Engine",
)