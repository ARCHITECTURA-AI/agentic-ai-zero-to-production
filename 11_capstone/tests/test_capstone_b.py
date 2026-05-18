import pytest
import importlib
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

analyst_solution = importlib.import_module("11_capstone.solutions.analyst_solution")
run_analyst = analyst_solution.run_analyst

def test_capstone_b_success():
    """Verify that a simple arithmetic script runs successfully."""
    code = "result = 12 * 12"
    res = run_analyst(code)
    
    assert res["status"] == "SUCCESS"
    assert res["output"] == "144"

def test_capstone_b_blocked():
    """Verify that imports are safely blocked by the analyst sandbox."""
    code = "import sys\nresult = sys.platform"
    res = run_analyst(code)
    
    assert res["status"] == "BLOCKED"
    assert "Imports are blocked" in res["output"]
