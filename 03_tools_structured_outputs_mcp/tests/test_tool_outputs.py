import pytest
import importlib
import sys
import os
from pydantic import ValidationError

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

typed_tools = importlib.import_module("03_tools_structured_outputs_mcp.solution.typed_tools")
process_refund_tool = typed_tools.process_refund_tool

def test_refund_tool_success():
    """Verify that a well-structured refund argument payload completes successfully."""
    payload = {"ticket_id": "TKT-991", "amount": 49.99}
    res = process_refund_tool(payload)
    assert "Refund of $49.99 processed successfully" in res

def test_refund_tool_invalid_amount():
    """Verify that a negative refund amount is blocked by validation gates."""
    payload = {"ticket_id": "TKT-991", "amount": -10.00}
    with pytest.raises(ValidationError):
        process_refund_tool(payload)

def test_refund_tool_missing_params():
    """Verify that omitting required parameters is correctly flagged by schemas."""
    payload = {"amount": 25.00}
    with pytest.raises(ValidationError):
        process_refund_tool(payload)
