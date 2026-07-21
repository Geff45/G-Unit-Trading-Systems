from kernel.registry.dependency_graph import DependencyGraph

graph = DependencyGraph()

graph.add_dependency("risk_engine", "trend_engine")
graph.add_dependency("decision_council", "risk_engine")
graph.add_dependency("decision_council", "volume_engine")
graph.add_dependency("decision_council", "liquidity_engine")

print("Registered Services")
print(graph.services())

print()

print("Decision Council Dependencies")
print(graph.dependencies_of("decision_council"))

print()

print("Risk Depends on Trend")
print(graph.has_dependency("risk_engine", "trend_engine"))