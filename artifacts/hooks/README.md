# Hooks (Templates)

These are example pre-commit hooks.

Notes:
- Git hooks are local by default; **CI enforcement is still required**.
- Provide both bash and PowerShell examples.

## Bash hook (macOS/Linux)

Copy `pre-commit` into `.git/hooks/pre-commit` and make it executable.

## PowerShell hook (Windows)

Option A (recommended): use `pre-commit` framework.

Option B: copy `pre-commit.ps1` somewhere and create `.git/hooks/pre-commit` that invokes it via `pwsh`.
