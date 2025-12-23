# Intent & Design Memory (The “Why”)

**Code explains “how.” Intent explains “why.” Agents need the “why” to avoid destroying the “how.”**

## What This Chapter Is About

“Design memory” is the set of artifacts that preserve intent over time:
- the invariants you must not break
- the reason you chose one architecture over another
- the constraints that are invisible in code (time, state, randomness)

Without design memory, agents (and future humans) will refactor your system toward the average of the internet.

## Why It Matters

Agents are dangerous optimizers:
- they delete “redundant” checks
- they simplify “weird” code that was protecting an edge case
- they replace local patterns with generic patterns

Intent prevents good-looking changes that are actually incorrect.

## 1) Intent-First Functions (Put the Why Where the Agent Will See It)

**What:** add a small, consistent intent header on critical code paths.

**Why:** six months from now, the agent won’t delete the “useless” check.
It will read the invariant and salute.

**Intent header template (keep it short):**
```text
AI-Intent: <what this function is responsible for>
Invariant: <must always remain true>
Failure Mode: <how to behave when inputs/deps are missing or invalid>
Risk: <what could go wrong if changed>
```

**Example:**
```python
def apply_tax(price: float, item_id: int, tax_rate: float | None) -> float:
    """
    AI-Intent: Apply the 2025 luxury tax.
    Invariant: NEVER apply to essential goods (IDs < 1000).
    Failure Mode: If rate missing, default to 0. DO NOT block checkout.
    Risk: Overcharging triggers refunds + regulatory complaints.
    """
    ...
```

## 2) Decision Journals (ADR‑Lite)

**What:** a lightweight record of important architectural decisions.

Agents love to revert your architecture to the “average of the internet.”
Decision journals stop regression.

**ADR‑lite template:**
```markdown
# Decision: <title>

## Context
<what problem were we solving?>

## Decision
<what did we choose?>

## Why
<the key reasoning in 3-5 bullets>

## Alternatives Considered
- <option> — <why rejected>

## Consequences
<what trade-offs we accept>
```

**Example:**
```markdown
# Decision: Monolith over microservices

## Context
Agent work kept failing because feature context was split across many repos and services.

## Decision
Keep a monolith with vertical slices.

## Why
- Microservices fragment the context window.
- Cross-service changes increase coordination cost.

## Alternatives Considered
- Microservices — rejected due to context fragmentation.
- Serverless — rejected due to cold starts and debugging complexity.
```

## 3) Time, State, & Randomness (Make the Invisible Visible)

Agents can’t reliably “see” implicit globals like `datetime.now()` and `random.random()`.
Make them explicit.

**Bad:** `def calculate(): ...` (uses global time? maybe?)

**Good:**
```python
from datetime import datetime
from random import Random

def calculate(now: datetime, rand: Random) -> int:
    ...
```

**Why:** simulation and reproducibility. You can ask: “What happens on leap day?” and actually test it.

## 4) Context Hygiene (The Trash Compactor)

Old code is poison. Dead experiments are hallucinations waiting to happen.

**What:** delete aggressively and keep the living architecture obvious.

**How:**
- remove dead code paths and unused modules
- delete abandoned experiments (or quarantine them explicitly)
- keep docs current (intent rot is worse than no intent)

**Why:** a clean context window is a smart context window.

## Checklist

- Do critical functions include short intent headers with invariants?
- Do you have ADR‑lite records for major architecture choices?
- Are time/randomness/state dependencies injected (not hidden globals)?
- Are deprecated patterns and dead code removed (or clearly quarantined)?
- Is “intent rot” prevented by updating intent when behavior changes?
