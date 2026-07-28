from gunit.host.background_service import BackgroundService


def test_background_service_start():
    service = BackgroundService()

    assert service.running is False

    service.start()

    assert service.running is True


def test_background_service_stop():
    service = BackgroundService()

    service.start()
    service.stop()

    assert service.running is False