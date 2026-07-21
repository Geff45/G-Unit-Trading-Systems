class DependencyManager:

    def __init__(self):
        self.dependencies = {}

    def add(self, module, depends_on):
        self.dependencies[module] = depends_on

        return {
            "module": module,
            "depends_on": depends_on
        }

    def get(self, module):
        return self.dependencies.get(module, [])

    def all(self):
        return self.dependencies