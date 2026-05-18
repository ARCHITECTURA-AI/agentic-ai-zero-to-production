"""
Starter file for Exercise 8.2.
Implements modular evaluations including groundness/faithfulness calculations.
"""
from typing import Dict, Any

def calculate_faithfulness(response: str, context: str) -> Dict[str, Any]:
    """Evaluates whether the response is fully grounded in the provided context.
    
    Returns:
        A dictionary containing the float 'score' (0.0 to 1.0) and a string 'reason'.
    """
    # TODO: Calculate grounding overlap metric.
    return {
        "score": 0.0,
        "reason": "Not implemented"
    }

def calculate_relevance(response: str, query: str) -> Dict[str, Any]:
    """Evaluates whether the response directly answers the customer query.
    
    Returns:
        A dictionary containing the float 'score' (0.0 to 1.0) and a string 'reason'.
    """
    # TODO: Calculate query relevancy metric.
    return {
        "score": 0.0,
        "reason": "Not implemented"
    }
