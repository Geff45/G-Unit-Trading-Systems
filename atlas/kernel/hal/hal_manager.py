from kernel.hal.cpu.cpu_manager import (
    CPUManager,
)

from kernel.hal.memory.memory_manager import (
    MemoryManager,
)


class HALManager:

    def __init__(self):

        self.cpu = CPUManager()

        self.memory = MemoryManager()

    def collect(self):

        return {

            "cpu": self.cpu.collect(),

            "memory": self.memory.collect(),

        }