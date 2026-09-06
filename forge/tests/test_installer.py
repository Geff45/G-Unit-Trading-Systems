from forge.installer import InstallerEngine


def test_installer_engine_can_be_created():
    installer = InstallerEngine()

    assert installer is not None


def test_installer_engine_has_run_method():
    installer = InstallerEngine()

    assert hasattr(installer, "run")
    assert callable(installer.run)


def test_installer_run_returns_none():
    installer = InstallerEngine()

    result = installer.run()

    assert result is None