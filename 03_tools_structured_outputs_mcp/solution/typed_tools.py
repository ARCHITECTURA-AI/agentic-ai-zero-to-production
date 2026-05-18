"""
Solution file for Exercise 3.1.
Enforces runtime validation using a strict Pydantic schema.
"""
from typing import Dict, Any
from pydantic import BaseModel, Field

class RefundArgs(BaseModel):
    """Schema defining parameters required for ticket refund operations."""
    ticket_id: str = Field(..., min_length=3, description="Unique identifier for the ticket")
    amount: float = Field(..., gt=0.0, description="Amount in USD to be refunded")

def process_refund_tool(arguments: Dict[str, Any]) -> str:
    """Executes a refund for a ticket after validating parameters.
    
    Raises:
        ValidationError: If arguments do not conform to RefundArgs schema rules.
    """
    # Force runtime validation
    args = RefundArgs(**arguments)
    
    # Process with validated attributes
    return f"Refund of ${args.amount:.2f} processed successfully for ticket {args.ticket_id}."
