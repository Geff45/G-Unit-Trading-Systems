from pprint import pprint

from kernel.hal.hal_manager import (
    HALManager,
)

manager = HALManager()

pprint(

    manager.collect()

)