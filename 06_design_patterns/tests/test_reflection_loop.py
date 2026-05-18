import pytest
import importlib
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

reflection_framework = importlib.import_module("06_design_patterns.solution.reflection_framework")
run_reflection_loop = reflection_framework.run_reflection_loop

def test_reflection_loop_refinement():
    """Verify that reflection loops critique informal text and output polite refined text."""
    res = run_reflection_loop("Refund me", max_rounds=3)
    
    assert res["rounds_run"] == 2
    assert "Dear Value Support Customer" in res["final_draft"]
    assert "Sincerely" in res["final_draft"]
    
    # Assert history recorded the journey
    history = res["history"]
    assert history[0]["critique"] != "APPROVED"
    assert history[1]["critique"] == "APPROVED"
