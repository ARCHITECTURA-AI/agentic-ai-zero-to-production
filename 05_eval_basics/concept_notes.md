# Concept Notes: Evaluation Basics & Test Harnesses

In traditional software, we verify logic using deterministic assertions (e.g. `assert add(2, 3) == 5`). In generative agentic AI, outputs are non-deterministic, text-heavy, and free-form. We must use a combination of deterministic and semantic metrics to verify quality.

---

## 1. Deterministic Evaluations

Before spending money on expensive LLM calls or complex setup, always deploy **Deterministic Evals**. They are fast, 100% reliable, and cost nothing:
- **Exact Match**: Verifies whether an output matches a target label precisely (useful for short codes, routing categories, or classification targets).
- **Regex Containment**: Asserts that key patterns (e.g. ticket numbers `TKT-\d+`, email patterns, phone formats) appear in the response.
- **Keyword Overlap**: Computes the percentage of domain-specific keywords (e.g. refund, billing, corporate names) found in the text.
- **Negative Assertions**: Checks for the absolute absence of restricted words (e.g. profanities, competitors, or sensitive labels).

---

## 2. Semantic & LLM-as-a-Judge Evaluations

When checking for tone, empathy, safety, or complex accuracy, deterministic keywords fall short. We utilize:
- **Embedding Distance**: Encodes target text and generated output to measure vector similarity (e.g., Cosine Similarity). If the score is high (e.g., $>0.85$), the meaning is aligned.
- **LLM-as-a-Judge**: Employs a highly capable model (like GPT-4 or Gemini Pro) as an automated evaluator. The model is given a strict rubric and grades the agent's output based on helpfulness, accuracy, and compliance.

### The LLM-as-a-Judge Rubric Pattern
To ensure the LLM-as-a-Judge grades reliably and does not hallucinate, we must enforce a structured grading schema:
1. **Explain the thought process**: Force the model to write a chain-of-thought justification first.
2. **Assign a score**: Define explicit grades (e.g. 1 to 5) with concrete criteria for each point.
3. **Structured Format**: Return the response as a JSON object (e.g. using Pydantic validation).

---

## 3. Gold Datasets & Benchmarks

A **Gold Dataset** is a version-controlled repository of typical queries, representative customer issues, and expected outcomes. 
When developers modify system prompts, change tools, or swap foundational models:
1. The test harness runs the updated agent over the entire Gold Dataset.
2. It scores each response against the targets.
3. It prints a comparison report (A/B score delta) to ensure changes do not cause performance regressions.
