"""
Starter file for Exercise 4.3.
Manage and prune prompt token budgets programmatically to prevent system overflows.
"""
from typing import List, Dict
import tiktoken

def count_tokens(text: str, model_name: str = "gpt-4") -> int:
    """Estimates the exact token count for the given text string."""
    # TODO: Load encoding and count tokens
    return 0

def prune_conversation_history(messages: List[Dict[str, str]], max_tokens: int, model_name: str = "gpt-4") -> List[Dict[str, str]]:
    """Prunes older messages from the history until total tokens fit max_tokens constraint."""
    # TODO: Count tokens of all messages.
    # If total exceeds max_tokens, discard the oldest non-system message and repeat.
    # Keep the system message (first element if role == 'system') locked if possible.
    
    return messages
