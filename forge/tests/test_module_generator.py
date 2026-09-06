from pathlib import Path

import pytest

from forge.generators import ModuleGenerator


def test_module_generator(tmp_path):

    generator = ModuleGenerator(tmp_path)

    result = generator.generate(
        class_name="RiskEngine",
        module_name="risk_engine",
    )

    module = Path(result["module"])
    test = Path(result["test"])

    assert module.exists()
    assert test.exists()

    assert "RiskEngine" in module.read_text(
        encoding="utf-8"
    )


def test_module_generator_creates_valid_test(tmp_path):

    generator = ModuleGenerator(tmp_path)

    result = generator.generate(
        class_name="RiskEngine",
        module_name="risk_engine",
    )

    test = Path(result["test"])

    content = test.read_text(
        encoding="utf-8"
    )

    assert "from gunit.modules.risk_engine import RiskEngine" in content
    assert "def test_risk_engine():" in content
    assert "RiskEngine()" in content


@pytest.mark.parametrize(
    "class_name",
    [
        "",
        "123Engine",
        "Trade Engine",
        "trade-engine",
    ],
)
def test_module_generator_rejects_invalid_class_name(
    tmp_path,
    class_name,
):

    generator = ModuleGenerator(tmp_path)

    with pytest.raises(ValueError):
        generator.generate(
            class_name=class_name,
            module_name="trade_engine",
        )


@pytest.mark.parametrize(
    "module_name",
    [
        "",
        "123engine",
        "trade engine",
        "trade-engine",
    ],
)
def test_module_generator_rejects_invalid_module_name(
    tmp_path,
    module_name,
):

    generator = ModuleGenerator(tmp_path)

    with pytest.raises(ValueError):
        generator.generate(
            class_name="TradeEngine",
            module_name=module_name,
        )