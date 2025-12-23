# Known Trade-offs

**We choose Safety over Freedom.**

This playbook intentionally trades off some “classic” engineering values to gain reliability under agent execution.

## 1) Duplication (DAMP over DRY)

**What you pay:** you will sometimes copy/paste small amounts of code to keep features vertically sliced.

**What you get:** one-hit retrieval. The agent finds everything in one folder, and the context window contains the full story.

**Mitigation:** keep duplication local and bounded.
- Duplicate glue code, not core algorithms.
- Extract shared infrastructure into `/core` only when it’s truly shared.

## 2) Rigidity (The Straitjacket)

**What you pay:** you can’t name files however you want.

**What you get:** deterministic navigation. The agent doesn’t hallucinate a path or “close enough” location.

**Mitigation:** optimize the convention once, then stop thinking about it.
Good conventions are boring.

## 3) Maintenance (The Tax)

**What you pay:** you maintain intent headers, decision records, `MAP.md`, and `FORBIDDEN.md`.

**What you get:** the codebase keeps its shape as AI capabilities change.

**Mitigation:** be selective.
- Add intent headers only to critical paths (billing, auth, data migrations).
- ADR-lite only for decisions that would be costly to “rediscover.”

## 4) Reduced “Cleverness”

**What you pay:** less room for clever abstractions and implicit behavior.

**What you get:** predictability. Agents (and humans) can reason about the system with fewer hidden assumptions.

**Mitigation:** allow cleverness inside well-defined boxes (small modules with strong tests).

## 5) Upfront Work

**What you pay:** you invest in conventions and constraints early in a system’s lifecycle.

**What you get:** compounding returns: fewer regressions, faster onboarding, and more reliable automation.

**Mitigation:** adopt incrementally using the [90-Day Adoption Path](adoption_path.md) so you don’t big-bang restructure.
