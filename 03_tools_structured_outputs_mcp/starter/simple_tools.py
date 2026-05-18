"""
Starter file for Exercise 3.1.
Enforce runtime type validation using Pydantic schemas.
"""
from typing import Dict, Any

# TODO: Define a Pydantic V2 model RefundArgs
# - ticket_id: str
# - amount: float (must be greater than 0.0)

def process_refund_tool(arguments: Dict[str, Any]) -> str:
    """Executes a refund for a ticket.
    
    Arguments must be validated against RefundArgs.
    """
    # TODO: Validate incoming arguments using the RefundArgs model.
    # If invalid, let the Pydantic ValidationError propagate.
    
    # Simple mock execution
    ticket_id = arguments.get("ticket_id")
    amount = arguments.get("amount")
    
    return f"Refund of ${amount:.2f} processed successfully for ticket {ticket_id}."
