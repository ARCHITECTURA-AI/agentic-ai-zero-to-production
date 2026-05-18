# Capstone Rubric

This rubric defines the grading and success metrics for capstone projects built during Module 11. Facilitators and students should use this to gauge production readiness.

---

## 📊 Rubric Categories & Criteria

| Metric | Fail (0 - 1 pts) | Satisfactory (2 - 3 pts) | Production Ready (4 - 5 pts) |
| :--- | :--- | :--- | :--- |
| **State-Loop & Stability** | Loops infinitely; runs out of budget immediately; crash on empty completions. | Stabilizes with basic max step limiter; simple recovery on JSON parsing. | Proactively handles infinite cycles; executes backoff retries; budget-aware. |
| **Tool Safety & Schemas** | Passes strings directly to tools; lacks Pydantic validation schemas. | Implements basic Pydantic schema validation; basic try-except blocks. | Fully isolates high-risk tools; validates execution arguments strictly via models. |
| **Memory & Context** | Dumb appending of history; context window overflows on long runs. | Simple vector store retriever; standard history pruning. | In-memory ChromaDB pipeline with smart token budget pruning to stay in model boundaries. |
| **Observability** | No logs or basic print statements; hard to debug step failures. | Basic standard logging; unstructured outputs. | Structured JSON logs; OpenTelemetry spans configured for precise trace tracking. |
| **Defensive Security** | Vulnerable to basic prompt injection payloads. | Has basic system prompts blocking overrides. | Implements active input guardrails, sanitization layers, and safe parser barriers. |
