from gunit.extensions import ExtensionState


def test_extension_state():

    assert ExtensionState.CREATED.value == "created"
    assert ExtensionState.REGISTERED.value == "registered"
    assert ExtensionState.INITIALIZED.value == "initialized"
    assert ExtensionState.ENABLED.value == "enabled"
    assert ExtensionState.DISABLED.value == "disabled"
    assert ExtensionState.FAILED.value == "failed"
