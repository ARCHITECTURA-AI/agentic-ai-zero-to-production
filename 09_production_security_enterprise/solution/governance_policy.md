# Enterprise Governance & Deployment Checklist

Before deploying Agentic systems inside a regulated production environment (e.g. SOC2, ISO27001), they must pass a structured **Governance Policy Audit**. naive AI agents that run code or trigger APIs autonomously can represent significant vector paths for exploitation.

---

## 1. Secrets Management and API Tokens
- [ ] **No Hardcoded Tokens**: All API credentials (for OpenAI, Anthropic, Jira, ServiceNow, etc.) must be stored in secure vaults (e.g. AWS Secrets Manager, HashiCorp Vault, Azure Key Vault).
- [ ] **Short Token Lifetimes**: API connection authorization keys must rotate automatically every 90 days.
- [ ] **Principle of Least Privilege**: Agent service accounts must be restricted only to resources required for the task. (e.g., Jira credentials should only have permission to create issues in a single project, not edit global system settings).

---

## 2. Infrastructure Sandboxing
- [ ] **Containerized Execution**: Code tools must run in independent Docker containers or firewalled sandboxes (e.g., gVisor, AWS Firecracker).
- [ ] **Network Isolation**: Sandbox runtimes must be offline (egress disabled) unless explicitly whitelisted for target corporate database APIs.
- [ ] **Timeouts and Caps**: CPU execution time limits must not exceed 2.0 seconds per request, and memory consumption must be capped at 128MB.

---

## 3. Comprehensive Logging & Audit Ledgers
- [ ] **Immutable History Logs**: Every tool call, prompt template iteration, user input, and agent response must be logged to a write-once read-many (WORM) storage ledger.
- [ ] **Personally Identifiable Information (PII) Sanitization**: Before trace logs are exported to external observability tools (like Arize, Langfuse), they must pass through an offline regex filter that redacts emails, social security numbers, and billing addresses.
