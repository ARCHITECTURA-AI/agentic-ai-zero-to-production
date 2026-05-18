"""
Solution file for Module 4.
Runtime checker to monitor token utilization metrics and raise alerts on potential prompt bloating.
"""
from typing import Dict, Any
import importlib
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

# Import count_tokens from solution using importlib
token_budget_manager = importlib.import_module("04_memory_rag_context.solution.token_budget_manager")
count_tokens = token_budget_manager.count_tokens

def check_context_health(
    prompt: str, 
    warning_threshold: int = 4000, 
    max_limit: int = 8000,
    model_name: str = "gpt-4"
) -> Dict[str, Any]:
    """Analyzes the current prompt token size and returns context health metrics.
    
    Args:
        prompt: Raw system/user combined prompt.
        warning_threshold: Boundary token count where warnings should trigger.
        max_limit: Strict absolute ceiling token limit of the model context window.
    """
    token_count = count_tokens(prompt, model_name)
    usage_pct = (token_count / max_limit) * 100.0
    
    status = "SAFE"
    if token_count >= max_limit:
        status = "CRITICAL"
    elif token_count >= warning_threshold:
        status = "WARNING"
        
    return {
        "token_count": token_count,
        "max_limit": max_limit,
        "usage_percentage": round(usage_pct, 2),
        "status": status,
        "is_healthy": status != "CRITICAL"
    }
