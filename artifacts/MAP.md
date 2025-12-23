# Repository Cognitive Map (Template)

This file is a curated “you are here” sign.

Rules:
- Keep this short (aim for 1–2 pages).
- Name boundaries explicitly.
- Mark red zones.
- State the laws (what must never happen).

---

## Core Architecture

- `/core` — shared infrastructure and cross-cutting concerns.
  - `/core/auth` — **RED ZONE**: authentication and authorization.
  - `/core/config` — configuration loading/validation.

- `/features` — vertical slices (business logic).
  - `/features/billing` — charging, invoices, refunds.
  - `/features/orders` — order lifecycle.

- `/infra` — adapters to external systems.
  - `/infra/persistence` — database models/migrations.
  - `/infra/http` — HTTP clients.

- `/api` — thin transport layer (controllers/handlers/routes). **No business rules.**

## The Laws (Non-Negotiable)

- **Business logic** lives in `/features/*`.
- **Controllers/handlers** must be thin. No business rules in `/api`.
- `/features/*` must not import `/infra/*` directly. Use ports/interfaces in `/core`.
- `/core/auth` is **read-only for agents** unless explicitly authorized.
- Secrets and credentials must never be logged.

## Common Tasks → Where to Change Code

- Add a new feature: `src/features/<feature>/...`
- Add a new API route: `src/api/...` that calls `src/features/<feature>/<feature>_service.*`
- Change a business rule: `src/features/<feature>/<feature>_service.*`
- Add a database field: `src/infra/persistence/...` + migration

## Red Zones (High-Risk Areas)

- `/core/auth` — requires security review.
- `/features/billing` — requires idempotency and audit trail.
- `/infra/secrets` — no logging; restrict access.

## Ownership / Reviews

- Billing: @billing-owners
- Auth: @security-owners
- Infra: @platform-owners
