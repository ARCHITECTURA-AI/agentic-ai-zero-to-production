"""
Starter file for Exercise 3.1 & 3.2 schemas.
Defines skeletons for custom Pydantic V2 extraction models.
"""
from pydantic import BaseModel, Field

class TicketExtraction(BaseModel):
    """Starter schema for extracting core information from raw support logs."""
    # TODO: Define fields
    # - customer_id: str (must not be empty)
    # - severity: str (must be one of 'LOW', 'MEDIUM', 'HIGH', 'CRITICAL')
    # - summary: str
    pass
