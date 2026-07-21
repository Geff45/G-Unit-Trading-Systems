class Registry:

    def __init__(self):
        self.services = {}

    def register(self, name, service):

        self.services[name] = service

        return {
            "status": "registered",
            "service": name
        }

    def get(self, name):

        return self.services.get(name)

    def all(self):

        return list(self.services.keys())