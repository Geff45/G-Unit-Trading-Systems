from boot.boot_manager import BootManager
from boot.system_report import SystemReport

boot = BootManager()

boot.boot()

print()

print(SystemReport().report())