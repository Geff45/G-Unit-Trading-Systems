from pathlib import Path

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