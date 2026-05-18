# Exercises: Advanced Evaluation & Observability

In this module, you will build a complete, zero-dependency telemetry framework and automated semantic evaluator.

---

## 🏋️ Exercise 8.1: Structuring a Hierarchical Span Tracer

**Location**: `starter/otel_tracer.py` → `solution/tracing_provider.py`
**Goal**: Build a thread-safe nested span tracking engine that records parent-child relationships, tag metadata, and millisecond execution latencies.

**Tasks**:
1. Open `starter/otel_tracer.py` and inspect the `Span` and `Tracer` classes.
2. Implement `start_span(name, parent_id)` which generates a unique span ID and records the start time.
3. Implement `end_span(span_id)` which computes execution duration in milliseconds.
4. Ensure child spans correctly record the parent span's ID.

---

## 🏋️ Exercise 8.2: Faithfulness and Relevance Metric Scorer

**Location**: `starter/eval_pipeline.py` → `solution/eval_framework.py`
**Goal**: Design offline automated metrics to grade response groundedness (Faithfulness) and Query Relevancy without network dependencies.

**Tasks**:
1. Implement `calculate_faithfulness(response, context)` which counts what fraction of claims in the response are found in the source context.
2. Implement `calculate_relevance(response, query)` which scores alignment between response key terms and the original user query.
3. Return structural outputs including floating-point scores and textual justifications.

---

## 🏋️ Exercise 8.3: Aggregating Business Session Costs

**Location**: `solution/eval_framework.py`
**Goal**: Calculate cost aggregates across multi-step execution sessions by summing token counts.

**Tasks**:
1. Add cost tags to spans representing LLM calls (e.g. `input_tokens`, `output_tokens`).
2. Implement `aggregate_session_cost(trace_id)` which traverses the trace graph and returns total pricing (e.g. $0.0015 per 1K input tokens).
