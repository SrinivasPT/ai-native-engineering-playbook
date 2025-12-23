# Cognitive Guardrails (The Constraints)

**Make illegal states unrepresentable. Make architectural drift difficult. Make dangerous zones explicit.**

## What This Chapter Is About

Cognitive guardrails are constraints that shape what an agent *can* do.
They turn “be careful” (policy) into “you can’t” (physics).

## Why This Matters

Agents are aggressive pattern matchers. When your system is under-specified, they will:
- guess values (strings, magic numbers, implicit states)
- take shortcuts (import forbidden layers, bypass invariants)
- apply generic best practices that conflict with local rules

Guardrails reduce the solution space so the *correct* move is easy and the *wrong* move is hard.

## 1) Constraint-Driven Code (Make Illegal States Unrepresentable)

**What:** replace “stringly typed” ambiguity with enums, constrained types, validated input objects, and explicit state machines.

**Legacy (ambiguous):**
```python
def process(status: str):  # agent guesses: "paid", "PAID", "settled"?
    ...
```

**AI-native (constrained):**
```python
from enum import Enum

class OrderStatus(str, Enum):

    PENDING = "pending"
    PAID = "paid"
    FAILED = "failed"

def process(status: OrderStatus):
    ...
```

**Why:** you shrink the universe of mistakes.

**How (practical):**
- Use enums for finite states.
- Prefer `Money`, `UserId`, `OrderId` types over raw `str`/`int` where feasible.
- Validate at boundaries (API -> domain) so internal code can assume invariants.

## 2) Executable Architecture (Physics, Not Policy)

**What:** encode architectural boundaries as checks that fail the build.

PDF diagrams are “write once, read never.” Agents can’t enforce them.
You need **architecture as code**.

**Example: an import boundary rule (pseudo):**
```python
# arch_linter.py
# Fail if domain/features import infra directly.
FORBIDDEN_IMPORTS = {

    "src.features": ["src.infra"],
    "src.core": ["src.features"],
}
```

**Why:** when an agent tries to take a shortcut, CI slaps its hand.
The agent learns the law by hitting the wall.

**How:**
- Start with 2–3 boundaries that matter most (domain vs infra, auth, payments, secrets).
- Make violations loud and deterministic.
- Prefer a simple check you will maintain over a complex framework you won’t.

## 3) Negative Space (FORBIDDEN.md)

**What:** explicitly list tools, packages, and patterns the agent must not use.

Agents are helpful optimizers. They will reach for whatever they saw “works” on the internet.
You need a **firewall for creativity**.

**Example `FORBIDDEN.md`:**
- **NEVER** import `requests`. Use `httpx`.
- **NEVER** read `os.environ` in application code. Use `Config`.
- **NEVER** place business rules in controllers.
- **NEVER** add new dependencies without updating the dependency policy.

**Why:** it forces the agent to unlearn generic training and follow *your* local laws.

**How:** keep it short and specific. If it becomes a novel, you’re using it as a dumping ground.

## 4) Explicit Security Boundaries (The Red Zone)

**What:** mark sensitive areas so agents treat them as special by default.

LLMs are sensitivity-blind: `password_hash` looks like `user_bio` to a tokenizer.
You must paint danger zones in bright red.

**Example (in `MAP.md`):**
```markdown
- `/core/auth`: RED ZONE. Changes require security review.
- `/infra/secrets`: RED ZONE. No logging. No debugging dumps.
- `/features/payments`: HIGH RISK. Must preserve idempotency and audit trail.
```

**Why:** it prevents refactoring leaks and “helpful” logging of secrets.

## 5) Permissioned Authority (Least Privilege)

**What:** stop running agents in god mode.

If an agent hallucinates `rm -rf`, it shouldn’t have the permissions to execute it.

**Practice examples:**
- Task: “Update CSS” → write access to `/frontend/styles/**` only.
- Task: “Add tests” → write access to `tests/**` only.
- Task: “Refactor auth” → read-only for most agents; gated write access for a security persona.

**Why:** blast-radius control.

## Checklist

- Do critical states have enums/types instead of raw strings?
- Are domain invariants validated at boundaries?
- Do you have 2–3 enforced architectural boundaries in CI?
- Does `FORBIDDEN.md` exist and match actual team standards?
- Are red zones explicitly marked in `MAP.md`?
- Are agents scoped by permissions/tools based on task risk?
