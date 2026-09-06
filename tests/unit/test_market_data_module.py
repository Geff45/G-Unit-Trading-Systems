from gunit.modules import Module, ModuleContext
from gunit.di import ServiceCollection

from gunit.modules.market_data_module import MarketDataModule


def test_market_data_module():
    services = ServiceCollection()
    context = ModuleContext(services)
    module = MarketDataModule()

    assert isinstance(module, Module)
    assert module.name == "MarketDataModule"
    assert module.version == "1.0.0"

    module.configure(context)
    module.start(context)
    module.stop(context)
