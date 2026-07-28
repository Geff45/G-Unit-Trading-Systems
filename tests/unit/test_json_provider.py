import json

from gunit.configuration import JsonProvider


def test_json_provider(tmp_path):
    data = {"name": "G-Unit"}

    file = tmp_path / "config.json"

    file.write_text(json.dumps(data), encoding="utf-8")

    provider = JsonProvider()

    assert provider.load_file(file)["name"] == "G-Unit"
