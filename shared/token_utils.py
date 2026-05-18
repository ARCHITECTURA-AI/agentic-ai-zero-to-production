import tiktoken
from typing import List, Dict, Any

def count_tokens(text: str, model_name: str = "gpt-4o-mini") -> int:
    """Compute the number of tokens in a text block utilizing tiktoken.
    
    Falls back gracefully if the encoding name is not recognized.
    """
    try:
        # Standard lookup logic
        encoding = tiktoken.encoding_for_model(model_name)
    except KeyError:
        # Default fallback
        encoding = tiktoken.get_encoding("cl100k_base")
        
    return len(encoding.encode(text))

def count_messages_tokens(messages: List[Dict[str, Any]], model_name: str = "gpt-4o-mini") -> int:
    """Compute overall tokens consumed by a structured ChatGPT messages payload list."""
    total_tokens = 0
    for message in messages:
        # Count standard fields
        content = message.get("content", "") or ""
        total_tokens += count_tokens(content, model_name)
        total_tokens += 4  # overhead for metadata wrappers
    total_tokens += 3  # reply start overhead
    return total_tokens

def check_token_budget(prompt: str, max_budget: int = 4000, model_name: str = "gpt-4o-mini") -> bool:
    """Ensure that the prompt text does not exceed the allotted token budget boundary."""
    return count_tokens(prompt, model_name) <= max_budget
