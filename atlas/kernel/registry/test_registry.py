from kernel.registry.service_descriptor import ServiceDescriptor
from kernel.registry.service_registry import ServiceRegistry


registry = ServiceRegistry()

trend = ServiceDescriptor(
    service_id="trend_engine",
    name="Trend Engine",
    version="1.0.0"
)

risk = ServiceDescriptor(
    service_id="risk_engine",
    name="Risk Engine",
    version="1.0.0",
    dependencies=["trend_engine"]
)

registry.register(trend)
registry.register(risk)

print("Services:", registry.count())

print("Trend Exists:", registry.exists("trend_engine"))

print("Risk:", registry.get("risk_engine"))

print("Registered Services")

for service in registry.all_services():
    print("-", service.service_id)