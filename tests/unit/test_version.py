"""
Unit tests for the Version model.
"""

from gunit.core.models.version import Version


def test_version_creation() -> None:
    """Test that a Version object is created correctly."""

    version = Version(
        major=1,
        minor=0,
        patch=0,
    )

    assert version.major == 1
    assert version.minor == 0
    assert version.patch == 0


def test_version_string() -> None:
    """Test the string representation."""

    version = Version(
        major=2,
        minor=5,
        patch=7,
    )

    assert str(version) == "2.5.7"


def test_version_equality() -> None:
    """Test equality between versions."""

    version1 = Version(1, 0, 0)
    version2 = Version(1, 0, 0)

    assert version1 == version2


def test_version_inequality() -> None:
    """Test inequality between versions."""

    version1 = Version(1, 0, 0)
    version2 = Version(1, 1, 0)

    assert version1 != version2