from kernel.config.config_loader import ConfigLoader


class ConfigurationManager:

    def __init__(self):

        self.loader = ConfigLoader()

        self._configs = {}

    def load(self, filename):

        self._configs[filename] = self.loader.load(filename)

    def get(self, filename):

        return self._configs.get(filename)

    def value(self, filename, *keys):

        data = self._configs.get(filename)

        for key in keys:
            data = data[key]

        return data