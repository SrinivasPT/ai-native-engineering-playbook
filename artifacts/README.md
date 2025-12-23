# Sample Artifacts (Working Templates)

These files are copy‑paste templates that implement the playbook concepts in a real repository.

How to use:
1. Copy the artifact into the root of your repo (or into the path indicated).
2. Replace placeholders like `<your-team>`, `<service>`, `<red-zone>`.
3. Wire the linters/hooks/CI into your actual toolchain.

## Index

- [Repository Cognitive Map](MAP.md) — A curated architecture map for agents and humans.
- [Forbidden Patterns](FORBIDDEN.md) — Negative space: what not to do.
- [DOs](DOs.md) — Positive guidance: what to do.
- [Copilot / Agent Instructions](copilot-instructions.md) — A single source of truth for agent behavior.
- [Personas](personas/) — Builder/Auditor/Conventions‑enforcer prompt templates.
- [Decision Journal Template](decisions/000_template.md) — ADR‑lite template.
- [Intent Header Template](intent_headers/intent_header_template.md) — Copy‑paste intent block for critical code.
- [Filename Lint (ls-lint)](ls-lint/.ls-lint.yml) — Enforce deterministic naming.
- [Architecture Linter](linters/arch_linter.py) — Enforce import boundaries (“architecture as code”).
- [Hooks](hooks/) — Pre-commit hooks (bash + PowerShell).
- [CI](ci/) — GitHub Actions workflow that runs the checks.
- [AI-Readable Test Failures](testing/ai_readable_test_failures.md) — Working examples.
- [Logging Schema Example](logging/event.schema.json) — Schema‑stable telemetry example.
- [CODEOWNERS Example](CODEOWNERS) — Review gates for red zones.

## Recommended Minimal Setup

If you want the smallest set that still works:
- Copy [MAP.md](MAP.md) and [FORBIDDEN.md](FORBIDDEN.md) into your repo root.
- Add [copilot-instructions.md](copilot-instructions.md) to your repo root (or to `.github/copilot-instructions.md`, depending on your tooling).
- Add the CI workflow in [ci/github-actions/ci.yml](ci/github-actions/ci.yml).

Then iterate: tighten naming rules, add import boundaries, add personas.

## Where to Copy These (Typical Repo Paths)

This playbook repo keeps templates under `artifacts/`. In a real repo, you usually copy them to these locations:

| Template in this playbook | Typical destination in your repo | Purpose |
|---|---|---|
| `artifacts/MAP.md` | `MAP.md` | Repo-level cognitive map for navigation + boundaries |
| `artifacts/FORBIDDEN.md` | `FORBIDDEN.md` | Negative-space firewall (what the agent must not do) |
| `artifacts/DOs.md` | `DOs.md` (optional) | Positive guidance (what to do) |
| `artifacts/copilot-instructions.md` | `.github/copilot-instructions.md` (or repo root) | Agent behavior + constraints |
| `artifacts/CODEOWNERS` | `.github/CODEOWNERS` | Review gates for red zones |
| `artifacts/personas/*` | `docs/ai/personas/*` (or similar) | Builder/Auditor/Enforcer prompt templates |
| `artifacts/ci/github-actions/ci.yml` | `.github/workflows/ci.yml` | Enforce checks in CI |
| `artifacts/hooks/pre-commit` | `.git/hooks/pre-commit` (local) | Local fast checks (CI still required) |
| `artifacts/hooks/pre-commit.ps1` | `scripts/pre-commit.ps1` (or similar) | Windows-friendly hook runner |
| `artifacts/ls-lint/.ls-lint.yml` | `.ls-lint.yml` | Deterministic naming enforcement |
| `artifacts/linters/arch_linter.py` | `tools/linters/arch_linter.py` (or similar) | Enforce import boundaries (adapt to your stack) |
| `artifacts/decisions/000_template.md` | `decisions/000_template.md` | ADR-lite starter template |
| `artifacts/intent_headers/intent_header_template.md` | `docs/ai/intent_header_template.md` | Copy-paste intent header reference |
| `artifacts/testing/ai_readable_test_failures.md` | `docs/testing/ai_readable_failures.md` | Examples for instructional failure messages |
| `artifacts/logging/event.schema.json` | `docs/logging/event.schema.json` (or `schemas/`) | Schema-stable telemetry contract |

Notes:
- Hooks in `.git/hooks/` are not committed by default; treat them as developer convenience.
- CI is the enforcement point; if CI doesn’t run it, it doesn’t exist.
