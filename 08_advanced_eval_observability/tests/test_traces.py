import pytest
import importlib
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

tracing_provider = importlib.import_module("08_advanced_eval_observability.solution.tracing_provider")
Tracer = tracing_provider.Tracer

def test_tracer_spans():
    """Verify that starting and ending spans computes correct durations."""
    tracer = Tracer()
    s = tracer.start_span("test_span")
    
    assert s.span_id in tracer.spans
    assert s.status == "UNFINISHED"
    
    tracer.end_span(s.span_id, status="OK", tags={"model": "gemini-flash"})
    
    assert s.status == "OK"
    assert s.tags["model"] == "gemini-flash"
    assert s.duration_ms >= 0.0

def test_tracer_hierarchy():
    """Verify that parent-child nested structures maintain traceable link keys."""
    tracer = Tracer()
    parent = tracer.start_span("orchestrator")
    child = tracer.start_span("tool_call", parent_id=parent.span_id)
    
    assert child.parent_id == parent.span_id
    
    children = tracer.get_child_spans(parent.span_id)
    assert len(children) == 1
    assert children[0].span_id == child.span_id

def test_tracer_cost_aggregation():
    """Verify that multi-span session pricing matches expected rates."""
    tracer = Tracer()
    s1 = tracer.start_span("call_1")
    tracer.end_span(s1.span_id, tags={"input_tokens": 1000, "output_tokens": 500})
    
    s2 = tracer.start_span("call_2")
    tracer.end_span(s2.span_id, tags={"input_tokens": 2000, "output_tokens": 1000})
    
    # Cost math:
    # (3000 * 0.0000015) + (1500 * 0.0000020) = 0.0045 + 0.0030 = 0.0075
    cost = tracer.aggregate_session_cost()
    assert abs(cost - 0.0075) < 1e-6
