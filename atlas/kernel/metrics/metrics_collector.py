from kernel.metrics.metric import Metric


class MetricsCollector:

    def __init__(self):

        self.registry = None

    def attach(self, registry):

        self.registry = registry

    def record(self, name, value, unit):

        metric = Metric(

            name=name,

            value=value,

            unit=unit,

        )

        self.registry.register(metric)