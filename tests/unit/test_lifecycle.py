from gunit.core.lifecycle import LifecycleManager
from gunit.core.lifecycle import LifecycleState


def test_lifecycle_start():

    manager = LifecycleManager()

    manager.start()

    assert manager.state == LifecycleState.RUNNING

    assert manager.running


def test_lifecycle_stop():

    manager = LifecycleManager()

    manager.start()

    manager.stop()

    assert manager.state == LifecycleState.STOPPED

    assert not manager.running