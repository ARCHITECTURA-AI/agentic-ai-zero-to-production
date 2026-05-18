"""
Solution code for Capstone Option A: Enterprise Customer Support Copilot.
Integrates Multi-Agent systems, context matching, and Human-in-the-Loop gating boundaries.
"""
import importlib
import sys
import os
from typing import Dict, Any

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

# Import multi-agent orchestrator using importlib
orchestrator = importlib.import_module("07_multi_agent.solution.orchestrator")
route_ticket = orchestrator.route_ticket

# Import HITL hooks
human_in_the_loop_hooks = importlib.import_module("06_design_patterns.solution.human_in_the_loop_hooks")
process_action_with_hitl = human_in_the_loop_hooks.process_action_with_hitl

def run_copilot(query: str, state: Dict[str, Any]) -> Dict[str, Any]:
    """Runs ticket intent analysis, Specialist routing, and HITL authorization locks."""
    # Capture original amount to prevent Specialist default overrides from wiping it
    orig_amount = state.get("amount", 0.0)

    # 1. Route query to Billing or Refund specialists
    routed_state = route_ticket(query, state)
    
    # Select the maximum specified value between incoming seeds and routing assignments
    amount_to_check = max(orig_amount, routed_state.get("amount", 0.0))

    # 2. Check if a high-value transaction requires Human-in-the-Loop gate verification
    if routed_state.get("routed_to") == "refund" and amount_to_check >= 100.00:
        hitl_state = process_action_with_hitl(action_type="refund", amount=amount_to_check)
        routed_state["status"] = hitl_state["status"]
        routed_state["response"] = hitl_state["message"]
        routed_state["amount"] = amount_to_check
        routed_state["history"].append("human_gate_activated")
    else:
        routed_state["status"] = "COMPLETED"
        routed_state["history"].append("copilot_finalized")

    return routed_state
