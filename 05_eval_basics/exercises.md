# Exercises: Prompt Evaluations & Benchmarking

In this module, you will design deterministic scoring mechanisms and implement an automated benchmark test suite.

---

## 🏋️ Exercise 5.1: Deterministic Grading Assertions

**Location**: `starter/exact_match.py` and `starter/regex_match.py`
**Goal**: Write quick, zero-cost deterministic scoring checks to evaluate ticket classifications and output safety guidelines.

**Tasks**:
1. Implement exact match comparison logic that normalizes whitespace and capitalization.
2. Implement a keyword scanner that calculates the overlap ratio between the actual agent output and a required keywords list.
3. Write a regex assertion scanner that verifies ticket IDs (`TKT-\d{5}`) or refund references are present in the response.

---

## 🏋️ Exercise 5.2: LLM-as-a-Judge Rubric Grader

**Location**: `starter/semantic_similarity.py` → `solution/llm_as_judge.py`
**Goal**: Implement a robust grading rubric where a highly capable LLM reviews support transcripts for helpfulness, tone, and correctness.

**Tasks**:
1. Define a structured grading output using Pydantic.
2. Formulate the evaluation system prompt (enforcing a reasoning explanation first, followed by a score from 1-5).
3. Connect a mock LLM provider interface to simulate the evaluation response cleanly during test cycles.

---

## 🏋️ Exercise 5.3: Gold Benchmarks and A/B Testing

**Location**: `solution/ab_testing_framework.py`
**Goal**: Score two separate agent prompt versions (Version A vs Version B) across a gold dataset (`eval_dataset.json`) to confirm quality improvements.

**Tasks**:
1. Load the Gold Dataset from `eval_dataset.json`.
2. Grade outputs from both prompt iterations using the deterministic and semantic functions you built.
3. Output a detailed report printing average scores and success metrics to track prompt performance gains.
