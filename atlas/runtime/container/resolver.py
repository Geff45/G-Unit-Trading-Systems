class Resolver:

    def __init__(self, registry):

        self.registry = registry

    def resolve(self, name):

        service = self.registry.get(name)

        if service is None:

            raise Exception(
                f"Service '{name}' not registered."
            )

        return service