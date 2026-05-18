"""
Solution file for Exercise 7.1 & 7.3.
Supervisor orchestrator coordinating specialist assignment, state handshakes, and hop limits.
"""
import importlib
import sys
import os
from typing import Dict, Any

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

specialist_agents = importlib.import_module("07_multi_agent.solution.specialist_agents")
handle_billing_inquiry = specialist_agents.handle_billing_inquiry
handle_refund_inquiry = specialist_agents.handle_refund_inquiry

def route_ticket(query: str, state: Dict[str, Any]) -> Dict[str, Any]:
    """Classifies user intent, delegates task to specialist agents, and counts state hops."""
    # 1. Initialize empty state fields if not present
    if "hop_count" not in state:
        state["hop_count"] = 0
    if "history" not in state:
        state["history"] = []
        
    # 2. Enforce ping-pong loop defense. Limit transitions to a maximum of 3 hops.
    if state["hop_count"] >= 3:
        state["status"] = "ESCALATED"
        state["response"] = "Supervisor: Infinite loop pattern identified. Escalating ticket to Customer Manager."
        state["history"].append("supervisor_escalation")
        return state
        
    # Increment transition count
    state["hop_count"] += 1
    
    query_lower = query.lower()
    
    # 3. Dynamic Specialist Routing & State Handshake Parsing
    if "billing" in query_lower or "charge" in query_lower:
        state["routed_to"] = "billing"
        state["account_id"] = "ACC-99182"
        # Delegate to billing specialist
        return handle_billing_inquiry(state)
        
    elif "refund" in query_lower:
        state["routed_to"] = "refund"
        state["ticket_id"] = "TKT-4412"
        state["amount"] = 85.00
        # Delegate to refund specialist
        return handle_refund_inquiry(state)
        
    else:
        # Resolve inline without delegating to specialists
        state["status"] = "RESOLVED"
        state["routed_to"] = "none"
        state["response"] = "Supervisor: Answered customer query regarding standard office working hours."
        state["history"].append("supervisor_direct")
        return state
