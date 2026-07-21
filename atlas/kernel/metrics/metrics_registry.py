class MetricsRegistry:
    
    def __init__(self):

        self._metrics = {}

    def register(self, metric):

        self._metrics[metric.name] = metric

    def get(self, name):

        return self._metrics.get(name)

    def all(self):

        return list(self._metrics.values())

    def count(self):

        return len(self._metrics)