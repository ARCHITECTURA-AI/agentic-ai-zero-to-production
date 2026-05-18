"""
Completed Solution for Module 01 foundations classification task.
"""

def classify_task(
    requires_tools: bool,
    interactive_human_in_loop: bool,
    steps_horizon_greater_than_one: bool
) -> str:
    """Classify corporate systems based on architectural properties.
    
    Rules:
    - If it does not require tools: Return 'chatbot'
    - If it requires tools but runs fully interactively step-by-step with a human: Return 'copilot'
    - If it requires tools, runs over long step horizons, and exhibits high autonomy: Return 'agent'
    """
    if not requires_tools:
        return "chatbot"
        
    if requires_tools and interactive_human_in_loop and not steps_horizon_greater_than_one:
        return "copilot"
        
    if requires_tools and steps_horizon_greater_than_one:
        return "agent"
        
    return "copilot" # Safe fallback
