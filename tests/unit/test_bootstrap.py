from gunit.atlas.bootstrap import bootstrap
from gunit.atlas.state import AtlasState


def test_bootstrap():
    engine = bootstrap()

    assert engine.state is AtlasState.RUNNING