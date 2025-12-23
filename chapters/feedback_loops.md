# Feedback Loops (The Learning)

**Reframing development: you are not the driver. You are the instructor.**

## What This Chapter Is About

Feedback loops are the mechanisms that let an agent converge on the correct solution:
- tests that explain failures
- tooling that’s fast and deterministic
- logs that are machine-parsable
- review processes that keep risk bounded

If you want agents to complete end-to-end work (not just write code), you need loops.

## Why This Matters

Without good feedback, agents guess.
With good feedback, agents iterate.

Your goal is to make the loop:

> Plan → Change → Run → Observe → Correct → Repeat

…fast, specific, and instruction-following.

## 1) AI‑Readable Test Failures (Turn Errors Into Prompts)

“Test failed” is a useless signal.
Turn failure messages into fix instructions.

**Legacy:** `AssertionError: False != True` (agent: “???”)

**AI‑native:**
```python
assert balance == 100, (
    f"Expected balance=100, got balance={balance}. "
    "Likely referral bonus logic. Check 'signup_flow.py' and the referral rules. "
    "Also verify transaction dates are not in the future."
)
```

**Why:** the error message is the fix plan.

**How (template):**
- What was expected vs observed
- Where to look (file/module)
- Common causes / invariants to check
- If applicable: reproduction hints (time zones, seeds, configuration)

## 2) Agent Personas (Split the Brain)

Don’t ask one agent to be god. Split responsibilities.

**Example crew:**
- **Builder**: writes code, fast, creative.
- **Auditor**: read-only, paranoid, checks security, data handling, invariants.
- **Conventions enforcer**: checks paths, naming, and folder laws.

**Why:** checks and balances. The auditor catches what the builder hallucinates.

**How:** make persona constraints explicit:
- Builder: can modify code, but must keep diffs small.
- Auditor: cannot write, only flags risk.
- Enforcer: only checks structural rules and fails fast.

## 3) Atomic Diffs (Keep Work Inside Attention Span)

Give an agent 2,000 lines and it will glaze over.
Give it 50–200 lines and it becomes precise.

**Example stack:**
1. PR 1: DB migration (small, isolated)
2. PR 2: core domain logic
3. PR 3: API wiring

**Why:** smaller diffs create tighter loops and less context loss.

## 4) Schema‑Stable Telemetry (Log for Machines)

Strings are for humans. JSON is for machines.

**Bad:** `log.error("Failed user " + uid)`

**Good:**
```python
log.error({
    "event": "billing_charge_failed",
    "reason": "insufficient_funds",
    "user_id": uid,
    "code_path": "src/features/billing/billing_service.py:45",
})
```

**Why:** an agent can query logs, find the `code_path`, and propose a fix.

**How:** keep log schemas stable; add fields rather than changing meanings.

## 5) Deterministic Tooling (Fast Feedback Is Oxygen)

If CI takes 20 minutes, the agent forgets what it was doing.

Targets that help:
- Unit tests: seconds, not minutes
- Linters/formatters: auto-fixable with one command
- One command to run “the loop” locally (e.g., `make test`)

## 6) Human‑in‑the‑Loop (Autonomy ≠ Abdication)

You own the risk.

**The new job:**
- Less: typing syntax
- More: reviewing plans, defining constraints, accepting risk

If you don’t understand the code, you don’t own it.

## Example: The Agent Fix Loop

1. Agent proposes a change plan (files, invariants, tests to run).
2. Agent makes a small diff.
3. Agent runs tests.
4. A failure message points to the likely cause and location.
5. Agent applies a correction.
6. Tests pass; auditor persona reviews risk.

## Checklist

- Do failing tests explain what to check and where?
- Are diffs small enough to review quickly?
- Are logs structured and stable (machine-readable)?
- Do you have at least two personas: builder + auditor?
- Is the local feedback loop fast and deterministic?

## Sample Artifacts

- Personas (Builder/Auditor/Enforcer): [../artifacts/personas/](../artifacts/personas/)
- AI-readable test failures: [../artifacts/testing/ai_readable_test_failures.md](../artifacts/testing/ai_readable_test_failures.md)
- Logging schema example: [../artifacts/logging/event.schema.json](../artifacts/logging/event.schema.json)
- CI template: [../artifacts/ci/github-actions/ci.yml](../artifacts/ci/github-actions/ci.yml)

---

← [Back to Table of Contents](../main.md)
