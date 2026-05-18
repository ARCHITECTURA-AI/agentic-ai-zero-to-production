# Operational Guide: Designing Quality AI Evaluation Pipelines

To avoid shipping buggy or toxic prompts to production, follow this production-ready blueprint to establish automated evaluation pipelines.

---

## 1. Five Principles for Designing Rubrics

1. **Be Binary Where Possible**: Yes/No checks (e.g. "Did the agent apologize?") are graded far more consistently by LLMs than numeric scales (e.g. "Grade empathy from 1-10").
2. **Context-Insulated Inputs**: Provide the evaluator only with the specific question, context, and output—never let it know which prompt iteration generated the response to prevent bias.
3. **Reference-Anchored Grading**: Always provide a "gold standard" reference solution. It is much easier for an LLM to compare an answer to a model key than to grade it in a vacuum.
4. **Include a "Reasoning" Chain**: Force the model to output a detailed rationale before the final score. This forces the model to analyze details instead of guessing.
5. **Enforce JSON schemas**: Always query the judge model with a Pydantic structure to facilitate automated tracking of regression scores.

---

## 2. CI/CD Integration Best Practices

In modern enterprise architectures, evaluations run automatically on every commit:
- **Smoke Tests**: Run 5 quick deterministic checks on pull requests. These should execute in less than 5 seconds.
- **Full Regressions**: Run the complete Gold Dataset (100+ cases) during release schedules or weekly builds.
- **Budget Alerts**: Block deployments if the average score falls below a critical threshold (e.g., average helpfulness drops from 4.8 to 4.2).

```
[Developer pushes code] ──► [GitHub Actions CI] ──► [Execute Deterministic Evals] 
                                                               │
    ┌─────────────────────── Pass ◄────────────────────────────┘
    ▼
[Execute LLM-as-a-Judge Evals] ──► [Pass: Merge PR]
    │
    ▼ Fail
[Block Deployment & Notify]
```
