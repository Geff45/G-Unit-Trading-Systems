from gunit.core.logging import LogLevel
from gunit.core.logging import LogRecord


def test_record_creation():

    record = LogRecord(
        level=LogLevel.INFO,
        logger="kernel",
        message="Boot successful"
    )

    assert record.logger == "kernel"

    assert record.level == LogLevel.INFO

    assert record.message == "Boot successful"


def test_record_timestamp():

    record = LogRecord(
        level=LogLevel.DEBUG,
        logger="core",
        message="Testing"
    )

    assert record.timestamp is not None