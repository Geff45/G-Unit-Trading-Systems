from gunit.di import ServiceCollection
from gunit.modules import Module, ModuleBuilder, ModuleContext
from gunit.modules.trading_engine_module import TradingEngineModule


def test_trading_engine_module_exposes_canonical_identity():
    module = TradingEngineModule()

    assert isinstance(module, Module)
    assert module.name == "TradingEngine"
    assert module.version == "1.0.0"


def test_trading_engine_module_configuration_accepts_shared_context():
    services = ServiceCollection()
    context = ModuleContext(services)
    module = TradingEngineModule()

    module.configure(context)


def test_trading_engine_module_participates_in_lifecycle():
    services = ServiceCollection()
    context = ModuleContext(services)
    module = TradingEngineModule()

    module.configure(context)
    module.start(context)
    module.stop(context)


def test_trading_engine_module_can_be_registered_with_builder():
    module = TradingEngineModule()

    registry = (
        ModuleBuilder()
        .add(module)
        .build()
    )

    assert registry.modules == [module]


def test_trading_engine_module_configuration_uses_provided_context():
    services = ServiceCollection()
    context = ModuleContext(services)
    module = TradingEngineModule()

    result = module.configure(context)

    assert result is None
