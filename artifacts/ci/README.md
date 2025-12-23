# CI Templates

These templates show how to enforce the playbook rules in CI.

- GitHub Actions: [github-actions/ci.yml](github-actions/ci.yml)

Principles:
- CI is the source of truth (hooks are optional convenience).
- Fail fast on structural violations.
- Keep feedback readable and actionable.
