from forge.renderer import Renderer


def test_renderer_can_be_created():
    renderer = Renderer()

    assert renderer is not None


def test_renderer_has_render_method():
    renderer = Renderer()

    assert hasattr(renderer, "render")
    assert callable(renderer.render)


def test_renderer_returns_template():
    renderer = Renderer()

    template = "Hello Forge"

    result = renderer.render(template)

    assert result == template