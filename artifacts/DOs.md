# DOs (Template)

This is the positive counterpart to `FORBIDDEN.md`.

## Structure

- Put business logic in `/features/*` (vertical slices).
- Keep controllers thin: translate HTTP/transport → call domain service → return.
- Keep naming deterministic: paths should be computable from tasks.

## Safety

- Add intent headers on critical paths (auth, billing, migrations).
- Prefer explicit types/enums over free-form strings.
- Add small tests that encode invariants.

## Workflow

- Keep diffs small and atomic.
- Make tests and tooling fast.
- Make failures instructional (expected vs actual, where to look, likely cause).
