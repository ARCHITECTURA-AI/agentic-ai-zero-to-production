# Concept Notes: Advanced Evaluation & Observability

In production environments, agent behavior can be highly non-deterministic. Traditional print logging is insufficient to debug long ReAct reasoning cycles, tool executions, and multi-agent collaborations. We need structured **Observability** and automated **Evaluations**.

---

## 1. Traces and Spans (OpenTelemetry Paradigm)

Observability in modern agent platforms (like Arize Phoenix, LangSmith, and Langfuse) is built on the **OpenTelemetry (OTel)** standard.

- **Trace**: Represents the entire lifecycle of a request (e.g. "Handle Customer Refund").
- **Span**: A single unit of work within a trace (e.g. "Vector DB Retrieval" or "LLM Call").
- **Hierarchical Context**: Spans can contain children. A child span must reference its `parent_span_id`. This creates a nested hierarchy of execution, allowing developers to visually inspect exactly which sub-task caused a delay or crash.

```
[Trace: Handle Support Ticket]
  ├── [Span A: Vector DB Query] (Duration: 45ms)
  └── [Span B: ReAct Reason Cycle] (Duration: 850ms)
        ├── [Span C: Tool Call - Check Balance] (Duration: 120ms)
        └── [Span D: LLM Synthesis] (Duration: 300ms)
```

---

## 2. Faithfulness vs. Answer Relevance

Automated evaluations assess LLM response quality across multiple dimensions:

1. **Faithfulness (Groundedness)**: Is the agent's answer strictly derived from the retrieved documents? If the agent makes claims not supported by the context, it has **hallucinated**.
   $$\text{Faithfulness} = \frac{\text{Number of supported claims}}{\text{Total claims made in response}}$$
   
2. **Answer Relevance**: Does the response directly address the user's initial query, or does it deflect and introduce irrelevant tangents?

---

## 3. Production Business KPIs

In addition to semantic scores, developers must track concrete engineering and business metrics:
- **Time to First Token (TTFT)**: Key for real-time customer-facing chat interfaces.
- **Cost per Session**: Aggregated cost derived from input/output tokens across all nested agent calls.
- **Deflection Rate**: The percentage of tickets fully resolved by the agent without triggering human-in-the-loop escalations.
