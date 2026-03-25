[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)]
    [string]$SopRoot
)

$ErrorActionPreference = 'Stop'

function Read-Template {
    param(
        [Parameter(Mandatory = $true)]
        [string]$Path
    )

    if (-not (Test-Path -LiteralPath $Path)) {
        throw "Missing template file: $Path"
    }

    return [System.IO.File]::ReadAllText([System.IO.Path]::GetFullPath($Path))
}

function Write-Utf8NoBomFile {
    param(
        [Parameter(Mandatory = $true)]
        [string]$Path,
        [Parameter(Mandatory = $true)]
        [string]$Content
    )

    $utf8NoBom = New-Object System.Text.UTF8Encoding($false)
    [System.IO.File]::WriteAllText($Path, $Content, $utf8NoBom)
}

function Expand-Template {
    param(
        [Parameter(Mandatory = $true)]
        [string]$Template,
        [Parameter(Mandatory = $true)]
        [hashtable]$Variables
    )

    $expanded = $Template
    foreach ($key in $Variables.Keys) {
        $expanded = $expanded.Replace("{{${key}}}", [string]$Variables[$key])
    }

    return $expanded
}

$normalizedSopRoot = $SopRoot.Trim().Trim('"')
$resolvedSopRoot = [System.IO.Path]::GetFullPath($normalizedSopRoot)
$sopDirName = Split-Path -Leaf $resolvedSopRoot.TrimEnd('\', '/')
$projectRoot = Split-Path -Parent $resolvedSopRoot
$projectRootDrive = [System.IO.Path]::GetPathRoot($projectRoot)

if ([string]::IsNullOrWhiteSpace($projectRoot)) {
    throw 'Cannot determine host project root. Make sure ai_develop_sop is placed under the project root.'
}

if ($projectRoot.TrimEnd('\', '/') -eq $projectRootDrive.TrimEnd('\', '/')) {
    throw 'ai_sop_init must be run only after ai_develop_sop is injected under a real host-project directory. Do not run it from the SOP source repository root or directly under a drive root.'
}

$sopAgents = Join-Path $resolvedSopRoot 'AGENTS.md'
if (-not (Test-Path -LiteralPath $sopAgents)) {
    throw "Missing SOP entry file: $sopAgents"
}

$projectEntry = Join-Path $resolvedSopRoot 'project_entry.md'
if (-not (Test-Path -LiteralPath $projectEntry)) {
    throw "Missing injected-project entry file: $projectEntry"
}

$runtimeDir = Join-Path $resolvedSopRoot 'runtime'
$templatesDir = Join-Path $runtimeDir 'templates'

$projectAgentsTemplatePath = Join-Path $templatesDir 'project_root_AGENTS.template.md'
$projectReadmeTemplatePath = Join-Path $templatesDir 'project_root_README.template.md'
$entryStateTemplatePath = Join-Path $templatesDir 'entry_state.template.md'
$projectMountTemplatePath = Join-Path $templatesDir 'project_mount.template.md'
$projectCharterTemplatePath = Join-Path $templatesDir 'project_charter.template.md'
$currentTargetTemplatePath = Join-Path $templatesDir 'current_target.template.md'
$sessionBriefTemplatePath = Join-Path $templatesDir 'session_brief.template.md'

$generatedAt = Get-Date -Format 'yyyy-MM-ddTHH:mm:sszzz'
$variables = @{
    GENERATED_AT = $generatedAt
    SOP_DIR_NAME = $sopDirName
    HOST_PROJECT_NAME = (Split-Path -Leaf $projectRoot)
}

$projectAgentsContent = Expand-Template -Template (Read-Template -Path $projectAgentsTemplatePath) -Variables $variables
$projectReadmeContent = Expand-Template -Template (Read-Template -Path $projectReadmeTemplatePath) -Variables $variables
$entryStateContent = Expand-Template -Template (Read-Template -Path $entryStateTemplatePath) -Variables $variables
$projectMountContent = Expand-Template -Template (Read-Template -Path $projectMountTemplatePath) -Variables $variables
$projectCharterContent = Expand-Template -Template (Read-Template -Path $projectCharterTemplatePath) -Variables $variables
$currentTargetContent = Expand-Template -Template (Read-Template -Path $currentTargetTemplatePath) -Variables $variables
$sessionBriefContent = Expand-Template -Template (Read-Template -Path $sessionBriefTemplatePath) -Variables $variables

$projectAgentsPath = Join-Path $projectRoot 'AGENTS.md'
$projectReadmePath = Join-Path $projectRoot 'README.md'
$bootstrapMarker = 'bootstrap_generated_by_ai_develop_sop'

if (Test-Path -LiteralPath $projectAgentsPath) {
    $existingProjectAgents = [System.IO.File]::ReadAllText([System.IO.Path]::GetFullPath($projectAgentsPath))
    if ($existingProjectAgents -notmatch [System.Text.RegularExpressions.Regex]::Escape($bootstrapMarker)) {
        throw "Host project already contains a non-generated AGENTS.md: $projectAgentsPath"
    }
}

$generatedRuntimeMarker = 'generated_by_ai_develop_sop_runtime_init'

Write-Utf8NoBomFile -Path $projectAgentsPath -Content $projectAgentsContent

if (-not (Test-Path -LiteralPath $projectReadmePath)) {
    Write-Utf8NoBomFile -Path $projectReadmePath -Content $projectReadmeContent
    Write-Host "[OK] Host-project README bootstrap generated: $projectReadmePath"
}
else {
    Write-Host "[OK] Host-project README preserved: $projectReadmePath"
}

$entryStatePath = Join-Path $runtimeDir 'entry_state.md'
if (Test-Path -LiteralPath $entryStatePath) {
    $existingEntryState = [System.IO.File]::ReadAllText([System.IO.Path]::GetFullPath($entryStatePath))
    if ($existingEntryState -notmatch [System.Text.RegularExpressions.Regex]::Escape($generatedRuntimeMarker)) {
        throw "Runtime file is not init-generated and cannot be reset automatically: $entryStatePath"
    }
}
Write-Utf8NoBomFile -Path $entryStatePath -Content $entryStateContent

$projectMountPath = Join-Path $runtimeDir 'project_mount.md'
if (Test-Path -LiteralPath $projectMountPath) {
    $existingProjectMount = [System.IO.File]::ReadAllText([System.IO.Path]::GetFullPath($projectMountPath))
    if ($existingProjectMount -notmatch [System.Text.RegularExpressions.Regex]::Escape($generatedRuntimeMarker)) {
        throw "Runtime file is not init-generated and cannot be reset automatically: $projectMountPath"
    }
}
Write-Utf8NoBomFile -Path $projectMountPath -Content $projectMountContent

$projectCharterPath = Join-Path $runtimeDir 'project_charter.md'
if (Test-Path -LiteralPath $projectCharterPath) {
    $existingProjectCharter = [System.IO.File]::ReadAllText([System.IO.Path]::GetFullPath($projectCharterPath))
    if ($existingProjectCharter -notmatch [System.Text.RegularExpressions.Regex]::Escape($generatedRuntimeMarker)) {
        throw "Runtime file is not init-generated and cannot be reset automatically: $projectCharterPath"
    }
}
Write-Utf8NoBomFile -Path $projectCharterPath -Content $projectCharterContent

$currentTargetPath = Join-Path $runtimeDir 'current_target.md'
if (Test-Path -LiteralPath $currentTargetPath) {
    $existingCurrentTarget = [System.IO.File]::ReadAllText([System.IO.Path]::GetFullPath($currentTargetPath))
    if ($existingCurrentTarget -notmatch [System.Text.RegularExpressions.Regex]::Escape($generatedRuntimeMarker)) {
        throw "Runtime file is not init-generated and cannot be reset automatically: $currentTargetPath"
    }
}
Write-Utf8NoBomFile -Path $currentTargetPath -Content $currentTargetContent

$sessionBriefPath = Join-Path $runtimeDir 'session_brief.md'
if (Test-Path -LiteralPath $sessionBriefPath) {
    $existingSessionBrief = [System.IO.File]::ReadAllText([System.IO.Path]::GetFullPath($sessionBriefPath))
    if ($existingSessionBrief -notmatch [System.Text.RegularExpressions.Regex]::Escape($generatedRuntimeMarker)) {
        throw "Runtime file is not init-generated and cannot be reset automatically: $sessionBriefPath"
    }
}
Write-Utf8NoBomFile -Path $sessionBriefPath -Content $sessionBriefContent

Write-Host "[OK] Host-project bootstrap AGENTS generated: $projectAgentsPath"
Write-Host "[OK] Runtime entry_state reset: $entryStatePath"
Write-Host "[OK] Runtime project_mount reset: $projectMountPath"
Write-Host "[OK] Runtime project_charter reset: $projectCharterPath"
Write-Host "[OK] Runtime current_target reset: $currentTargetPath"
Write-Host "[OK] Runtime session_brief reset: $sessionBriefPath"
Write-Host '[INFO] Re-running ai_sop_init resets init-generated bootstrap/runtime files to the template state.'
Write-Host '[INFO] ai_sop_init does not reset ai_develop_sop/AGENTS.md itself; injected project type state is reset in runtime/entry_state.md.'
Write-Host '[INFO] Zero-touch initialization completed: the injected project is ready to enter the default common workflow immediately.'
