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
    'references/cognition-layers-and-language.md',
    'references/planning.md',
    'references/realism-constraints.md',
    'references/revision-checklist.md',
    'references/scene-causality-and-agency.md',
    'references/scene-and-structure.md',
    'references/story-outline-and-causal-summary.md',
    'references/style-fidelity.md',
    'scripts/check_manuscript_text.py'
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
    '(?i)[A-Z]:[\\/]',
    '(?i)/(?:Users|home)/[^/\s]+/',
    '(?i)/root/',
    '(?i)/(?:tmp|workspace|opt|var|etc|mnt|srv)/',
    '\\\\[^\\\s]+\\[^\\\s]+\\',
    'file://'
)

$pathLeakFixtures = @(
    'D:\Projects\sample\file.txt',
    'C:\Temp\sample.txt',
    '/Users/name/project/file.txt',
    '/home/name/project/file.txt',
    '/root/project/file.txt',
    '/tmp/manuscript.txt',
    '/workspace/project/file.txt',
    '/opt/tool/file.txt',
    '/var/data/file.txt',
    '\\server\share\file.txt',
    'file:///tmp/sample.txt'
)

foreach ($fixture in $pathLeakFixtures) {
    $matched = $forbiddenPatterns | Where-Object { $fixture -match $_ }
    if (-not $matched) {
        throw "Local-path hygiene pattern missed validation fixture: $fixture"
    }
}

$forbiddenProjectTerms = @(
    (-join [char[]]@(0x300A, 0x9752, 0x4E91, 0x5F55, 0x300B)),
    (-join [char[]]@(0x5927, 0x4ED9, 0x7960)),
    (-join [char[]]@(0x5343, 0x65A4, 0x9635)),
    (-join [char[]]@(0x4E94, 0x8272, 0x7B26)),
    (-join [char[]]@(0x6267, 0x6CD5, 0x4ED9, 0x59D1))
)

foreach ($publicFile in $publicFiles) {
    $content = Get-Content -LiteralPath $publicFile.FullName -Raw -Encoding UTF8
    foreach ($pattern in $forbiddenPatterns) {
        if ($content -match $pattern) {
            $relativeName = $publicFile.FullName.Substring($packageRoot.Length).TrimStart('\')
            throw "Public package contains a local path in $relativeName (pattern: $pattern)"
        }
    }
    foreach ($term in $forbiddenProjectTerms) {
        if ($content.Contains($term)) {
            $relativeName = $publicFile.FullName.Substring($packageRoot.Length).TrimStart('\')
            throw "Public package contains project-specific material in $relativeName (term: $term)"
        }
    }
}

$checker = Join-Path $packageRoot 'scripts/check_manuscript_text.py'
& python -c "import ast, pathlib, sys; p = pathlib.Path(sys.argv[1]); ast.parse(p.read_text(encoding='utf-8'), filename=str(p))" $checker
if ($LASTEXITCODE -ne 0) {
    throw 'Manuscript checker syntax validation failed.'
}

& python $checker --help | Out-Null
if ($LASTEXITCODE -ne 0) {
    throw 'Manuscript checker --help failed.'
}

& python -B -m unittest discover -s (Join-Path $repositoryRoot 'tests') -p 'test_*.py'
if ($LASTEXITCODE -ne 0) {
    throw 'Repository tests failed.'
}

Write-Host "Package validation PASS: $($publicFiles.Count) files checked."
