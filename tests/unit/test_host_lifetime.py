from gunit.host.lifetime import HostLifetime


def test_lifetime_initial_state():
    lifetime = HostLifetime()

    assert lifetime.started is False
    assert lifetime.stopped is False


def test_lifetime_start():
    lifetime = HostLifetime()

    lifetime.start()

    assert lifetime.started is True
    assert lifetime.stopped is False


def test_lifetime_stop():
    lifetime = HostLifetime()

    lifetime.start()
    lifetime.stop()

    assert lifetime.started is False
    assert lifetime.stopped is True