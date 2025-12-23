# Common Failure Modes

**How to fail at AI adoption.**

This chapter is a debugging guide. If your agent program is producing chaos, find the matching failure mode and apply the fix.

## 1) Over-Constraining Early
**The Mistake:** Locking down architecture before you know what you are building.
**The Result:** Paralysis. The agent can't move without hitting a wall.

**Symptoms:**
- every change requires exceptions and approvals
- engineers spend more time fighting rules than building product
- agents produce minimal diffs because they’re blocked, not because they’re correct

**Fix:**
- keep constraints focused on high-risk zones first (auth, payments)
- adopt conventions incrementally (one feature at a time)
- treat early rules as “defaults,” not “laws,” until the system stabilizes

## 2) Under-Constraining Critical Zones
**The Mistake:** Letting the agent edit `auth_service.py` without review.
**The Result:** Security breach.

**Symptoms:**
- secret leakage into logs
- authentication/authorization regressions
- “helpful” refactors that weaken checks

**Fix:**
- mark red zones in `MAP.md`
- enforce review gates for high-risk folders
- run a security/auditor persona on sensitive diffs

## 3) Intent Rot
**The Mistake:** Changing the code but leaving the old comments.
**The Result:** The agent believes the comment, not the code. Hallucination ensues.

**Symptoms:**
- agents repeatedly reintroduce removed behavior (“but the comment says…”) 
- humans are confused about what’s true
- tests disagree with docs

**Fix:**
- keep intent headers short and update them when behavior changes
- delete stale intent rather than lying
- prefer executable checks (tests/linters) over narrative where possible

## 4) Persona Bottlenecks
**The Mistake:** Requiring 5 different AI agents to approve every PR.
**The Result:** Development velocity drops to zero.

**Symptoms:**
- coordination overhead dominates
- review queues grow
- agents repeat the same feedback with different wording

**Fix:**
- start with two personas: Builder + Auditor
- add more personas only when you have a clear recurring risk to address
- keep diffs small so one auditor pass is enough

## Meta-Failure: No Fast Loop

**The Mistake:** CI takes so long that neither humans nor agents iterate effectively.

**Symptoms:**
- “push and pray” workflow
- agents lose context between runs
- more breakage reaches main

**Fix:**
- make unit tests fast
- add a single local command to run the core loop
- automate formatting and lint fixes
