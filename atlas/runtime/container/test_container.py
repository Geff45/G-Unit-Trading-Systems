from container import Container


container = Container()


class TradingEngine:

    def __init__(self):

        self.name = "Institutional Trading Engine"

    def info(self):

        return self.name


class AIEngine:

    def __init__(self):

        self.version = "Atlas AI v1"

    def info(self):

        return self.version


print(

    container.register(
        "trading",
        TradingEngine()
    )

)

print(

    container.register(
        "ai",
        AIEngine()
    )

)

print(container.services())

print(container.resolve("trading").info())

print(container.resolve("ai").info())