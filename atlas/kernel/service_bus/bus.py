from kernel.service_bus.router import Router
from kernel.service_bus.dispatcher import Dispatcher
from kernel.service_bus.publisher import Publisher
from kernel.service_bus.subscriber import Subscriber
from kernel.service_bus.envelope import Envelope

from kernel.middleware.pipeline import MiddlewarePipeline
from kernel.middleware.validation import ValidationMiddleware
from kernel.middleware.logging import LoggingMiddleware
from kernel.middleware.metrics import MetricsMiddleware
from kernel.middleware.tracing import TracingMiddleware
from kernel.middleware.authentication import AuthenticationMiddleware
from kernel.middleware.authorization import AuthorizationMiddleware
from kernel.middleware.compression import CompressionMiddleware
from kernel.middleware.encryption import EncryptionMiddleware


class ServiceBus:
    """
    Atlas Enterprise Service Bus
    """

    def __init__(self):

        self.router = Router()

        self.dispatcher = Dispatcher(
            self.router
        )

        self.publisher = Publisher(
            self
        )

        self.pipeline = MiddlewarePipeline()

        self._register_default_middleware()

    def _register_default_middleware(self):

        self.pipeline.add(
            ValidationMiddleware()
        )

        self.pipeline.add(
            AuthenticationMiddleware()
        )

        self.pipeline.add(
            AuthorizationMiddleware()
        )

        self.pipeline.add(
            CompressionMiddleware()
        )

        self.pipeline.add(
            EncryptionMiddleware()
        )

        self.pipeline.add(
            LoggingMiddleware()
        )

        self.pipeline.add(
            MetricsMiddleware()
        )

        self.pipeline.add(
            TracingMiddleware()
        )

    def publish(
        self,
        envelope: Envelope,
    ):

        envelope = self.pipeline.process(
            envelope
        )

        self.dispatcher.dispatch(
            envelope
        )

    def subscribe(
        self,
        subscriber: Subscriber,
    ):

        self.router.subscribe(
            subscriber
        )

    def unsubscribe(
        self,
        subscriber: Subscriber,
    ):

        self.router.unsubscribe(
            subscriber
        )