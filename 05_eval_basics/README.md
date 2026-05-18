# Module 05: Evaluation Basics & Test Harnesses

## What you will learn
- Deterministic vs semantic evaluation strategies for LLM outputs.
- Writing deterministic evaluation metrics (exact matches, keyword overlaps, regex assertions).
- Implementing an "LLM-as-a-Judge" evaluation model for grading complex agent outputs.
- Creating an automated evaluation run suite and test datasets to score agent updates.

## Files in this folder
- `concept_notes.md` — deterministic vs semantic evaluation paradigms
- `evaluation_guide.md` — operational principles for designing testing benchmarks
- `exercises.md` — guide sheet for exercises
- `starter/` — exercise starter templates
  - `exact_match.py` — starter for standard exact-match and regex grading
  - `regex_match.py` — starter for keyword-based score assertions
  - `semantic_similarity.py` — starter for invoking simulated judge score evaluations
- `solution/` — reference implementations
  - `deterministic_evals.py` — robust exact match, regex, keyword overlap, and clause-containment assertions
  - `llm_as_judge.py` — full LLM-as-a-Judge rubric evaluator with grading guidelines
  - `ab_testing_framework.py` — benchmark pipeline scoring prompt updates against target keys
  - `eval_dataset.json` — version-controlled evaluation gold dataset of test customer tickets
- `tests/` — validation checks
  - `test_deterministic_evals.py` — verifies deterministic validation scoring
  - `test_llm_judge.py` — verifies simulated LLM-as-a-Judge outputs against known grading criteria

## Run order
1. Read `concept_notes.md` and `evaluation_guide.md`
2. Review the structured exercises in `exercises.md`
3. Complete the starter scripts inside `starter/`
4. Run `pytest` to verify your grading algorithms work cleanly
5. Contrast your code structure with the `solution/` implementations

## Success criteria
- Evaluation suite grades customer support summaries based on keyword inclusion and specific billing regex.
- LLM-as-a-Judge compiles a structured grading payload evaluating output safety and helpfulness.
- A/B benchmark runner scores two distinct system prompt iterations and calculates absolute performance gains.

## Common failure modes
- **Evaluating with LLM-as-a-Judge alone**: This introduces noise and higher costs. You should always run deterministic metrics first.
- **Brittle exact-matching**: Exact string comparisons fail due to minor formatting shifts. You must normalize strings (lowercasing, trimming) or use semantic/keyword checks instead.
- **Failing to version-control datasets**: Ad-hoc tests make it impossible to track quality over time. You should always save your gold test cases in a file like `eval_dataset.json`.
