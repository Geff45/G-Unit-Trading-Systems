from kernel.health.health_monitor import HealthMonitor
from kernel.health.health_report import HealthReport
from kernel.health.health_status import HealthStatus

monitor = HealthMonitor()

monitor.update(
    HealthReport(
        service_id="runtime",
        status=HealthStatus.HEALTHY,
        message="Runtime operational",
    )
)

monitor.update(
    HealthReport(
        service_id="scheduler",
        status=HealthStatus.HEALTHY,
        message="Scheduler running",
    )
)

print("Services:", monitor.healthy())

for report in monitor.all():

    print(report.service_id, report.status.value)