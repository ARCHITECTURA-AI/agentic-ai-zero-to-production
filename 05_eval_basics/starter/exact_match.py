"""
Starter file for Exercise 5.1.
Write deterministic exact-match routing classification graders.
"""
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

def grade_routing_decision(prediction: str, target: str) -> bool:
    """Verifies that the agent's predicted routing matches the target exactly.
    
    Should be case-insensitive and ignore surrounding whitespace.
    """
    # TODO: Normalize both inputs and verify equality.
    return False
