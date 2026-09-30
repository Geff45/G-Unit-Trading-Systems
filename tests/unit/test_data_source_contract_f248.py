import inspect

import pytest

from gunit.data_sources.data_source import DataSource


def test_data_source_is_abstract():
    assert inspect.isabstract(DataSource)


def test_data_source_defines_source_id():
    assert hasattr(DataSource, "source_id")


def test_data_source_defines_source_type():
    assert hasattr(DataSource, "source_type")


def test_data_source_defines_capabilities():
    assert hasattr(DataSource, "capabilities")


def test_data_source_cannot_be_instantiated():
    with pytest.raises(TypeError):
        DataSource()
