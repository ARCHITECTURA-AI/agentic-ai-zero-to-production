import pytest
import importlib
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

orchestrator = importlib.import_module("07_multi_agent.starter.supervisor")
route_ticket = orchestrator.route_ticket

def test_handshake_state_preservation():
    """Verify that case details are safely loaded into the shared state payload."""
    state = {}
    res = route_ticket("refund my ticket", state)
    
    assert res["ticket_id"] == "TKT-4412"
    assert res["amount"] == 85.00
    assert "refund_agent" in res["history"]

def test_ping_pong_hop_defense():
    """Verify that routing transitions exceeding 3 hops escalate directly to managers."""
    # Seed state with high hop count
    state = {
        "hop_count": 3,
        "history": ["agent_a", "agent_b", "agent_c"]
    }
    
    res = route_ticket("billing charge dispute", state)
    
    assert res["status"] == "ESCALATED"
    assert "Hop count safety limit" in res["response"] or "Infinite loop" in res["response"]
    assert "supervisor_escalation" in res["history"]
