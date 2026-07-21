from kernel.metrics.metrics_registry import MetricsRegistry
from kernel.metrics.metrics_collector import MetricsCollector

registry = MetricsRegistry()

collector = MetricsCollector()

collector.attach(registry)

collector.record(

    "cpu_usage",

    18.5,

    "%",

)

collector.record(

    "memory_usage",

    420,

    "MB",

)

print("Metrics:", registry.count())

for metric in registry.all():

    print(

        metric.name,

        metric.value,

        metric.unit,

    )