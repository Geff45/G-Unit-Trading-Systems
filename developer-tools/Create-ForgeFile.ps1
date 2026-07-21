<#
==============================================================
 Atlas Forge File Creator
 Version: 1.0.0
==============================================================

Creates a file and any missing parent directories.

Example:

.\developer-tools\Create-ForgeFile.ps1 `
    -Path "developer-tools\forge\core\services\service_state.py"

#>

param(

    [Parameter(Mandatory = $true)]
    [string]$Path

)

$ProjectRoot = "C:\G-Unit-Trading-Systems"

$FullPath = Join-Path $ProjectRoot $Path

$Directory = Split-Path $FullPath -Parent

if (!(Test-Path $Directory))
{
    New-Item `
        -ItemType Directory `
        -Force `
        -Path $Directory | Out-Null

    Write-Host "[NEW] Directory : $Directory" -ForegroundColor Green
}

if (!(Test-Path $FullPath))
{
    New-Item `
        -ItemType File `
        -Force `
        -Path $FullPath | Out-Null

    Write-Host "[NEW] File : $Path" -ForegroundColor Yellow
}
else
{
    Write-Host "[ OK ] Already exists : $Path" -ForegroundColor Cyan
}