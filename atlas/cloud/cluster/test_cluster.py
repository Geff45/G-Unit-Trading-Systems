from cluster_manager import ClusterManager
from node_registry import NodeRegistry


cluster = ClusterManager()

registry = NodeRegistry()


node = cluster.register_node(
    "worker-001",
    cpu=16,
    ram="64GB",
    gpu="RTX4090"
)

print(node)


registry.add(
    node["node"]
)

print(
    cluster.list_nodes()
)


print(
    cluster.health_check()
)


print(
    registry.all()
)