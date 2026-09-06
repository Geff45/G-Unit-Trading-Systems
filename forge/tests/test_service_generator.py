from pathlib import Path

from forge.generators import ServiceGenerator


def test_service_generator(tmp_path):

    generator = ServiceGenerator(tmp_path)

    result = generator.generate(
        class_name="MarketService",
        module_name="market_service",
    )

    service = Path(result["service"])
    test = Path(result["test"])

    assert service.exists()
    assert test.exists()

    assert "MarketService" in service.read_text(
        encoding="utf-8"
    )


def test_service_generator_creates_valid_test(tmp_path):

    generator = ServiceGenerator(tmp_path)

    result = generator.generate(
        class_name="RiskService",
        module_name="risk_service",
    )

    test = Path(result["test"])

    assert test.exists()

    content = test.read_text(
        encoding="utf-8"
    )

    assert "RiskService" in content
    assert "risk_service" in content