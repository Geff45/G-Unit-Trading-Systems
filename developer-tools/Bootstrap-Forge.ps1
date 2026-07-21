# ============================================================
# Atlas Forge Bootstrap Installer
# Version: 1.0.0
# G-Unit Trading Systems
# ============================================================

$ProjectRoot = "C:\G-Unit-Trading-Systems"

Write-Host ""
Write-Host "===============================================" -ForegroundColor Cyan
Write-Host "         ATLAS FORGE BOOTSTRAP INSTALLER"
Write-Host "                Version 1.0.0"
Write-Host "===============================================" -ForegroundColor Cyan
Write-Host ""

# ------------------------------------------------------------
# Folders
# ------------------------------------------------------------

$Folders = @(

"developer-tools",

"developer-tools\forge",

"developer-tools\forge\cli",
"developer-tools\forge\config",
"developer-tools\forge\cache",
"developer-tools\forge\logs",
"developer-tools\forge\plugins",
"developer-tools\forge\templates",
"developer-tools\forge\tests",
"developer-tools\forge\utils",

"developer-tools\forge\core",
"developer-tools\forge\core\engine",
"developer-tools\forge\core\services",

"developer-tools\forge\core\services\logger",
"developer-tools\forge\core\services\context",
"developer-tools\forge\core\services\settings",
"developer-tools\forge\core\services\database",

"developer-tools\forge\core\models"

)

# ------------------------------------------------------------
# Files
# ------------------------------------------------------------

$Files = @(

# Root

"developer-tools\forge\README.md",
"developer-tools\forge\forge.py",

# Config

"developer-tools\forge\config\forge.json",

# Engine

"developer-tools\forge\core\engine\__init__.py",
"developer-tools\forge\core\engine\engine.py",
"developer-tools\forge\core\engine\service_container.py",
"developer-tools\forge\core\engine\lifecycle.py",
"developer-tools\forge\core\engine\events.py",

# Services

"developer-tools\forge\core\services\__init__.py",

"developer-tools\forge\core\services\logger\__init__.py",
"developer-tools\forge\core\services\logger\logger_service.py",

"developer-tools\forge\core\services\context\__init__.py",
"developer-tools\forge\core\services\context\context_service.py",

"developer-tools\forge\core\services\settings\__init__.py",
"developer-tools\forge\core\services\settings\settings_service.py",

"developer-tools\forge\core\services\database\__init__.py",
"developer-tools\forge\core\services\database\project_database_service.py",

# Models

"developer-tools\forge\core\models\__init__.py"

)

# ------------------------------------------------------------
# Create folders
# ------------------------------------------------------------

Write-Host "Creating folders..." -ForegroundColor Yellow
Write-Host ""

foreach ($Folder in $Folders)
{
    $Path = Join-Path $ProjectRoot $Folder

    if (Test-Path $Path)
    {
        Write-Host "[ OK ] Folder exists : $Folder"
    }
    else
    {
        New-Item -ItemType Directory -Path $Path -Force | Out-Null
        Write-Host "[NEW] Folder created : $Folder" -ForegroundColor Green
    }
}

Write-Host ""

# ------------------------------------------------------------
# Create files
# ------------------------------------------------------------

Write-Host "Creating files..." -ForegroundColor Yellow
Write-Host ""

foreach ($File in $Files)
{
    $Path = Join-Path $ProjectRoot $File

    if (Test-Path $Path)
    {
        Write-Host "[ OK ] File exists : $File"
    }
    else
    {
        New-Item -ItemType File -Path $Path -Force | Out-Null
        Write-Host "[NEW] File created : $File" -ForegroundColor Cyan
    }
}

Write-Host ""
Write-Host "===============================================" -ForegroundColor Green
Write-Host " Atlas Forge Bootstrap Completed Successfully!"
Write-Host "===============================================" -ForegroundColor Green
Write-Host ""