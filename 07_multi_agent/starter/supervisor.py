"""
Starter file for Exercise 7.1.
Implements the Supervisor/Orchestrator coordinator skeleton.
"""
from typing import Dict, Any

def route_ticket(query: str, state: Dict[str, Any]) -> Dict[str, Any]:
    """Evaluates customer query intent and delegates work to specialist agents.
    
    Args:
        query: Customer query string.
        state: Shared task state dictionary.
    """
    # TODO:
    # 1. Classify query: does it belong to "billing" or "refund"?
    # 2. Extract ticket/account numbers.
    # 3. Call the appropriate agent handler.
    # 4. Enforce hop counter gates.
    
    return {
        "status": "COMPLETED",
        "routed_to": "none",
        "response": "Placeholder response"
    }
