from gunit.atlas.engine import AtlasEngine
from gunit.atlas.state import AtlasState


def test_engine_starts_created():
    engine = AtlasEngine()

    assert engine.state is AtlasState.CREATED


def test_engine_boot():
    engine = AtlasEngine()

    engine.boot()

    assert engine.state is AtlasState.RUNNING
    assert engine.running


def test_engine_shutdown():
    engine = AtlasEngine()

    engine.boot()
    engine.shutdown()

    assert engine.state is AtlasState.STOPPED