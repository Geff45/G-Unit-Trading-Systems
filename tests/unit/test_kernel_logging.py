from gunit.core.kernel import BootManager
from gunit.core.kernel import KernelState


def test_boot_changes_kernel_state():

    boot = BootManager()

    kernel = boot.boot()

    assert kernel.state == KernelState.RUNNING
