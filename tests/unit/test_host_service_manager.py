from gunit.host.background_service import BackgroundService
from gunit.host.service_manager import HostedServiceManager


def test_add_service():
    manager = HostedServiceManager()
    service = BackgroundService()

    manager.add(service)

    assert len(manager.services) == 1


def test_start_all():
    manager = HostedServiceManager()

    s1 = BackgroundService()
    s2 = BackgroundService()

    manager.add(s1)
    manager.add(s2)

    manager.start_all()

    assert s1.running
    assert s2.running


def test_stop_all():
    manager = HostedServiceManager()

    s1 = BackgroundService()
    s2 = BackgroundService()

    manager.add(s1)
    manager.add(s2)

    manager.start_all()
    manager.stop_all()

    assert not s1.running
    assert not s2.running


def test_remove_service():
    manager = HostedServiceManager()

    service = BackgroundService()

    manager.add(service)
    manager.remove(service)

    assert len(manager.services) == 0