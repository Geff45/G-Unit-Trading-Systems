from registry import Registry
from resolver import Resolver
from injector import Injector


class Container:

    def __init__(self):

        self.registry = Registry()

        self.resolver = Resolver(self.registry)

        self.injector = Injector(self.resolver)

    def register(self, name, service):

        return self.registry.register(
            name,
            service
        )

    def resolve(self, name):

        return self.injector.inject(name)

    def services(self):

        return self.registry.all()