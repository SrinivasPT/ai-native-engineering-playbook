# 90-Day Adoption Path

**Evolution is painful. Here is the schedule.**

This path is designed to increase autonomy without increasing risk.
If you skip the foundation steps, you will create a chaos engine.

### Month 1: The Foundation (Stop the Bleeding)

**Goal:** make navigation deterministic and reduce “search-driven edits.”

**Week 1: Establish the map**
- **Action:** Write `MAP.md` (core folders, boundaries, red zones, 5–10 laws).
- **Action:** Identify 1–2 “high risk” zones (auth, payments) and label them.
- **Deliverable:** a new engineer can explain the repo in 10 minutes.

**Week 2: Standardize file paths**
- **Action:** pick a deterministic naming/path convention.
- **Action:** migrate one feature to the new convention end-to-end.
- **Deliverable:** “Given a task, we can predict the file path.”

**Week 3: Enforce conventions**
- **Action:** add enforcement in CI (e.g., `ls-lint` or a simple custom check).
- **Action:** add a “no new files outside convention” rule.
- **Deliverable:** convention violations fail the build.

**Week 4: Reduce context fragmentation**
- **Action:** apply vertical slicing to 1–2 additional features.
- **Action:** remove dead/duplicate folders that cause confusion (or quarantine them explicitly).
- **Result:** the agent stops getting lost.

### Month 2: The Guardrails (Build the Walls)

**Goal:** constrain the solution space so incorrect changes become hard.

**Week 5: Make illegal states unrepresentable**
- **Action:** replace stringly-typed states with enums/types on one critical feature.
- **Action:** validate invariants at boundaries (API → domain).
- **Deliverable:** fewer “almost right” failures and fewer invalid states.

**Week 6: Enforce architecture**
- **Action:** add one architecture rule that matters (e.g., features cannot import infra).
- **Action:** make violations fail CI deterministically.
- **Deliverable:** architectural drift becomes a build error.

**Week 7: Add negative-space rules**
- **Action:** create/expand `FORBIDDEN.md` to match real team standards.
- **Action:** remove the most common “agent hallucination” patterns (libraries, shortcuts).
- **Deliverable:** agents stop introducing forbidden dependencies/patterns.

**Week 8: Tighten red zones + permissions**
- **Action:** require review for red-zone changes.
- **Action:** run agents with least-privilege access for scoped tasks.
- **Result:** the agent stops breaking the build (and stops creating high-risk drift).

### Month 3: The Brain (Teach the Why)

**Goal:** teach intent and create self-correcting loops.

**Week 9: Add intent headers to critical paths**
- **Action:** add intent/invariant/failure-mode headers to 5–10 critical functions.
- **Deliverable:** agents can explain why “weird checks” exist.

**Week 10: ADR-lite decision journals**
- **Action:** record the top 3 architectural decisions you don’t want reversed.
- **Deliverable:** “average-of-the-internet” refactor suggestions get blocked by documented intent.

**Week 11: Rewrite feedback**
- **Action:** upgrade the worst failing tests to be AI-readable.
- **Action:** ensure the local loop is fast (formatters, lint-fix, unit tests).
- **Deliverable:** agent can go from red → green with fewer human interventions.

**Week 12: Persona rollout**
- **Action:** deploy at least two personas: Builder + Auditor.
- **Action:** enforce small diffs and review gates for risk.
- **Result:** the agent starts fixing its own bugs.

## How to Measure Progress (Simple Signals)

- “Where is the file?” questions drop.
- Convention violations become rare because CI blocks them early.
- Red-zone changes become deliberate and reviewed.
- Time-to-green for a typical agent change decreases.
- PR sizes shrink.

## Sample Artifacts

- Templates index: [artifacts/README.md](artifacts/README.md)
- CI workflow template: [artifacts/ci/github-actions/ci.yml](artifacts/ci/github-actions/ci.yml)
- Hooks templates: [artifacts/hooks/README.md](artifacts/hooks/README.md)

---

← [Back to Table of Contents](main.md)
