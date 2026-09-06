from .configuration import Configuration


class ConfigurationRoot(Configuration):

    def __init__(self, providers=None):
        super().__init__()

        self.providers = list(providers or [])

        for provider in self.providers:
            values = provider.load()

            if values:
                for key, value in values.items():
                    self.set(key, value)


__all__ = ["ConfigurationRoot"]
