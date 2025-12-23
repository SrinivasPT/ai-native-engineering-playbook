# Strategy & Scope

## What This Chapter Gives You

This chapter answers four questions:
- **What** “AI-native engineering” means in practice (not hype)
- **Who** should adopt these patterns (and who should not)
- **When** to introduce constraints (and when to stay flexible)
- **How** to climb the maturity ladder without creating a chaos engine

## Who Needs This?

**You do, if:**
- You maintain a codebase large enough that context is routinely missing (> ~50k LOC is a good proxy)
- You use agents (Cursor, Windsurf, Claude, etc.) and they repeatedly:
  - get lost (“where is the file?”)
  - make edits in the wrong layer
  - invent libraries, modules, or patterns that aren’t in your repo
  - refactor away domain invariants

**Walk away if:**
- You are hacking on a weekend prototype, exploring product-market fit
- You expect constraints to “create velocity” before you even know the shape of the system

Constraints are an investment. Make them when you have something to protect.

## The Philosophy

This is not a “no-code” dream. This is **high-discipline engineering**.

AI-native engineering treats your repo as an execution environment for intelligence.
That means:
- “Laws” must be explicit (not tribal knowledge)
- constraints should be enforced by tools (not policy docs)
- intent must be written down where the agent will see it (code, tests, MAP/forbidden files)

### Minimum Prerequisites

If you do not have these, build them first:
- CI that runs tests and linting on every change
- A working local developer loop (`make test`, `npm test`, etc.)
- A basic release pipeline (even if manual)

You can’t automate a process that doesn’t exist.

## The AI-Native Maturity Model

Adopting AI isn’t a switch you flip. It’s a ladder you climb.
Most teams get stuck at “autocomplete plus vibes.” This model gives you a safer progression path.

#### Level 1: The Reliable Intern (Predictable Structure)

**What changes:** the agent stops asking “Where is the file?”

**How:** deterministic naming + a repo map (`MAP.md`) + vertical slicing.

**Result:** navigation errors drop toward zero.

**Example:**
- Task: “Add refunds support”
- Convention: `src/features/[feature]/[feature]_[layer].py`
- Path becomes a calculation: `src/features/refunds/refunds_service.py`

#### Level 2: The Historian (Intent & Memory)

**What changes:** the agent can explain *why* the code looks like this.

**How:** intent headers on critical functions + lightweight decision journals (ADR-lite).

**Result:** the agent stops refactoring your business logic into oblivion.

**Example:**
- “We used a Factory here to avoid circular deps; do not inline.”
- “Do not split into microservices; context fragmentation was a failure mode.”

#### Level 3: The Student (Feedback Systems)

**What changes:** tests stop shouting “FAIL” and start teaching.

**How:** turn test failures into fix instructions; log in machine-readable schemas; keep fast feedback loops.

**Result:** the agent runs: Code → Fail → Read error → Fix → Pass (with minimal supervision).

#### Level 4: The Partner (Semi-Autonomous)

**What changes:** specialized personas patrol your repo.

**How:** split responsibilities (builder vs auditor), enforce least privilege, and require small diffs.

**Result:** you wake up to green builds and merged PRs more often than not.

**Warning:** You cannot skip levels. If you try Level 4 autonomy without Level 1 structure, you will build a chaos engine.

## When to Apply Which Practices

- If agents pick the wrong files: start with [Structural Predictability](structural_predictability.md).
- If agents break architecture: add [Cognitive Guardrails](cognitive_guardrails.md).
- If agents refactor away “weird but necessary” code: add [Intent & Design Memory](intent_design_memory.md).
- If agents can’t finish end-to-end changes: strengthen [Feedback Loops](feedback_loops.md).

## Checklist (Use This Before You Increase Autonomy)

- Can the agent locate the correct folder without search?
- Are there written laws (`MAP.md`, conventions) the agent can follow?
- Are critical invariants documented close to the code that enforces them?
- Will CI/tooling block architectural drift automatically?
- Do tests/logs provide enough instruction for the agent to self-correct?

---

← [Back to Table of Contents](main.md)
