from gunit.core.logging import Logger
from gunit.core.logging import LogLevel


def test_logger_creation():
    logger = Logger("kernel")

    assert logger.name == "kernel"
    assert logger.level == LogLevel.INFO


def test_logger_level_change():
    logger = Logger("kernel")
    logger.set_level(LogLevel.DEBUG)

    assert logger.level == LogLevel.DEBUG