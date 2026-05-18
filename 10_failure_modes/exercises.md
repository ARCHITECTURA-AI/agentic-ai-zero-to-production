# Exercises: Failure Modes & Incident Recovery

In this module, you will build defensive layers to secure your agents from exploitation and keep them operating during service disruptions.

---

## 🏋️ Exercise 10.1: Intercepting Prompt Injections

**Location**: `starter/defense.py` → `solution/guardrails.py`
**Goal**: Build input and output guardrails that analyze query payloads for jailbreak sequences and prevent private keys from leaking.

**Tasks**:
1. Open `starter/defense.py` and inspect `is_safe_input` and `is_safe_output` functions.
2. Build custom regex rules and semantic keyword arrays to identify jailbreaks like `"ignore all previous"`, `"system override"`, or `"developer mode"`.
3. Implement an output check that intercepts and redacts target secret variables (like `"SECRET_API_TOKEN"`) from response texts.

---

## 🏋️ Exercise 10.2: Designing Model Degradation Runbooks

**Location**: `starter/incident_recovery.py` → `solution/recovery_playbook.py`
**Goal**: Implement a fallback runner that intercepts API connection exceptions, registers failures, and gracefully switches to secondary backup systems.

**Tasks**:
1. Open `starter/incident_recovery.py` and inspect the runbook skeleton.
2. Write logic to execute the primary pipeline.
3. Catch any `ConnectionError`, `TimeoutError`, or downstream outages.
4. On failure, write an incident log entry and route execution to the fallback runner.

---

## 🏋️ Exercise 10.3: Reviewing the Security Vulnerability Catalog

**Location**: `solution/vulnerabilities_guide.md`
**Goal**: Review the comprehensive vulnerability catalog outlining prompt jailbreak methodologies, data pollution vectors, and countermeasures.
