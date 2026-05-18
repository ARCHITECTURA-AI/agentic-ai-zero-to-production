"""
Starter file for Exercise 6.3.
Enforce security barriers with Human-in-the-Loop manual authorization checks.
"""
from typing import Dict, Any

def process_action_with_hitl(action_type: str, amount: float) -> Dict[str, Any]:
    """Inspects actions and requests human approval if bounds are breached."""
    # TODO:
    # 1. If action_type is "refund" and amount exceeds $100.0, pause the loop.
    # 2. Return state dictionary indicating "PENDING_APPROVAL".
    # 3. Otherwise, return "COMPLETED".
    
    return {}

def resume_action(serialized_state: Dict[str, Any], human_decision: str) -> str:
    """Resumes a paused action based on manual human feedback ('APPROVED' or 'REJECTED')."""
    # TODO: Process the state depending on the human decision.
    return "Status"
