# Structural Predictability (The Map)

## What This Chapter Is About

Structural predictability means your repo has enough consistent structure that an agent can locate the correct place to work **without searching**.

**Rule #1: If the agent has to search, you have already lost.**

AI agents operate on probability. Every time they have to “guess” where something lives, they roll a die. Eventually, they roll a critical fail.

The goal is **Zero‑Shot Navigation**: given a task description, the correct file path is either obvious or mechanically computable.

## Why It Matters

Search is expensive and error-prone for agents:
- it burns context window on directory listings and irrelevant files
- it increases the chance of editing the wrong layer (API vs domain vs infra)
- it encourages “close enough” edits instead of correct ones

If you want autonomy, you must make navigation deterministic.

## 1) Deterministic Conventions (The Hash Map)
**What:** choose one naming/path convention that maps features to folders and layers.

**Why:** it converts navigation from “fuzzy search” into “hash lookup.”

**The Old Way (Creative Chaos):** developers name files based on vibes.
`auth_stuff.js`, `UserLoginController.ts`, `utils/helpers.py`.
The agent must read the tree to infer rules. That burns tokens and adds ambiguity.

**The AI-Native Way (The Algorithm):**
The file path is a function of the feature.
`[feature]/[feature]_[layer].[ext]`

*   **Task:** "Add a billing service."
*   **Calculation:** `features/billing/billing_service.py`
*   **Search Cost:** Zero.

**Enforcement:**
Don’t ask nicely. Enforce in CI.

Example enforcement options:
- `ls-lint` / naming linters
- custom script (simple is fine)
- pre-commit hooks (nice) plus CI (non-negotiable)

If a file is out of place, the build fails.
*   **Why:** It turns navigation from a "Fuzzy Search" problem into a "Hash Map Lookup" problem.

**How to pick a convention (pragmatic rules):**
- Prefer a convention that matches your runtime boundaries (feature/domain boundaries)
- Avoid deep nesting (agents and humans both lose context)
- Keep layer names small and stable (api/service/repo/model)

## 2) Repo-Level Cognitive Maps (MAP.md)
**What:** a curated “you are here” document that aligns the agent’s mental model with your architecture.

**The Problem:** “Lost in the Middle.”
When an agent enters a large repo, it’s blind. Dumping `tree` into context is noise.

**The Solution:** `MAP.md`
A curated "You Are Here" sign for the intelligence.

```markdown
# Repository Cognitive Map
## Core Architecture
- `/core`: Shared infrastructure.
    - `/core/auth`: **High Risk**. Do not touch without `security_auditor` review.
- `/features`: Business logic.
    - `/features/payments`: Stripe integration.
## The Laws
- **Business Logic** lives in `/features`.
- **Database Models** live in `/infra/persistence`.
- **NEVER** place business rules in `/api` controllers.
```

**Why:** It aligns the agent's mental model with the architect's intent instantly.

**How to keep `MAP.md` useful:**
- Keep it short (1–2 pages)
- Mark “red zones” and ownership
- State the *laws* (where business logic must live, import boundaries)
- Update it when you reorganize the repo (treat it like production code)

## 3) Vertical Slicing (The Bundle)
**What:** keep a feature’s API, domain logic, persistence adapter, and types close together.

**The Problem:** The scatter.
In horizontal architecture, a feature is smeared across 5 folders (`controllers`, `services`, `models`, `repos`, `dtos`).
The agent must retrieve 5 fragments to understand one concept. It will miss one.

**The Solution:** The Bundle.
Put everything related to “Orders” in one place.

```
src/features/orders/
  order_api.py
  order_model.py
  order_service.py
  order_repo.py
```

**Why:** **One‑Hit Retrieval.** A single search for “order logic” returns the whole context. The agent sees the entire feature at once.

## How to Implement Structural Predictability (In Order)

1. Pick a deterministic convention (feature + layer).
2. Move one feature to the new layout end-to-end.
3. Write `MAP.md` with:
   - folder meanings
   - boundaries and red zones
   - 5–10 “laws” the agent must follow
4. Add enforcement in CI.
5. Repeat feature-by-feature (don’t big-bang migrate unless you must).

## Quick Checks (Agent-Friendly)

You’re “done” with this chapter when:
- You can name the file path before you open the repo.
- A new engineer can locate a feature’s logic in < 60 seconds.
- CI blocks new files that violate conventions.
- `MAP.md` is short, accurate, and names boundaries clearly.

## Sample Artifacts

- Repo map template: [../artifacts/MAP.md](../artifacts/MAP.md)
- Filename lint config: [../artifacts/ls-lint/.ls-lint.yml](../artifacts/ls-lint/.ls-lint.yml)
- Pre-commit hook templates: [../artifacts/hooks/README.md](../artifacts/hooks/README.md)
- CI template: [../artifacts/ci/github-actions/ci.yml](../artifacts/ci/github-actions/ci.yml)

---

← [Back to Table of Contents](../main.md)
