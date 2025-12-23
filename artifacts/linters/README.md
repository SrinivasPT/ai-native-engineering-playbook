# Linters (Templates)

## Architecture linter

- File: [arch_linter.py](arch_linter.py)
- Language: Python example

What it enforces:
- Import boundaries (e.g., `src.features` must not import `src.infra`).

How to run:
- `python artifacts/linters/arch_linter.py --root src`

How to integrate:
- Pre-commit hook: run it on staged changes.
- CI: run it on every PR.

Adaptation notes:
- For TypeScript/JS, implement the same rule using your AST toolchain or ESLint rules.
- For Java/Kotlin, use build plugins or static analysis.
