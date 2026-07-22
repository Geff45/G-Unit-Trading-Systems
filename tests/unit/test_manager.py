from gunit.core.logging import LoggerFactory
from gunit.core.logging import LoggerManager


def test_factory_returns_singleton():
    assert LoggerFactory.manager() is LoggerFactory.manager()


def test_manager_caches_loggers():
    manager = LoggerManager()

    first = manager.get_logger("kernel")
    second = manager.get_logger("kernel")

    assert first is second