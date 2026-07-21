class NodeRegistry:

    def __init__(self):

        self.registry = {}


    def add(self, node):

        self.registry[node["name"]] = node

        return {
            "status": "stored",
            "node": node["name"]
        }


    def get(self, name):

        return self.registry.get(name)


    def all(self):

        return list(self.registry.values())