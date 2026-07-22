from pathlib import Path

from gunit.core.logging import FileHandler
from gunit.core.logging import LogLevel
from gunit.core.logging import LogRecord
from gunit.core.logging import StandardFormatter


def test_file_handler(tmp_path):

    logfile = tmp_path / "test.log"

    handler = FileHandler(
        logfile,
        StandardFormatter(),
    )

    handler.emit(
        LogRecord(
            level=LogLevel.INFO,
            logger="kernel",
            message="Hello",
        )
    )

    assert logfile.exists()

    assert "Hello" in logfile.read_text(encoding="utf-8")