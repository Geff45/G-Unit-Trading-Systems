"""
G-UNIT Platform Kernel

Health Monitor
"""

from .health_report import HealthReport


class HealthMonitor:
    """
    Aggregates platform health information.
    """

    def __init__(self):

        self._checks = []

    def register_check(self, check):

        self._checks.append(check)

    def run(self):

        report = HealthReport(
            platform_status="RUNNING"
        )

        for check in self._checks:

            try:

                result = check()

                if result is not None:

                    report.services.append(result)

            except Exception as exc:

                report.errors.append(str(exc))

                report.platform_status = "DEGRADED"

        return report