import pytest
import importlib
import sys
import os
from pydantic import ValidationError

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

validated_handoff = importlib.import_module("03_tools_structured_outputs_mcp.solution.validated_handoff")
route_ticket_validated = validated_handoff.route_ticket_validated

pydantic_models = importlib.import_module("03_tools_structured_outputs_mcp.solution.pydantic_models")
TicketExtraction = pydantic_models.TicketExtraction

def test_validated_handoff_success():
    """Verify that a valid ticket routing decision structure processes cleanly."""
    payload = {
        "category": "billing",
        "reason": "Customer needs billing adjustment",
        "confidence": 0.95,
        "escalation_required": False
    }
    res = route_ticket_validated(payload)
    assert "Ticket routed to billing with confidence 0.95" in res

def test_validated_handoff_out_of_bounds_confidence():
    """Verify that confidence ratings exceeding 1.0 are blocked."""
    payload = {
        "category": "refund",
        "reason": "Valid refund",
        "confidence": 1.5,
        "escalation_required": False
    }
    with pytest.raises(ValidationError):
        route_ticket_validated(payload)

def test_ticket_extraction_schema_valid():
    """Verify that a valid log extraction passes Pydantic severity validations."""
    ticket = TicketExtraction(customer_id="CUST-102", severity="HIGH", summary="Database timeout")
    assert ticket.customer_id == "CUST-102"
    assert ticket.severity == "HIGH"

def test_ticket_extraction_schema_invalid_severity():
    """Verify that arbitrary severity strings (e.g. 'URGENT') fail to parse."""
    with pytest.raises(ValidationError):
        TicketExtraction(customer_id="CUST-102", severity="URGENT", summary="Timeout error")
