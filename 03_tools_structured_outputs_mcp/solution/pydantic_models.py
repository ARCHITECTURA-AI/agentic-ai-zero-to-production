"""
Solution file for Exercise 3.1 & 3.2 schemas.
Defines complete, validated Pydantic models for extraction.
"""
from typing import Literal
from pydantic import BaseModel, Field

class TicketExtraction(BaseModel):
    """Production schema for extracting core information from raw support logs."""
    customer_id: str = Field(..., min_length=1, description="Unique customer ID")
    severity: Literal['LOW', 'MEDIUM', 'HIGH', 'CRITICAL'] = Field(..., description="Ticket classification level")
    summary: str = Field(..., min_length=5, description="Brief description of the customer issue")
