# ==========================================================
# Atlas Forge Structure Manifest
# Version 3.0
# ==========================================================

$Structure = @{

    Engine = @(
        "developer-tools\forge\core\engine\__init__.py",
        "developer-tools\forge\core\engine\engine.py",
        "developer-tools\forge\core\engine\events.py",
        "developer-tools\forge\core\engine\lifecycle.py",
        "developer-tools\forge\core\engine\service_container.py"
    )

    Services = @(
        "developer-tools\forge\core\services\base\base_service.py",
        "developer-tools\forge\core\services\logger\logger_service.py",
        "developer-tools\forge\core\services\context\context_service.py",
        "developer-tools\forge\core\services\settings\settings_service.py",
        "developer-tools\forge\core\services\database\project_database_service.py"
    )

    Managers = @(
        "developer-tools\forge\core\services\manager\service_manager.py"
    )

    Database = @(
        "developer-tools\forge\database\project.json",
        "developer-tools\forge\database\modules.json",
        "developer-tools\forge\database\dependencies.json",
        "developer-tools\forge\database\snapshots.json",
        "developer-tools\forge\database\history.json"
    )
}