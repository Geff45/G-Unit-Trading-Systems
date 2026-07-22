"""
Unit tests for the G-UNIT kernel.
"""

from gunit.core.kernel import BootManager, KernelState


def test_kernel_initial_state() -> None:
    manager = BootManager()

    assert manager.kernel.state == KernelState.CREATED


def test_kernel_boot() -> None:
    manager = BootManager()

    kernel = manager.boot()

    assert kernel.state == KernelState.RUNNING
    assert kernel.is_running()


def test_kernel_shutdown() -> None:
    manager = BootManager()

    kernel = manager.boot()
    kernel.stop()

    assert kernel.state == KernelState.STOPPED
    assert not kernel.is_running()