class ServiceLoader:

    def __init__(self):
        self.services = {}

    def register(self, name, service):

        self.services[name] = service

        return {
            "status": "registered",
            "service": name
        }

    def load(self, name):

        return self.services.get(name)

    def services_list(self):

        return list(self.services.keys())