import pytest
import importlib
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

orchestrator = importlib.import_module("07_multi_agent.solution.orchestrator")
route_ticket = orchestrator.route_ticket

def test_supervisor_routes_to_billing():
    """Verify that a query detailing billing double-charges routes to billing specialist."""
    state = {}
    res = route_ticket("My account was charged twice. Help please.", state)
    
    assert res["routed_to"] == "billing"
    assert res["status"] == "RESOLVED"
    assert "Billing Specialist" in res["response"]
    assert "billing_agent" in res["history"]

def test_supervisor_routes_to_refund():
    """Verify that a query requesting ticket refunds routes to refund specialist."""
    state = {}
    res = route_ticket("I need a refund for my delayed flight.", state)
    
    assert res["routed_to"] == "refund"
    assert res["status"] == "RESOLVED"
    assert "Refund Specialist" in res["response"]
    assert "refund_agent" in res["history"]

def test_supervisor_resolves_inline():
    """Verify that a generic question is handled directly by the supervisor without routing."""
    state = {}
    res = route_ticket("What are your business hours?", state)
    
    assert res["routed_to"] == "none"
    assert res["status"] == "RESOLVED"
    assert "working hours" in res["response"]
    assert "supervisor_direct" in res["history"]
