"""
Kernel boot sequence controller.
"""

from __future__ import annotations

from .kernel import Kernel


class BootManager:
    """
    Controls kernel startup.
    """

    def __init__(self) -> None:
        self.kernel = Kernel()

    def boot(self) -> Kernel:

        self.kernel.logger.info("Boot sequence initiated.")

        self.kernel.start()

        self.kernel.logger.info("Boot sequence completed.")

        return self.kernel
