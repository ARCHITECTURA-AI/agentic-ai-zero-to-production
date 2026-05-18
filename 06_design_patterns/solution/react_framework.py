"""
Solution file for Exercise 6.1.
Implements a highly traceable ReAct core runner that loops through thoughts and actions.
"""
from typing import List, Dict, Any

def run_react_loop(query: str, max_iterations: int = 3) -> Dict[str, Any]:
    """Runs a ReAct execution loop alternating between thoughts, actions, and observations.
    
    Prevents infinite cycles using a strict iteration loop boundary.
    """
    steps = []
    final_answer = ""
    
    for i in range(1, max_iterations + 1):
        if "refund" in query.lower():
            if i == 1:
                thought = "I need to check the validity and status of customer ticket TKT-991."
                action = "lookup_ticket_details(TKT-991)"
                observation = "Ticket TKT-991 exists. Amount: $49.99. Status: Unused."
                steps.append({
                    "iteration": i,
                    "thought": thought,
                    "action": action,
                    "observation": observation
                })
            elif i == 2:
                thought = "Ticket validity confirmed. I will execute the refund tool."
                action = "process_refund(TKT-991, 49.99)"
                observation = "Refund transaction successful. ID: TXN-55102."
                steps.append({
                    "iteration": i,
                    "thought": thought,
                    "action": action,
                    "observation": observation
                })
                final_answer = "Refund of $49.99 successfully processed for ticket TKT-991. Trans ID: TXN-55102."
                break
        else:
            # General system query execution route
            thought = "I must query general databases to resolve the customer's request."
            action = "search_kb(general_info)"
            observation = "Search completed. Found general system status normal."
            steps.append({
                "iteration": i,
                "thought": thought,
                "action": action,
                "observation": observation
            })
            final_answer = "I have reviewed system statuses and everything appears normal. Can I help with anything else?"
            break
            
    if not final_answer:
        final_answer = "ReAct loop reached maximum iteration safety limits without complete resolution."
        
    return {
        "query": query,
        "steps": steps,
        "final_answer": final_answer
    }
