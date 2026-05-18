import pytest
import importlib
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

human_in_the_loop_hooks = importlib.import_module("06_design_patterns.solution.human_in_the_loop_hooks")
process_action_with_hitl = human_in_the_loop_hooks.process_action_with_hitl
resume_action = human_in_the_loop_hooks.resume_action

def test_hitl_automatic_allow():
    """Verify that low-value transactions complete automatically."""
    state = process_action_with_hitl(action_type="refund", amount=45.00)
    assert state["status"] == "COMPLETED"
    assert "processed automatically" in state["message"]

def test_hitl_pause_gate():
    """Verify that transactions above $100 trigger security pause blocks."""
    state = process_action_with_hitl(action_type="refund", amount=150.00)
    assert state["status"] == "PENDING_APPROVAL"
    assert "exceeds automatic threshold" in state["message"]

def test_hitl_resume_approved():
    """Verify that resuming with 'APPROVED' decision processes the transaction."""
    state = process_action_with_hitl(action_type="refund", amount=150.00)
    res = resume_action(state, human_decision="APPROVED")
    assert "APPROVED" in res
    assert "finalized successfully" in res

def test_hitl_resume_rejected():
    """Verify that resuming with 'REJECTED' decision aborts the transaction."""
    state = process_action_with_hitl(action_type="refund", amount=150.00)
    res = resume_action(state, human_decision="REJECTED")
    assert "REJECTED" in res
    assert "canceled" in res
