import json

from gunit.core.logging import JsonFormatter
from gunit.core.logging import LogLevel
from gunit.core.logging import LogRecord
from gunit.core.logging import StandardFormatter


def test_standard_formatter():

    formatter = StandardFormatter()

    record = LogRecord(
        level=LogLevel.INFO,
        logger="kernel",
        message="Booted",
    )

    output = formatter.format(record)

    assert "Booted" in output

    assert "INFO" in output


def test_json_formatter():

    formatter = JsonFormatter()

    record = LogRecord(
        level=LogLevel.ERROR,
        logger="system",
        message="Failure",
    )

    data = json.loads(formatter.format(record))

    assert data["level"] == "ERROR"

    assert data["message"] == "Failure"