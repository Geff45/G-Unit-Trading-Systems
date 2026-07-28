from gunit.container.service_container import ServiceContainer
from gunit.host.background_service import BackgroundService
from gunit.host.host import Host
from gunit.host.options import HostOptions


def test_clear_services():
    host = Host(
        ServiceContainer(),
        HostOptions(),
    )

    host.add_service(BackgroundService())
    host.add_service(BackgroundService())

    assert len(host.hosted_services.services) == 2

    host.clear_services()

    assert len(host.hosted_services.services) == 0


def test_add_multiple_services():
    host = Host(
        ServiceContainer(),
        HostOptions(),
    )

    for _ in range(5):
        host.add_service(
            BackgroundService()
        )

    assert len(host.hosted_services.services) == 5