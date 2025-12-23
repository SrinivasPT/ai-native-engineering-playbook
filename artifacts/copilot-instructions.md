# Copilot / Agent Instructions (Template)

These instructions are meant for AI coding agents operating inside this repository.

If you adopt this file, place it where your tool expects it (common locations include:
- `copilot-instructions.md` at repo root
- `.github/copilot-instructions.md`
- `docs/ai/agent_instructions.md`
).

---

## Mission

Help implement changes safely and predictably by following local conventions and constraints.

## First Steps (Always)

1. Read `MAP.md` to understand boundaries and red zones.
2. Read `FORBIDDEN.md` to learn what must not be introduced.
3. Prefer deterministic navigation: avoid repo-wide search unless necessary.

## Operating Rules

### Plan and Scope

- Confirm the goal in 1–3 sentences before editing.
- Keep diffs small and reviewable.
- Do not do opportunistic refactors.

### Mechanical Predictability

- Follow the repo’s naming conventions.
- Put feature changes in the feature folder (vertical slice).
- Do not invent folders, packages, or libraries.

### Safety and Red Zones

- Treat these areas as high-risk (examples):
  - `core/auth/**`
  - `infra/secrets/**`
  - `features/billing/**`
- If a task touches a red zone, do one of:
  - propose a minimal patch and request explicit approval
  - route changes through an “auditor” review persona

### Tooling and Validation

- If tests exist, run the most relevant tests.
- If linters exist, run them.
- If a change might break behavior, add/update tests.

## Output Expectations

When proposing a change:
- List files you will modify.
- State the invariants you intend to preserve.
- State how you will validate (tests, lint, manual checks).

## Do / Don’t

**Do**
- Prefer explicit, boring code in critical paths.
- Add intent headers on critical functions (invariants + failure modes).
- Upgrade error messages to be instructional.

**Don’t**
- Don’t introduce new dependencies unless asked.
- Don’t change architecture boundaries.
- Don’t write code you can’t explain.

---

## Quick Links

- [MAP.md](MAP.md)
- [FORBIDDEN.md](FORBIDDEN.md)
- [Artifacts README](artifacts/README.md)
