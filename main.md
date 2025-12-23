# The AI-Native Engineering Playbook

This playbook shows how to design codebases and engineering workflows that AI agents can reliably navigate, change, and validate without turning your repo into a chaos engine.

## How to Use This Playbook

- If you're new: read [Introduction](introduction.md) + [Strategy & Scope](chapters/strategy_scope.md) first.
- If agents keep getting lost: start with [Structural Predictability](chapters/structural_predictability.md).
- If agents keep “optimizing” away safety/intent: start with [Cognitive Guardrails](chapters/cognitive_guardrails.md) + [Intent & Design Memory](chapters/intent_design_memory.md).
- If agents can write code but can’t finish the job: start with [Feedback Loops](chapters/feedback_loops.md).

## Quick Start (One Afternoon)

1. Create a repo map: a `MAP.md` that names folders, boundaries, and red zones.
2. Add a `FORBIDDEN.md` listing tools/patterns the agent must not use.
3. Pick one deterministic naming convention and enforce it in CI.
4. Rewrite one flaky test failure into an “AI-readable” failure message.

## Table of Contents

- [Introduction](introduction.md) — The core shift: optimizing for context and predictability.
- [Strategy & Scope](chapters/strategy_scope.md) — Who this is for, and the maturity ladder you can’t skip.
- [Structural Predictability](chapters/structural_predictability.md) — Make navigation deterministic; stop search-driven edits.
- [Cognitive Guardrails](chapters/cognitive_guardrails.md) — Constrain the solution space so mistakes become hard.
- [Intent & Design Memory](chapters/intent_design_memory.md) — Preserve the “why” so agents don’t refactor away invariants.
- [Feedback Loops](chapters/feedback_loops.md) — Turn tests/logs/tools into instruction-following loops.
- [Known Trade-offs](chapters/tradeoffs.md) — What you give up (and why it’s worth it).
- [90-Day Adoption Path](adoption_path.md) — A practical rollout plan with measurable milestones.
- [Common Failure Modes](failure_modes.md) — How teams fail (and what to do instead).
- [Final Synthesis](synthesis.md) — A compact mental model and scorecard.
- [Conclusion](conclusion.md) — The operating posture to keep.

## Sample Artifacts (Working Templates)

- [Artifacts README](artifacts/README.md) — Copy‑paste templates: `MAP.md`, `FORBIDDEN.md`, instructions, hooks, CI.

