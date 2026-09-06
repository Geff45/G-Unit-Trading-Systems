import json

from forge.manifest import load_manifest, save_manifest


def test_load_manifest_returns_default_when_missing(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)

    manifest = load_manifest()

    assert manifest == {
        "version": "0.1.0",
        "installed_phases": [],
    }


def test_save_and_load_manifest(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)

    data = {
        "version": "0.1.0",
        "installed_phases": ["F203", "F204"],
    }

    save_manifest(data)

    manifest_file = tmp_path / "forge_manifest.json"

    assert manifest_file.exists()

    loaded = load_manifest()

    assert loaded == data


def test_saved_manifest_is_valid_json(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)

    data = {
        "version": "0.1.0",
        "installed_phases": ["F203"],
    }

    save_manifest(data)

    manifest_file = tmp_path / "forge_manifest.json"

    parsed = json.loads(
        manifest_file.read_text(encoding="utf-8")
    )

    assert parsed == data