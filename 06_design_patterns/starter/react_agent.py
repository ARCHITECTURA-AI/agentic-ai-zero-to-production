"""
Starter file for Exercise 6.1.
Implements the ReAct (Reasoning + Action) execution loop skeleton.
"""
from typing import List, Dict, Any

def run_react_loop(query: str, max_iterations: int = 3) -> Dict[str, Any]:
    """Runs a ReAct cycle that alternates thoughts, actions, and observations.
    
    Args:
        query: Customer issue string.
        max_iterations: Safety limit to prevent infinite loops.
    """
    # TODO:
    # 1. Initialize message history list.
    # 2. Iterate up to max_iterations.
    # 3. Formulate Thought, pick a tool Action, retrieve Observation.
    # 4. Terminate cleanly with a Final Answer.
    
    steps = []
    
    # Write ReAct loop here:
    
    return {
        "query": query,
        "steps": steps,
        "final_answer": "Placeholder final answer"
    }
