param([Parameter(Mandatory=$true)][string]$Baseline, [string]$ChangeNote = '')
$ErrorActionPreference = 'Stop'
$taskRoot = Split-Path $PSScriptRoot -Parent
$guardArgs = @("$PSScriptRoot/check_integrations.py", '--root', $taskRoot, '--config', "$taskRoot/config/integrations.json", '--baseline', $Baseline)
if ($ChangeNote) { $guardArgs += @('--change-note', $ChangeNote) }
python @guardArgs
if ($LASTEXITCODE -ne 0) { throw 'Integration release gate failed' }
git -C $taskRoot diff --check
if ($LASTEXITCODE -ne 0) { throw 'Diff validation failed' }
