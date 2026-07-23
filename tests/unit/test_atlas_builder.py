from gunit.atlas.builder import AtlasBuilder
from gunit.atlas.engine import AtlasEngine


def test_builder_returns_engine():
    engine = AtlasBuilder().build()

    assert isinstance(engine, AtlasEngine)