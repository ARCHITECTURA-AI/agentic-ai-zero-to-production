"""
Solution file for Exercise 6.3.
Security validation checkpoints implementing Human-in-the-Loop approval workflows.
"""
from typing import Dict, Any

def process_action_with_hitl(action_type: str, amount: float) -> Dict[str, Any]:
    """Inspects refund payloads and pauses execution for manual approvals if above thresholds."""
    if action_type == "refund" and amount > 100.00:
        return {
            "status": "PENDING_APPROVAL",
            "action_type": action_type,
            "amount": amount,
            "message": f"Refund of ${amount:.2f} exceeds automatic threshold of $100.00. Execution paused."
        }
        
    return {
        "status": "COMPLETED",
        "action_type": action_type,
        "amount": amount,
        "message": f"Refund of ${amount:.2f} processed automatically."
    }

def resume_action(serialized_state: Dict[str, Any], human_decision: str) -> str:
    """Resumes execution from a serialized snapshot based on the reviewer decision ('APPROVED'/'REJECTED')."""
    if serialized_state.get("status") != "PENDING_APPROVAL":
        return f"Error: Attempted to resume a process that was not paused. State: {serialized_state.get('status')}"
        
    amount = serialized_state.get("amount", 0.00)
    decision_clean = human_decision.upper().strip()
    
    if decision_clean == "APPROVED":
        return f"Transaction APPROVED. Refund of ${amount:.2f} finalized successfully."
    elif decision_clean == "REJECTED":
        return f"Transaction REJECTED. Refund of ${amount:.2f} has been canceled."
    else:
        return f"Transaction remains PENDING. Unknown decision: '{human_decision}'."
