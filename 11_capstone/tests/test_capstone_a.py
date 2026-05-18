import pytest
import importlib
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

copilot_solution = importlib.import_module("11_capstone.solutions.copilot_solution")
run_copilot = copilot_solution.run_copilot

def test_capstone_a_normal_flow():
    """Verify that a small refund goes through automatically."""
    state = {}
    res = run_copilot("refund my broken mug", state)
    
    assert res["routed_to"] == "refund"
    assert res["status"] == "COMPLETED"
    assert "refund_agent" in res["history"]

def test_capstone_a_hitl_flow():
    """Verify that a high-value refund is gated for human approval."""
    state = {"amount": 250.00} # Seed high amount
    res = run_copilot("refund my broken screen", state)
    
    assert res["routed_to"] == "refund"
    assert res["status"] == "PENDING_APPROVAL"
    assert "human_gate_activated" in res["history"]
