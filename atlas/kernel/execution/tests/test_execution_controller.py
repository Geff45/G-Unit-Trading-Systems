from kernel.execution.controller import (
    ExecutionController,
)

from kernel.execution.controller_descriptor import (
    ControllerDescriptor,
)


controller = ExecutionController(

    ControllerDescriptor(

        controller_id="atlas",

        name="Atlas Execution",

        version="1.0.0",
    )
)

controller.initialize()

controller.start()

print()

print(controller.descriptor.state)

controller.stop()

print()

print(controller.descriptor.state)