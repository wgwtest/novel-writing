[CmdletBinding()]
param(
    [string]$CodexRoot
)

$ErrorActionPreference = 'Stop'

$repositoryRoot = Split-Path -Parent $PSScriptRoot
$sourceDirectory = [System.IO.Path]::GetFullPath((Join-Path $repositoryRoot 'novel-writing'))

if (-not (Test-Path -LiteralPath $sourceDirectory -PathType Container)) {
    throw "Installable package directory not found: $sourceDirectory"
}

$resolvedCodexRoot = $CodexRoot
if ([string]::IsNullOrWhiteSpace($resolvedCodexRoot)) {
    if (-not [string]::IsNullOrWhiteSpace($env:CODEX_HOME)) {
        $resolvedCodexRoot = $env:CODEX_HOME
    }
    else {
        $resolvedCodexRoot = Join-Path $env:USERPROFILE '.codex'
    }
}

$resolvedCodexRoot = [System.IO.Path]::GetFullPath($resolvedCodexRoot)
$skillsDirectory = Join-Path $resolvedCodexRoot 'skills'
$targetDirectory = Join-Path $skillsDirectory 'novel-writing'

New-Item -ItemType Directory -Path $skillsDirectory -Force | Out-Null

$existingItem = Get-Item -LiteralPath $targetDirectory -Force -ErrorAction SilentlyContinue
if ($null -ne $existingItem) {
    $existingTargets = @($existingItem.Target) | Where-Object { -not [string]::IsNullOrWhiteSpace($_) }
    if ($existingItem.LinkType -and $existingTargets.Count -gt 0) {
        [string]$existingTargetText = $existingTargets | Select-Object -First 1
        $existingTarget = [System.IO.Path]::GetFullPath($existingTargetText)
        if ($existingTarget -eq $sourceDirectory) {
            Write-Host "Local development link is already correct: $targetDirectory -> $sourceDirectory"
            exit 0
        }
    }

    $timestamp = Get-Date -Format 'yyyyMMdd-HHmmss'
    $backupDirectory = "$targetDirectory.backup-$timestamp"
    Move-Item -LiteralPath $targetDirectory -Destination $backupDirectory
    Write-Host "Backed up existing local installation: $backupDirectory"
}

New-Item -ItemType Junction -Path $targetDirectory -Target $sourceDirectory | Out-Null

$installedItem = Get-Item -LiteralPath $targetDirectory -Force
if (-not $installedItem.LinkType) {
    throw "Local development link was not created: $targetDirectory"
}

Write-Host "Installed local development link: $targetDirectory -> $sourceDirectory"
