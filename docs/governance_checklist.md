# Enterprise Governance Checklist

Use this checklist to audit an agentic system before deploying it to corporate environments or exposing it to customer channels.

---

## 🔒 Security & Containment
- [ ] **Execution Sandbox**: Are tools that execute generated code isolated inside a secure Docker container or micro-sandbox?
- [ ] **Least Privilege Access**: Does the agent's database or API token restrict write access to only necessary schemas or objects?
- [ ] **Injection Defenses**: Is there a dedicated validator sanitizing input strings before sending them to the LLM completion API?
- [ ] **Sensitive Data Scrubbing**: Are PII or credit card numbers masked prior to external provider routing?

---

## 🛡️ Budget & Crash Safeguards
- [ ] **Max Loop Limiter**: Is there a hard-coded maximum loop steps check (e.g., `max_steps=10`) preventing run-away iteration?
- [ ] **Cost-Breaker**: Is there an automated checker verifying the dollar value of tokens consumed and halting runs above threshold limits?
- [ ] **Fallback Logic**: Does the agent degrade gracefully (e.g., alert a human agent) if the model provider experiences an outage?

---

## 👁️ Auditability & Compliance
- [ ] **Trace Logs**: Are all agent decisions, system prompts, thoughts, actions, and observations recorded in a structured JSON log?
- [ ] **OpenTelemetry Integration**: Are trace spans transmitted to an APM system (like Phoenix, Datadog, or LangSmith)?
- [ ] **Human Escalation Gate**: Do tools that modify state (e.g., refund money, send emails, delete files) require an explicit HITL approval click?
