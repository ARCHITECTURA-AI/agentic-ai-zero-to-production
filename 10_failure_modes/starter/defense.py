"""
Starter file for Exercise 10.1.
Implements input/output guardrail checks for prompt injection and leak preventions.
"""

def is_safe_input(prompt: str) -> bool:
    """Scans the user query prompt for injection attempts.
    
    Returns:
        True if the prompt is safe, False if blocked.
    """
    # TODO: Build regex or check strings for instruction override hacks.
    return True

def sanitize_output(response: str) -> str:
    """Scans response content for private system variables and sanitizes them."""
    # TODO: Intercept and redact secret keys from being leaked.
    return response
