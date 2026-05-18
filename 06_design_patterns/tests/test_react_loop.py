import pytest
import importlib
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

react_framework = importlib.import_module("06_design_patterns.solution.react_framework")
run_react_loop = react_framework.run_react_loop

def test_react_loop_refund():
    """Verify that a refund query successfully cycles through ticket validations and refunds."""
    res = run_react_loop("Can I get a refund please?", max_iterations=3)
    
    assert res["query"] == "Can I get a refund please?"
    assert len(res["steps"]) == 2
    assert "TKT-991" in res["steps"][0]["action"]
    assert "process_refund" in res["steps"][1]["action"]
    assert "Refund of $49.99 successfully processed" in res["final_answer"]

def test_react_loop_limit():
    """Verify that tight max iteration limits prevent excessive cycling."""
    res = run_react_loop("Can I get a refund please?", max_iterations=1)
    
    assert len(res["steps"]) == 1
    assert "safety limits" in res["final_answer"]
