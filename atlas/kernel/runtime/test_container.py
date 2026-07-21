from kernel.runtime.container import DependencyContainer


class Logger:

    pass


class ConsoleLogger(Logger):

    def __init__(self):

        self.name = "Atlas Logger"


container = DependencyContainer()

container.register(Logger, ConsoleLogger)

logger1 = container.resolve(Logger)

logger2 = container.resolve(Logger)

print(logger1.name)

print(logger1 is logger2)