from gunit.core.logging import LogLevel


def test_level_names():

    assert LogLevel.INFO.label == "INFO"

    assert LogLevel.ERROR.label == "ERROR"


def test_from_string():

    assert LogLevel.from_string("info") == LogLevel.INFO

    assert LogLevel.from_string("warning") == LogLevel.WARNING