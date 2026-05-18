# Module 08: Advanced Evaluation & Observability

## What you will learn
- Structuring nested agent traces with hierarchical span IDs (OpenTelemetry concepts).
- Capturing runtime errors, inputs, outputs, and token latencies inside traces.
- Automated LLM evaluation techniques: Faithfulness, Answer Relevance, and Semantic Hallucination detection.
- Implementing business-level KPIs (e.g. Cost per Session, Success Rate).

## Files in this folder
- `concept_notes.md` — Core concepts of agent tracing (spans, tags, parent relationships) and advanced evaluators
- `exercises.md` — instructions to build tracing systems and semantic scorers
- `starter/` — exercise starter templates
  - `otel_tracer.py` — hierarchical trace logger skeleton
  - `eval_pipeline.py` — faithfulness & relevance metric scorer skeleton
- `solution/` — reference implementations
  - `tracing_provider.py` — fully functioning nested span logger and exporter
  - `eval_framework.py` — modular offline LLM evaluators scoring faithfulness and relevance
  - `prompts/eval_judges.txt` — reference structured grading prompts for LLM-as-a-Judge evaluators
- `tests/` — validation checks
  - `test_traces.py` — verifies spans, latencies, and hierarchy logic
  - `test_eval_metrics.py` — verifies that correctness and hallucination checkers score correctly

## Run order
1. Read `concept_notes.md`
2. Follow instructions in `exercises.md`
3. Edit files in `starter/`
4. Run `pytest` to confirm your tracing and scoring loops pass tests
5. Compare your design against `solution/`

## Success criteria
- Nested functions generate child spans containing the exact parent span ID.
- Trace logs track precise millisecond start/end timestamps and calculate run latencies.
- The evaluation engine accurately scores high-faithfulness vs low-faithfulness texts.

## Common failure modes
- **Disconnected traces**: Losing parent span IDs inside async boundaries or multi-thread pools, resulting in orphan traces. You must pass tracing context explicitly or use thread-local state.
- **Trace volume overhead**: Logging excessively detailed spans in high-throughput production environments, raising IO latency. You should use asynchronous exporters or batching.
- **Biased evaluations**: Over-relying on LLM judges without deterministic fallback scores, yielding noisy metrics. You should combine deterministic checks with semantic scorers.
