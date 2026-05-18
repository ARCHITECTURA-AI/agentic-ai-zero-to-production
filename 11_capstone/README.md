# Module 11: Capstone Projects (Options A, B, C, D)

Welcome to the Capstone Module! In this final coding module, you will choose one of four comprehensive, enterprise-grade capstone projects. Each project pulls together knowledge from across all modules—integrating tool definitions, RAG, structured evaluation metrics, multi-agent coordination, OTel tracing, sandboxing, and security guardrails.

---

## The 4 Capstone Options

### 🚀 Option A: Enterprise Customer Support Copilot (Multi-Agent RAG & HITL)
- **Concept**: A unified ticket-handling team. A supervisor coordinates specialist Billing and Refund agents.
- **Key Modules**: RAG Context, Human-in-the-Loop gates, multi-agent handshakes.
- **Starters**: `starters/copilot_starter.py`
- **Solutions**: `solutions/copilot_solution.py`

### 📊 Option B: Sandboxed Autonomous Data Analyst
- **Concept**: An agent capable of performing raw data processing by executing dynamic mathematical script commands in a fully isolated, timeout-guarded environment.
- **Key Modules**: Sandboxing, AST auditing, prompt engineering.
- **Starters**: `starters/analyst_starter.py`
- **Solutions**: `solutions/analyst_solution.py`

### 🔧 Option C: Resilient DevOps Incident Coordinator
- **Concept**: An active site reliability agent that monitors application traces, flags anomalies, manages Jira ticket integrations, and manages circuit breaker recovery loops.
- **Key Modules**: Telemetry Traces, Circuit Breakers, fallbacks.
- **Starters**: `starters/devops_starter.py`
- **Solutions**: `solutions/devops_solution.py`

### 🛡️ Option D: Secure Semantic Guardrail Gateway Proxy
- **Concept**: A high-speed middleware proxy API wrapper that intercepts prompt injections, evaluates groundedness (faithfulness), and audits responses for PII leaks.
- **Key Modules**: Guardrails, LLM-as-a-Judge evaluations.
- **Starters**: `starters/proxy_starter.py`
- **Solutions**: `solutions/proxy_solution.py`

---

## Validation & Testing
We have provided validation tests inside the `tests/` subdirectory to verify that your capstone code correctly implements the core architectural specifications.
- Run `pytest 11_capstone/tests/` to verify your implementation.
