# Concept Notes: Module 00 - Alignment and Calibration

## Why We Calibrate
Building software with agents represents a fundamental paradigm shift from static engineering:
1. **Stateless LLMs**: An LLM does not "remember" the previous execution step unless you feed the context back.
2. **Nondeterminism**: Traditional tests verify exact output string matches; agentic evaluations require semantic checking or schema confirmation.
3. **The Halting Problem**: Agents can run infinitely if safety exit bounds are missing.
4. **Handoff Contracts**: Multi-agent graphs fail without rigid schema specifications.
