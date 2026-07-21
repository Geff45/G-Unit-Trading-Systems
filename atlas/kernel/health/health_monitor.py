from kernel.health.health_report import HealthReport


class HealthMonitor:

    def __init__(self):

        self._reports = {}

    def update(self, report: HealthReport):

        self._reports[report.service_id] = report

    def get(self, service_id):

        return self._reports.get(service_id)

    def all(self):

        return list(self._reports.values())

    def healthy(self):

        return len(self._reports)