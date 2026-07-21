# ==========================================================
# Atlas Forge
# Service Manager Bootstrap
# Version: 1.0.0
# ==========================================================

$ProjectRoot = "C:\G-Unit-Trading-Systems"

$Folders = @(
    "developer-tools\forge\core\services\manager"
)

$Files = @(
    "developer-tools\forge\core\services\manager\__init__.py",
    "developer-tools\forge\core\services\manager\service_manager.py"
)

$CreatedFolders = 0
$CreatedFiles = 0

Write-Host ""
Write-Host "===============================================" -ForegroundColor Cyan
Write-Host "     Atlas Forge - Service Manager Setup"
Write-Host "===============================================" -ForegroundColor Cyan
Write-Host ""

foreach ($Folder in $Folders)
{
    $Path = Join-Path $ProjectRoot $Folder

    if (!(Test-Path $Path))
    {
        New-Item -ItemType Directory -Force -Path $Path | Out-Null
        Write-Host "[NEW] Folder : $Folder" -ForegroundColor Green
        $CreatedFolders++
    }
    else
    {
        Write-Host "[ OK ] Folder : $Folder"
    }
}

Write-Host ""

foreach ($File in $Files)
{
    $Path = Join-Path $ProjectRoot $File

    if (!(Test-Path $Path))
    {
        New-Item -ItemType File -Force -Path $Path | Out-Null
        Write-Host "[NEW] File : $File" -ForegroundColor Yellow
        $CreatedFiles++
    }
    else
    {
        Write-Host "[ OK ] File : $File"
    }
}

Write-Host ""
Write-Host "===============================================" -ForegroundColor Green
Write-Host "Service Manager structure ready."
Write-Host "===============================================" -ForegroundColor Green
Write-Host ""
Write-Host "Folders Created : $CreatedFolders"
Write-Host "Files Created   : $CreatedFiles"
Write-Host ""