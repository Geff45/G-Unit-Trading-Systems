class RuntimeConfiguration:
    def __init__(self):
        self.settings = {}

    def set(self, key, value):
        self.settings[key] = value
        return {"status": "set", "key": key}

    def get(self, key, default=None):
        return self.settings.get(key, default)

    def all(self):
        return self.settings