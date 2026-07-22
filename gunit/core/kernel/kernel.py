"""
Enterprise Kernel.
"""

from __future__ import annotations

from gunit.core.logging import LoggerFactory

from .state import KernelState


class Kernel:
    """
    Core runtime kernel.
    """

    def __init__(self) -> None:

        self.logger = LoggerFactory.get_logger("kernel")

        self.state = KernelState.CREATED

    def start(self) -> None:

        self.logger.info("Kernel starting...")

        self.state = KernelState.RUNNING

        self.logger.info("Kernel started.")

    def stop(self) -> None:

        self.logger.info("Kernel stopping...")

        self.state = KernelState.STOPPED

        self.logger.info("Kernel stopped.")

    def is_running(self) -> bool:
        """
        Returns True if the kernel is currently running.
        """
        return self.state == KernelState.RUNNING

    def is_stopped(self) -> bool:
        """
        Returns True if the kernel is currently stopped.
        """
        return self.state == KernelState.STOPPED

    def is_created(self) -> bool:
        """
        Returns True if the kernel has been created but not started.
        """
        return self.state == KernelState.CREATED
