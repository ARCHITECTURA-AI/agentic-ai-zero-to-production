"""
Starter file for Exercise 3.2.
Demonstrates the danger of unstructured state handoffs during routing.
"""
from typing import Dict, Any

def route_ticket_unstructured(decision_dict: Dict[str, Any]) -> str:
    """Routes a support ticket using raw, unstructured dictionary parameters.
    
    This function is highly fragile and vulnerable to parameter mismatching.
    """
    # Downstream expects 'category' and 'confidence' (float)
    # But without schema enforcement, upstream might pass mismatched keys like 'dept' or string values.
    category = decision_dict.get("category")
    confidence = decision_dict.get("confidence")
    
    if not category:
        raise ValueError("Routing failed: missing category info.")
        
    # Risky cast that will fail if confidence is not a float or a numeric string
    confidence_val = float(confidence) if confidence is not None else 0.0
    
    return f"Ticket routed to {category} with confidence {confidence_val:.2f}."
