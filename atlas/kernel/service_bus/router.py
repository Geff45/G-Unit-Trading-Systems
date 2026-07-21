from collections import defaultdict

from kernel.service_bus.envelope import Envelope
from kernel.service_bus.subscriber import Subscriber


class Router:
    """
    Enterprise Atlas Router

    Responsible for routing
    messages to subscribers.
    """

    def __init__(self):

        self._routes = defaultdict(list)

    def subscribe(
        self,
        subscriber: Subscriber,
    ):

        self._routes[
            subscriber.topic
        ].append(
            subscriber
        )

    def unsubscribe(
        self,
        subscriber: Subscriber,
    ):

        if subscriber in self._routes[
            subscriber.topic
        ]:

            self._routes[
                subscriber.topic
            ].remove(
                subscriber
            )

    def dispatch(
        self,
        envelope: Envelope,
    ):

        subscribers = self._routes.get(
            envelope.message.topic,
            [],
        )

        for subscriber in subscribers:

            subscriber.receive(
                envelope
            )

    def subscribers(
        self,
        topic: str,
    ):

        return self._routes.get(
            topic,
            [],
        )