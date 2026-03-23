[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)]
    [string]$AgentsFile
)

if (-not (Test-Path -LiteralPath $AgentsFile)) {
    Write-Host "[ERROR] 未找到 AGENTS.md: $AgentsFile"
    exit 1
}

$path = [System.IO.Path]::GetFullPath($AgentsFile)
$content = [System.IO.File]::ReadAllText($path)
$pattern = '(?ms)(## 3\. 当前项目入口配置\s*\r?\n)(.*?)(\r?\n---)'

$updated = [System.Text.RegularExpressions.Regex]::Replace(
    $content,
    $pattern,
    {
        param($match)

        $body = $match.Groups[2].Value
        $newBody = [System.Text.RegularExpressions.Regex]::Replace(
            $body,
            '(?m)^- `([^`]+)`: `.*?`$',
            '- `$1`: `None`'
        )

        return $match.Groups[1].Value + $newBody + $match.Groups[3].Value
    }
)

if ($updated -eq $content) {
    Write-Host '[INFO] 未发现可重置的项目入口字段，AGENTS.md 未修改。'
    exit 2
}

$utf8NoBom = New-Object System.Text.UTF8Encoding($false)
[System.IO.File]::WriteAllText($path, $updated, $utf8NoBom)
Write-Host '[OK] 已将 AGENTS.md 还原到初始 SOP 入口状态。'
