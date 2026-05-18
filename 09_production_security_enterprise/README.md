# Module 09: Production Security & Enterprise Integration

## What you will learn
- Sandboxing code execution: Isolating dynamic tool runs from target host systems.
- Mitigating Denial-of-Service (DoS) and infinite execution loops using strict timeouts.
- Safe deserialization and sanitization of user-supplied variables.
- Connecting agents to enterprise endpoints (Jira, Salesforce, ServiceNow) using authenticated headers and a robust **Circuit Breaker** resilience pattern.

## Files in this folder
- `concept_notes.md` — Security boundary designs and Circuit Breaker patterns
- `exercises.md` — detailed instructions to configure sandboxes and connectors
- `starter/` — exercise starter templates
  - `sandbox_runner.py` — sandboxed execution skeleton
  - `enterprise_client.py` — enterprise sync and circuit breaker skeleton
- `solution/` — reference implementations
  - `secure_sandbox.py` — timeout-hardened and global-restricted environment runner
  - `enterprise_connector.py` — Jira/ServiceNow connector wrapper with fully functional Circuit Breaker state machines
  - `governance_policy.md` — enterprise deployment governance security guide
- `tests/` — validation checks
  - `test_sandbox.py` — verifies that execution timeouts abort hanging loops successfully
  - `test_enterprise.py` — verifies circuit breaker transitions from CLOSED to OPEN under API failures

## Run order
1. Read `concept_notes.md`
2. Follow instructions in `exercises.md`
3. Edit files in `starter/`
4. Run `pytest` to confirm your security boundaries and circuit breakers pass tests
5. Compare your design against `solution/`

## Success criteria
- Code sandboxes successfully block imports of hazardous modules (like `os` or `sys`).
- Dynamic script execution halts instantly if execution duration exceeds the maximum millisecond timeout limit.
- The Enterprise Client automatically trips its Circuit Breaker and returns fallback errors if consecutive target endpoint timeouts occur.

## Common failure modes
- **Leaky Sandboxes**: Restricting standard builtins but failing to block custom sub-imports, allowing malicious scripts to exploit private fields. You must restrict global tables completely.
- **Runaway Threading**: Using simple timeout flags without terminating sub-processes, resulting in zombie processes consuming CPU cores. You must use joining processes or active thread cancellation.
- **Brittle Retries**: Flooding downstream enterprise platforms with immediate retry bursts, triggering severe rate limits. You should implement exponential backoff with jitter.
