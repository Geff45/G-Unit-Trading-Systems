param(
    [string]$Command="help"
)

$Bootstrap = Join-Path $PSScriptRoot "..\installer\Bootstrap.ps1"

switch($Command)
{
    "init"
    {
        & $Bootstrap
    }

    default
    {
        Write-Host ""
        Write-Host "ATLAS Forge"
        Write-Host ""
        Write-Host "Commands:"
        Write-Host "  init"
    }
}