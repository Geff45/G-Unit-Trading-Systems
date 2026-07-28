from gunit.host.background_service import BackgroundService
from gunit.host.lifetime import HostLifetime
from gunit.host.service_manager import HostedServiceManager
from gunit.host.startup import StartupPipeline


def test_pipeline_start():
    lifetime = HostLifetime()
    manager = HostedServiceManager()

    service = BackgroundService()
    manager.add(service)

    pipeline = StartupPipeline(lifetime, manager)

    pipeline.start()

    assert lifetime.started
    assert service.running


def test_pipeline_stop():
    lifetime = HostLifetime()
    manager = HostedServiceManager()

    service = BackgroundService()
    manager.add(service)

    pipeline = StartupPipeline(lifetime, manager)

    pipeline.start()
    pipeline.stop()

    assert lifetime.stopped
    assert not service.running