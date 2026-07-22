from gunit.core.logging import LoggerFactory


def test_factory_returns_same_logger():

    first = LoggerFactory.get_logger("kernel")

    second = LoggerFactory.get_logger("kernel")

    assert first is second
