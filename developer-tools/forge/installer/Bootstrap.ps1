param(
    [switch]$Repair
)

$ProjectRoot = Resolve-Path "$PSScriptRoot\..\..\.."
$ForgeRoot   = Join-Path $ProjectRoot "developer-tools\forge"

Write-Host ""
Write-Host "==========================================" -ForegroundColor Cyan
Write-Host "      ATLAS FORGE BOOTSTRAP v1.0"
Write-Host "==========================================" -ForegroundColor Cyan
Write-Host ""

# ------------------------------------
# Folder Structure
# ------------------------------------

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
    "logs",
    "plugins",
    "reports",
    "templates",
    "tests",
    "installer"
)

foreach($folder in $Folders)
{
    $Path = Join-Path $ForgeRoot $folder

    if(!(Test-Path $Path))
    {
        New-Item -ItemType Directory -Path $Path | Out-Null
        Write-Host "[CREATED] $folder" -ForegroundColor Green
    }
    else
    {
        Write-Host "[ OK ] $folder"
    }
}

# ------------------------------------
# File Structure
# ------------------------------------

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
    "core\services\project_database_service.py"
)

foreach($file in $Files)
{
    $Path = Join-Path $ForgeRoot $file

    if(!(Test-Path $Path))
    {
        New-Item -ItemType File -Path $Path | Out-Null
        Write-Host "[CREATED] $file" -ForegroundColor Yellow
    }
    else
    {
        Write-Host "[ OK ] $file"
    }
}

# ------------------------------------
# Rename test -> tests
# ------------------------------------

$Old = Join-Path $ForgeRoot "test"
$New = Join-Path $ForgeRoot "tests"

if((Test-Path $Old) -and !(Test-Path $New))
{
    Rename-Item $Old "tests"
    Write-Host "[RENAMED] test -> tests" -ForegroundColor Magenta
}

Write-Host ""
Write-Host "==========================================" -ForegroundColor Cyan
Write-Host " Forge Bootstrap Complete"
Write-Host "==========================================" -ForegroundColor Cyan