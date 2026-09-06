from gunit.modules import Module, ModuleContext
from gunit.di import ServiceCollection

from gunit.modules.{{MODULE_NAME}} import {{CLASS_NAME}}


def test_{{MODULE_NAME}}():
    services = ServiceCollection()
    context = ModuleContext(services)
    module = {{CLASS_NAME}}()

    assert isinstance(module, Module)
    assert module.name == "{{CLASS_NAME}}"
    assert module.version == "1.0.0"

    module.configure(context)
    module.start(context)
    module.stop(context)
