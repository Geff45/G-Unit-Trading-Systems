# ===============================================================
# Atlas Forge Structure Updater
# Version: 2.0.0
# G-Unit Trading Systems
# ===============================================================

$ProjectRoot = "C:\G-Unit-Trading-Systems"

$Folders = @(

# Root
"developer-tools",
"developer-tools\forge",

# Core
"developer-tools\forge\core",
"developer-tools\forge\core\engine",
"developer-tools\forge\core\models",
"developer-tools\forge\core\services",

# Services
"developer-tools\forge\core\services\logger",
"developer-tools\forge\core\services\context",
"developer-tools\forge\core\services\settings",
"developer-tools\forge\core\services\database",

# Configuration
"developer-tools\forge\config",

# Database
"developer-tools\forge\database",

# Runtime
"developer-tools\forge\cache",
"developer-tools\forge\logs",
"developer-tools\forge\reports",
"developer-tools\forge\workspace",

# Extensions
"developer-tools\forge\plugins",
"developer-tools\forge\templates",
"developer-tools\forge\tests",
"developer-tools\forge\utils",

# Metadata
"developer-tools\forge\metadata"
)

$Files = @(

# -------------------------------------------------
# Root
# -------------------------------------------------

"developer-tools\forge\forge.py",
"developer-tools\forge\README.md",
"developer-tools\forge\VERSION",

# -------------------------------------------------
# Engine
# -------------------------------------------------

"developer-tools\forge\core\engine\__init__.py",
"developer-tools\forge\core\engine\engine.py",
"developer-tools\forge\core\engine\service_container.py",
"developer-tools\forge\core\engine\lifecycle.py",
"developer-tools\forge\core\engine\events.py",

# -------------------------------------------------
# Models
# -------------------------------------------------

"developer-tools\forge\core\models\__init__.py",

# -------------------------------------------------
# Services
# -------------------------------------------------

"developer-tools\forge\core\services\__init__.py",

"developer-tools\forge\core\services\logger\__init__.py",
"developer-tools\forge\core\services\logger\logger_service.py",

"developer-tools\forge\core\services\context\__init__.py",
"developer-tools\forge\core\services\context\context_service.py",

"developer-tools\forge\core\services\settings\__init__.py",
"developer-tools\forge\core\services\settings\settings_service.py",

"developer-tools\forge\core\services\database\__init__.py",
"developer-tools\forge\core\services\database\project_database_service.py",

# -------------------------------------------------
# Config
# -------------------------------------------------

"developer-tools\forge\config\forge.json",
"developer-tools\forge\config\defaults.json",

# -------------------------------------------------
# Database
# -------------------------------------------------

"developer-tools\forge\database\project.json",
"developer-tools\forge\database\modules.json",
"developer-tools\forge\database\dependencies.json",
"developer-tools\forge\database\snapshots.json",
"developer-tools\forge\database\history.json"
)

$CreatedFolders = 0
$CreatedFiles = 0

Write-Host ""
Write-Host "===================================================" -ForegroundColor Cyan
Write-Host "        Atlas Forge Structure Updater v2.0"
Write-Host "===================================================" -ForegroundColor Cyan
Write-Host ""

# -------------------------------------------------
# Create folders
# -------------------------------------------------

foreach ($Folder in $Folders)
{
    $Path = Join-Path $ProjectRoot $Folder

    if (Test-Path $Path)
    {
        Write-Host "[ OK ] Folder : $Folder"
    }
    else
    {
        New-Item -ItemType Directory -Force -Path $Path | Out-Null
        Write-Host "[NEW] Folder : $Folder" -ForegroundColor Green
        $CreatedFolders++
    }
}

Write-Host ""

# -------------------------------------------------
# Create files
# -------------------------------------------------

foreach ($File in $Files)
{
    $Path = Join-Path $ProjectRoot $File

    if (Test-Path $Path)
    {
        Write-Host "[ OK ] File : $File"
    }
    else
    {
        New-Item -ItemType File -Force -Path $Path | Out-Null
        Write-Host "[NEW] File : $File" -ForegroundColor Yellow
        $CreatedFiles++
    }
}

Write-Host ""
Write-Host "===================================================" -ForegroundColor Green
Write-Host "Atlas Forge Update Complete"
Write-Host "===================================================" -ForegroundColor Green
Write-Host ""

Write-Host ("Folders created : {0}" -f $CreatedFolders)
Write-Host ("Files created   : {0}" -f $CreatedFiles)

Write-Host ""
Write-Host "Forge structure is up to date." -ForegroundColor Cyan
Write-Host ""