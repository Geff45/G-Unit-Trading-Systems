"""
G-UNIT Platform Kernel

Telemetry Manager

Collects and stores system metrics.
"""


from typing import List

from .metrics import Metric



class TelemetryManager:
    """
    Central telemetry collector.
    """



    def __init__(self):

        self.metrics: List[Metric] = []



    def record(
        self,
        metric: Metric
    ):
        """
        Store metric.
        """

        self.metrics.append(
            metric
        )



    def get_metrics(
        self,
        source=None
    ):

        if source:

            return [

                metric

                for metric in self.metrics

                if metric.source == source

            ]


        return self.metrics



    def latest(
        self,
        count=10
    ):

        return self.metrics[-count:]



    def clear(self):

        self.metrics.clear()