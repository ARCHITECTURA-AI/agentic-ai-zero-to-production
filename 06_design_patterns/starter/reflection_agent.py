"""
Starter file for Exercise 6.2.
Self-correction design pattern using Generator-Reflector critique iterations.
"""
from typing import Dict, Any

def generate_draft(query: str, critique: str = "") -> str:
    """Drafts a response email to a customer ticket, incorporating optional critique."""
    # TODO: Generate draft string. If critique is present, adjust the response.
    return "Draft response"

def reflect_critique(draft: str) -> str:
    """Analyzes a draft and suggests specific styling or detail changes."""
    # TODO: Inspect the draft and return improvement advice.
    return "Critique comments"

def run_reflection_loop(query: str, max_rounds: int = 2) -> Dict[str, Any]:
    """Alternates draft generation and critique to iteratively refine outcomes."""
    # TODO: Run generation and critique cycles.
    
    return {
        "final_draft": "Final refined draft"
    }
