# Intent Header Template

Use this as a short, consistent block at the top of critical functions or modules.

```text
AI-Intent: <what this code is responsible for>
Invariant: <must always remain true>
Failure Mode: <what to do when deps/inputs are missing>
Risk: <what breaks if changed>
```

Example:

```text
AI-Intent: Charge a saved payment method for an invoice.
Invariant: Never charge twice for the same invoice (idempotency required).
Failure Mode: If gateway is unavailable, record failure and retry; do not drop state.
Risk: Double charges cause refunds, disputes, and compliance incidents.
```
