from kernel.services.service import Service
from kernel.services.service_descriptor import (
    ServiceDescriptor,
)
from kernel.services.service_loader import (
    ServiceLoader,
)


class TradingService(Service):

    def start(self):

        print(
            "Trading Service Started"
        )

    def stop(self):

        print(
            "Trading Service Stopped"
        )

    def pause(self):

        print(
            "Trading Service Paused"
        )

    def resume(self):

        print(
            "Trading Service Resumed"
        )


descriptor = ServiceDescriptor(
    service_id="trading",
    name="Trading Service",
    version="1.0.0",
)

service = TradingService(
    descriptor
)

loader = ServiceLoader()

container = loader.load(
    [service]
)

manager = container.manager_instance()

print()

print(
    "Registered Services:",
    manager.count(),
)

print()

manager.start(
    "trading"
)

print()

print(
    manager.get(
        "trading"
    ).descriptor.state.value
)