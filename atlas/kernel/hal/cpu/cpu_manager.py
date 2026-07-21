import platform
import os


class CPUManager:

    def collect(self):

        return {

            "processor": platform.processor(),

            "architecture": platform.machine(),

            "logical_cores": os.cpu_count(),

        }