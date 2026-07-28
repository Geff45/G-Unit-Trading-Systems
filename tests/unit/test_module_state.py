from gunit.modules import ModuleState


def test_states():
    assert ModuleState.CREATED.value == "created"
    assert ModuleState.LOADED.value == "loaded"
    assert ModuleState.STARTED.value == "started"
    assert ModuleState.STOPPED.value == "stopped"