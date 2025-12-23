# FORBIDDEN (Template)

This file is a “negative space” firewall: patterns an agent must not introduce.

Use this to override the model’s generic training with *your* local laws.

---

## Dependencies

- **NEVER** add a new dependency without:
  - updating the dependency policy (if you have one)
  - justifying it in an ADR-lite decision
  - getting an explicit approval

## Architecture

- **NEVER** place business rules in controllers/handlers/routes.
- **NEVER** bypass domain services to “just make it work.”
- **NEVER** import from red zones unless explicitly authorized.

## Security

- **NEVER** log secrets, tokens, passwords, session IDs, full credit card numbers.
- **NEVER** downgrade crypto/security checks to make tests pass.
- **NEVER** disable authz checks for convenience.

## Code Changes

- **NEVER** do large refactors when asked for a small change.
- **NEVER** rename files/folders unless the task explicitly requires it.
- **NEVER** change public APIs without updating callers and tests.

## Tooling / Workflow

- **NEVER** commit formatting-only changes mixed with logic changes.
- **NEVER** skip tests when the repo has tests.

## Repo-Specific (Fill These In)

- **NEVER** use `<forbidden-lib>`; use `<preferred-lib>`.
- **NEVER** read env vars directly in app code; use `<Config>`.
