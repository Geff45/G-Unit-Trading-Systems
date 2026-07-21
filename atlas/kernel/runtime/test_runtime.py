from kernel.runtime.runtime import AtlasRuntime
from kernel.registry.service_descriptor import ServiceDescriptor


class Logger:
    pass


class ConsoleLogger(Logger):

    def __init__(self):

        self.name = "Atlas Runtime Logger"


runtime = AtlasRuntime()

descriptor = ServiceDescriptor(
    service_id="logger",
    name="Console Logger",
    version="1.0.0",
)

runtime.add_service(
    descriptor,
    ConsoleLogger,
)

logger = runtime.resolve(ConsoleLogger)

print(logger.name)

print()

print("Registered Services")

print(runtime.services())