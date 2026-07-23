from gunit.atlas.state import AtlasState


def test_state_members_exist():
    assert AtlasState.CREATED.name == "CREATED"
    assert AtlasState.RUNNING.name == "RUNNING"
    assert AtlasState.STOPPED.name == "STOPPED"