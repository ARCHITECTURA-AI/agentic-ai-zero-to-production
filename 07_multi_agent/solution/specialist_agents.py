"""
Solution file for Exercise 7.2.
Specialist agents for processing targeted domains (billing and refunds) with handshake logs.
"""
from typing import Dict, Any

def handle_billing_inquiry(state: Dict[str, Any]) -> Dict[str, Any]:
    """Resolves account billing disputes and writes update traces to the state."""
    account_id = state.get("account_id", "ACC-UNKNOWN")
    
    # Process billing dispute logic
    state["status"] = "RESOLVED"
    state["response"] = f"Billing Specialist: Secondary charge reversed successfully for billing account {account_id}."
    state["history"].append("billing_agent")
    
    return state

def handle_refund_inquiry(state: Dict[str, Any]) -> Dict[str, Any]:
    """Resolves ticket refund transactions and writes update traces to the state."""
    ticket_id = state.get("ticket_id", "TKT-UNKNOWN")
    amount = state.get("amount", 0.00)
    
    # Process refund transaction logic
    state["status"] = "RESOLVED"
    state["response"] = f"Refund Specialist: Refund of ${amount:.2f} processed successfully for ticket {ticket_id}."
    state["history"].append("refund_agent")
    
    return state
