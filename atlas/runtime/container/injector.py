class Injector:

    def __init__(self, resolver):

        self.resolver = resolver

    def inject(self, service_name):

        return self.resolver.resolve(service_name)