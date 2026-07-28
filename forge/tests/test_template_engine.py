from forge.template_engine import TemplateEngine


def test_template_engine():

    engine = TemplateEngine()

    text = engine.render(
        "module.py.tpl",
        {
            "CLASS_NAME": "RiskEngine",
        },
    )

    assert "RiskEngine" in text