[CmdletBinding()]
param()

$ErrorActionPreference = 'Stop'

$repositoryRoot = Split-Path -Parent $PSScriptRoot
$packageRoot = Join-Path $repositoryRoot 'novel-writing'
$skillFile = Join-Path $packageRoot 'SKILL.md'

$requiredFiles = @(
    'SKILL.md',
    'agents/openai.yaml',
    'references/character-introductions.md',
    'references/planning.md',
    'references/realism-constraints.md',
    'references/revision-checklist.md',
    'references/scene-and-structure.md',
    'references/style-fidelity.md'
)

foreach ($relativePath in $requiredFiles) {
    $candidate = Join-Path $packageRoot $relativePath
    if (-not (Test-Path -LiteralPath $candidate -PathType Leaf)) {
        throw "Required package file is missing: $relativePath"
    }
}

$skillText = Get-Content -LiteralPath $skillFile -Raw -Encoding UTF8
if ($skillText -notmatch '(?s)^---\r?\nname:\s*novel-writing\r?\ndescription:\s*.+?\r?\n---\r?\n') {
    throw 'SKILL.md front matter is missing or malformed.'
}

foreach ($relativePath in $requiredFiles | Where-Object { $_ -like 'references/*' }) {
    $normalizedReference = $relativePath.Replace('\', '/')
    if (-not $skillText.Contains($normalizedReference)) {
        throw "SKILL.md does not reference required file: $normalizedReference"
    }
}

$publicFiles = Get-ChildItem -LiteralPath $packageRoot -Recurse -File -Force
$forbiddenPatterns = @(
    '[A-Za-z]:\\Users\\',
    '[A-Za-z]:\\CodexWorkSpace\\',
    '/home/[^/\s]+/',
    'file://'
)

foreach ($publicFile in $publicFiles) {
    $content = Get-Content -LiteralPath $publicFile.FullName -Raw -Encoding UTF8
    foreach ($pattern in $forbiddenPatterns) {
        if ($content -match $pattern) {
            $relativeName = $publicFile.FullName.Substring($packageRoot.Length).TrimStart('\')
            throw "Public package contains a local path in $relativeName (pattern: $pattern)"
        }
    }
}

Write-Host "Package validation PASS: $($publicFiles.Count) files checked."
