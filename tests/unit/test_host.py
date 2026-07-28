from gunit.container.service_container import ServiceContainer

from gunit.host.background_service import BackgroundService
from gunit.host.host import Host
from gunit.host.options import HostOptions


def test_host_start():
    host = Host(
        ServiceContainer(),
        HostOptions(),
    )

    host.start()

    assert host.running


def test_host_stop():
    host = Host(
        ServiceContainer(),
        HostOptions(),
    )

    host.start()
    host.stop()

    assert not host.running


def test_host_service_registration():
    host = Host(
        ServiceContainer(),
        HostOptions(),
    )

    service = BackgroundService()

    host.add_service(service)

    host.start()

    assert service.running

    host.stop()

    assert not service.running