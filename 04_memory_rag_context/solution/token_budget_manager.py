"""
Solution file for Exercise 4.3.
Programmatic prompt pruning and token budget containment manager.
"""
from typing import List, Dict
import tiktoken

def count_tokens(text: str, model_name: str = "gpt-4") -> int:
    """Calculates the exact token footprint of a text block using the model's BPE tokenizer."""
    try:
        encoding = tiktoken.encoding_for_model(model_name)
    except KeyError:
        # Fallback to standard base encoding if target model signature is unspecified
        encoding = tiktoken.get_encoding("cl100k_base")
        
    return len(encoding.encode(text))

def prune_conversation_history(
    messages: List[Dict[str, str]], 
    max_tokens: int, 
    model_name: str = "gpt-4"
) -> List[Dict[str, str]]:
    """Prunes history recursively, discarding oldest user/assistant interactions to satisfy token limits.
    
    Keeps system instruction blocks preserved at all times to prevent agent amnesia.
    """
    working_history = list(messages)
    
    def get_total_history_tokens() -> int:
        # Accumulate token footprints across all current logs in the queue
        return sum(count_tokens(msg.get("content", ""), model_name) for msg in working_history)
        
    # Loop and prune oldest non-system elements until token footprint fits constraints
    while get_total_history_tokens() > max_tokens and len(working_history) > 1:
        pruned_an_item = False
        for idx in range(len(working_history)):
            if working_history[idx].get("role") != "system":
                working_history.pop(idx)
                pruned_an_item = True
                break
                
        if not pruned_an_item:
            # Only system messages are left. Break to avoid wiping out core instructions.
            break
            
    return working_history
