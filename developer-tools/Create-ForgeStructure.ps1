# ============================================================
# ATLAS Forge Bootstrap Creator
# Version : 1.0.0
# Project : G-Unit Trading Systems
# ============================================================

$ProjectRoot = "C:\G-Unit-Trading-Systems"
$ForgeRoot   = Join-Path $ProjectRoot "developer-tools\forge"

Write-Host ""
Write-Host "==============================================" -ForegroundColor Cyan
Write-Host "      ATLAS FORGE STRUCTURE GENERATOR"
Write-Host "==============================================" -ForegroundColor Cyan
Write-Host ""

# ------------------------------------------------------------
# Folder List
# ------------------------------------------------------------

$Folders = @(
    "cache",
    "cli",
    "commands",
    "config",
    "core",
    "core\engine",
    "core\services",
    "database",
    "docs",
    "installer",
    "logs",
    "plugins",
    "reports",
    "templates",
    "tests"
)

foreach($Folder in $Folders)
{
    $Path = Join-Path $ForgeRoot $Folder

    if(Test-Path $Path)
    {
        Write-Host "[ OK ] Folder exists : $Folder"
    }
    else
    {
        New-Item -ItemType Directory -Path $Path -Force | Out-Null
        Write-Host "[CREATED] Folder : $Folder" -ForegroundColor Green
    }
}

# ------------------------------------------------------------
# File List
# ------------------------------------------------------------

$Files = @(
    "cli\Forge.ps1",

    "config\forge.json",

    "database\project.json",
    "database\modules.json",
    "database\dependencies.json",
    "database\snapshots.json",

    "core\engine\engine.py",

    "core\services\context_service.py",
    "core\services\logger_service.py",
    "core\services\settings_service.py",
    "core\services\project_database_service.py",

    "installer\Bootstrap.ps1"
)

foreach($File in $Files)
{
    $Path = Join-Path $ForgeRoot $File

    if(Test-Path $Path)
    {
        Write-Host "[ OK ] File exists : $File"
    }
    else
    {
        New-Item -ItemType File -Path $Path -Force | Out-Null
        Write-Host "[CREATED] File : $File" -ForegroundColor Yellow
    }
}

# ------------------------------------------------------------
# Rename test -> tests
# ------------------------------------------------------------

$Old = Join-Path $ForgeRoot "test"
$New = Join-Path $ForgeRoot "tests"

if(Test-Path $Old)
{
    if(!(Test-Path $New))
    {
        Rename-Item $Old "tests"
        Write-Host "[RENAMED] test -> tests" -ForegroundColor Magenta
    }
    else
    {
        Remove-Item $Old -Force -Recurse
        Write-Host "[REMOVED] Duplicate 'test' folder" -ForegroundColor Magenta
    }
}

Write-Host ""
Write-Host "==============================================" -ForegroundColor Green
Write-Host " ATLAS Forge Structure Ready"
Write-Host "==============================================" -ForegroundColor Green