from gunit.core.runtime import RuntimeState


def test_runtime_state_contains_expected_values() -> None:
    assert RuntimeState.CREATED.name == "CREATED"
    assert RuntimeState.INITIALIZING.name == "INITIALIZING"
    assert RuntimeState.STARTING.name == "STARTING"
    assert RuntimeState.RUNNING.name == "RUNNING"
    assert RuntimeState.STOPPING.name == "STOPPING"
    assert RuntimeState.STOPPED.name == "STOPPED"
    assert RuntimeState.FAILED.name == "FAILED"