from .configuration import Configuration


class ConfigurationManager(Configuration):

    def __init__(self):
        super().__init__()


__all__ = ["ConfigurationManager"]
