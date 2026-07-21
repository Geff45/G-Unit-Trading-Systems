class ClusterManager:

    def __init__(self):
        self.nodes = []


    def register_node(self, name, cpu, ram, gpu):

        node = {
            "name": name,
            "cpu": cpu,
            "ram": ram,
            "gpu": gpu,
            "status": "online"
        }

        self.nodes.append(node)

        return {
            "status": "registered",
            "node": node
        }


    def list_nodes(self):

        return self.nodes


    def health_check(self):

        return {
            "nodes": len(self.nodes),
            "status": "healthy"
        }


    def remove_node(self, name):

        self.nodes = [
            node for node in self.nodes
            if node["name"] != name
        ]

        return {
            "status": "removed",
            "node": name
        }