from enum import Enum


class IdentityType(Enum):

    KERNEL = "Kernel"

    SERVICE = "Service"

    MODULE = "Module"

    WORKER = "Worker"

    PLUGIN = "Plugin"

    MODEL = "Model"

    CONNECTION = "Connection"

    STRATEGY = "Strategy"

    PORTFOLIO = "Portfolio"

    ORDER = "Order"

    POSITION = "Position"

    SESSION = "Session"

    DATASOURCE = "DataSource"

    BROKER = "Broker"

    UNKNOWN = "Unknown"