# Module 10: Failure Modes & Incident Recovery

## What you will learn
- Identifying Direct and Indirect Prompt Injection attacks.
- Implementing robust sanitization filters (Guardrails) to intercept jailbreaks.
- Designing output validators to prevent leaking private system prompts or customer data.
- Establishing automated Incident Recovery Playbooks that degrade gracefully under system API out-of-memory or timeout conditions.

## Files in this folder
- `concept_notes.md` — Agent failure typologies (reasoning loops, data poisoning) and injection patterns
- `exercises.md` — detailed instructions to secure prompts and design runbooks
- `starter/` — exercise starter templates
  - `defense.py` — guardrail shield skeleton
  - `incident_recovery.py` — system degradation recovery skeleton
- `solution/` — reference implementations
  - `guardrails.py` — injection-intercepting and output-checking guardrail shields
  - `recovery_playbook.py` — automated incident recovery engine with model fallbacks
  - `vulnerabilities_guide.md` — comprehensive security playbook for LLM applications
- `tests/` — validation checks
  - `test_guardrails.py` — verifies that prompt injections are intercepted and blocked
  - `test_recovery.py` — verifies that API outages trigger secondary fallbacks and logging entries

## Run order
1. Read `concept_notes.md`
2. Follow instructions in `exercises.md`
3. Edit files in `starter/`
4. Run `pytest` to confirm your defenses and recovery wrappers pass tests
5. Compare your design against `solution/`

## Success criteria
- Prompt injections trying to override instruction sets are correctly flagged and blocked.
- Output checks intercept any private system keys (like 'SECRET_API_TOKEN') before returning results.
- Failed main API connections automatically route to backup mock recovery pipelines without crashing.

## Common failure modes
- **Naively blacklisting keywords**: Blocking only a handful of exact terms (like 'ignore instructions') while failing to detect semantic variations. You should use regex and LLM-based classifiers.
- **Cascading retry crashes**: Flooding retry channels during outages, resulting in severe resource exhaustion. You must implement exponential decay backoffs.
- **Unverified fallbacks**: Directing failures to backup endpoints that themselves are unauthenticated or unmonitored. You must test recovery paths regularly.
