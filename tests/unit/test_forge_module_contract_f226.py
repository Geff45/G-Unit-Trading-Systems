from pathlib import Path

from forge.generators import ModuleGenerator


def test_generated_module_implements_atlas_module_contract(tmp_path):
    generator = ModuleGenerator(tmp_path)

    result = generator.generate(
        class_name="MarketDataModule",
        module_name="market_data_module",
    )

    module = Path(result["module"])
    content = module.read_text(encoding="utf-8")

    assert "from gunit.modules import Module, ModuleContext" in content
    assert "class MarketDataModule(Module):" in content
    assert 'return "MarketDataModule"' in content
    assert 'return "1.0.0"' in content
    assert "def configure(self, context: ModuleContext) -> None:" in content
    assert "def start(self, context: ModuleContext) -> None:" in content
    assert "def stop(self, context: ModuleContext) -> None:" in content


def test_generated_module_test_validates_atlas_module_contract(tmp_path):
    generator = ModuleGenerator(tmp_path)

    result = generator.generate(
        class_name="MarketDataModule",
        module_name="market_data_module",
    )

    test = Path(result["test"])
    content = test.read_text(encoding="utf-8")

    assert "from gunit.modules import Module, ModuleContext" in content
    assert "from gunit.modules.market_data_module import MarketDataModule" in content
    assert "isinstance(module, Module)" in content
    assert 'module.name == "MarketDataModule"' in content
    assert 'module.version == "1.0.0"' in content
    assert "module.configure(context)" in content
    assert "module.start(context)" in content
    assert "module.stop(context)" in content
