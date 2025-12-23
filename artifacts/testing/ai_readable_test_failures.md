# AI-Readable Test Failures (Examples)

Goal: make failures act like prompts.

## Pattern

Include:
- expected vs actual
- likely cause
- where to look
- invariant to preserve

## Python example

```python
def test_referral_bonus_applied():
    balance = get_balance_for_user("u1")
    assert balance == 100, (
        f"Expected balance=100, got balance={balance}. "
        "Likely referral bonus logic. Check src/features/signup/signup_flow.py. "
        "Invariant: bonus applies only once per referred user. "
        "If time-dependent, verify transaction date is not in the future."
    )
```

## TypeScript example

```ts
expect(actual).toBe(expected);
// Better:
expect(actual).toBe(expected);
// with message:
if (actual !== expected) {
  throw new Error(
    `Expected=${expected} Actual=${actual}. ` +
    `Check referral bonus rules in src/features/signup/signupService.ts. ` +
    `Invariant: bonus only once per user.`
  );
}
```

## What not to do

- Don’t print massive objects.
- Don’t hide the failure in vague words (“should be correct”).
- Don’t require a human to guess what file to open.
