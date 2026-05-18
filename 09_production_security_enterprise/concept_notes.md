# Concept Notes: Production Security & Enterprise Integration

When moving agents into production inside corporate environments, they transition from sandboxed playgrounds to live systems capable of executing database mutations, reading customer records, and triggering external business APIs. This introduces critical security challenges.

---

## 1. Secure Sandboxed Execution

If an agent is given the capability to write and run code (e.g. Python code tools to solve data analysis tasks), the code **must** be isolated from the host machine:
- **Builtins Restriction**: Standard hazardous operations (like `open()`, `eval()`, `exec()`, `__import__`) must be blocked or heavily restricted to prevent reading host system files or environment variables.
- **Process Boundaries**: Scripts must run in isolated subprocesses, virtual environments, or Docker containers, rather than inside the main agent application process.
- **Timeouts**: Malicious user prompts can cause the agent to generate infinite loops (e.g. `while True: pass`). The execution sandbox must enforce strict timeouts to prevent Denial-of-Service.

---

## 2. Enterprise Integrations & Circuit Breakers

Agents need to call enterprise systems (Jira, ServiceNow, Salesforce). If these downstream systems experience latency spikes or outages, a naive agent will repeatedly call them, wasting API credits, clogging queues, and crashing the agent.

To protect both our agent and downstream systems, we implement the **Circuit Breaker** design pattern:

```
          [Request In]
               │
               ▼
     ┌──────────────────┐
     │  Circuit State   │
     └───────┬──────────┘
             │
      ┌──────┴──────┐
      ▼             ▼
  [CLOSED]       [OPEN] (Fails immediately with fallback)
(Normal run)
      │
      ├─► Succesful: Reset Failure Counter
      │
      └─► Fails: Failure Counter++
            │
            ▼
        Failures >= Threshold ?
            │
            ├─► Yes: State = OPEN
            └─► No: Keep CLOSED
```

### Circuit Breaker States:
1. **CLOSED**: Normal operation. Requests flow directly to the downstream enterprise service.
2. **OPEN**: The service has failed repeatedly. The circuit breaker immediately blocks all requests, returning a fast fallback error without touching the target API.
3. **HALF-OPEN**: After a cooling period, the circuit breaker allows a single test request through. If it succeeds, the circuit closes again; if it fails, it returns to the OPEN state.
