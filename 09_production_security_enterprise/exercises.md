# Exercises: Production Security & Enterprise Integration

In this module, you will write code to protect your agent infrastructure from rogue code tools and downstream API failure cascades.

---

## 🏋️ Exercise 9.1: Building a Restricted Code Sandbox

**Location**: `starter/sandbox_runner.py` → `solution/secure_sandbox.py`
**Goal**: Implement a sandboxed environment runner that compiles and executes Python script strings with strict timeout boundaries and restricted global variables.

**Tasks**:
1. Open `starter/sandbox_runner.py` and inspect the `run_code_sandbox` function skeleton.
2. Build global namespace dictionaries that strip access to `__import__` and other dangerous builtins.
3. Configure the runner to run user scripts inside a separate thread or process.
4. Set a timeout limit (e.g. 500 milliseconds) that terminates the runner if the code executes a hanging loop.

---

## 🏋️ Exercise 9.2: Implementing a Circuit Breaker Client

**Location**: `starter/enterprise_client.py` → `solution/enterprise_connector.py`
**Goal**: Design a client class that wraps connection requests to enterprise endpoints (like Jira and ServiceNow) with an automated circuit breaker.

**Tasks**:
1. Implement a state tracking machine with three states: `"CLOSED"`, `"OPEN"`, and `"HALF-OPEN"`.
2. Keep a count of consecutive API connection timeouts or errors.
3. If failures exceed 3, transition the state to `"OPEN"`, blocking subsequent connection attempts and immediately raising a fallback message.

---

## 🏋️ Exercise 9.3: Enterprise Governance Deployment Policy

**Location**: `solution/governance_policy.md`
**Goal**: Review corporate deployment compliance guidelines detailing audit trails, API secret storage rules, and token rotation frequencies.
