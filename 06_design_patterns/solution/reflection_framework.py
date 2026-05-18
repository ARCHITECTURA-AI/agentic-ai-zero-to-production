"""
Solution file for Exercise 6.2.
Self-correction workflow executing draft generation and structured critique refinement loops.
"""
from typing import Dict, Any

def generate_draft(query: str, critique: str = "") -> str:
    """Generates customer email response, adapting style if feedback is supplied."""
    if not critique:
        return "Refund is done. Bye."
    else:
        # Refine draft responding to the critique criteria
        return (
            "Dear Value Support Customer,\n\n"
            "We have successfully finalized processing the refund for your ticket. "
            "The funds should post back to your account within 3-5 business days. "
            "Please reach out if you have further inquiries.\n\n"
            "Sincerely,\n"
            "Customer Response Team"
        )

def reflect_critique(draft: str) -> str:
    """Critiques a draft for corporate compliance, professional tone, and paragraph structures."""
    if "Sincerely" not in draft or len(draft) < 30:
        return (
            "Draft is too brief and lacks a polite corporate closing phrase. "
            "Please expand text and add a formal 'Sincerely' sign-off block."
        )
    return "APPROVED"

def run_reflection_loop(query: str, max_rounds: int = 2) -> Dict[str, Any]:
    """Alternates generation and reflection reviews to achieve optimized text quality."""
    critique = ""
    draft = ""
    history = []
    
    for r in range(1, max_rounds + 1):
        draft = generate_draft(query, critique)
        critique = reflect_critique(draft)
        
        history.append({
            "round": r,
            "draft": draft,
            "critique": critique
        })
        
        if critique == "APPROVED":
            break
            
    return {
        "final_draft": draft,
        "rounds_run": len(history),
        "history": history
    }
