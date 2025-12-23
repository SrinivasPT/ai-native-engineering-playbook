Param(
  [string]$RepoRoot = (Get-Location).Path
)

$ErrorActionPreference = 'Stop'
Set-Location $RepoRoot

Write-Host "pre-commit: running checks..."

# Filename lint (requires ls-lint installed)
$lsLint = Get-Command ls-lint -ErrorAction SilentlyContinue
if ($null -ne $lsLint) {
  & ls-lint
} else {
  Write-Host "pre-commit: ls-lint not installed; skipping"
}

# Architecture linter (Python example)
$python = Get-Command python -ErrorAction SilentlyContinue
if ($null -ne $python -and (Test-Path "artifacts/linters/arch_linter.py")) {
  & python artifacts/linters/arch_linter.py --root src
} else {
  Write-Host "pre-commit: arch_linter not runnable; skipping"
}

Write-Host "pre-commit: OK"
