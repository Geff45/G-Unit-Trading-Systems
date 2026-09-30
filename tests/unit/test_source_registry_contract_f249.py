import inspect

import pytest

from gunit.data_sources.source_registry import SourceRegistry


def test_source_registry_is_concrete():
    assert not inspect.isabstract(SourceRegistry)


def test_source_registry_can_be_instantiated():
    registry = SourceRegistry()
    assert registry is not None


def test_source_registry_defines_register():
    assert hasattr(SourceRegistry, "register")


def test_source_registry_defines_get():
    assert hasattr(SourceRegistry, "get")


def test_source_registry_defines_names():
    assert hasattr(SourceRegistry, "names")


def test_source_registry_defines_contains():
    assert hasattr(SourceRegistry, "__contains__")


def test_source_registry_can_hold_multiple_sources():
    registry = SourceRegistry()
    assert len(registry.names()) == 0
