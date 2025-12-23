# ls-lint (Template)

Files:
- [.ls-lint.yml](.ls-lint.yml)

Purpose:
- Enforce deterministic naming and reduce “search-driven edits.”

How to use:
1. Copy `.ls-lint.yml` into your repo root.
2. Install `ls-lint` in CI.
3. Run `ls-lint` locally and in CI.

Notes:
- Adjust rules to match your layout (kebab-case vs snake_case vs camelCase).
- CI is the enforcement point; hooks are optional.
