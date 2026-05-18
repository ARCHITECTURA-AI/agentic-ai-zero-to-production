"""
Solution file for Exercise 3.2.
Uses the shared RouterDecision Pydantic model to perform safe, validated handoffs.
"""
from typing import Dict, Any
from shared.models import RouterDecision

def route_ticket_validated(decision_dict: Dict[str, Any]) -> str:
    """Routes a support ticket safely using validated RouterDecision schemas.
    
    Guarantees strict type and value checking before moving the ticket.
    
    Raises:
        ValidationError: If input fails to match RouterDecision requirements.
    """
    # Enforce Pydantic validation boundary
    decision = RouterDecision(**decision_dict)
    
    return f"Ticket routed to {decision.category} with confidence {decision.confidence:.2f}."
