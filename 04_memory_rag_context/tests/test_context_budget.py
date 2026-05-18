import pytest
import importlib
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

token_budget_manager = importlib.import_module("04_memory_rag_context.solution.token_budget_manager")
count_tokens = token_budget_manager.count_tokens
prune_conversation_history = token_budget_manager.prune_conversation_history

context_health_checks = importlib.import_module("04_memory_rag_context.solution.context_health_checks")
check_context_health = context_health_checks.check_context_health

def test_count_tokens():
    """Verify that text token counts are evaluated as non-zero integers."""
    assert count_tokens("Hello, world!") > 0

def test_pruning_retains_system_prompt():
    """Verify that pruning drops old customer interactions but locks system rules."""
    history = [
        {"role": "system", "content": "You are a helpful customer service assistant."},
        {"role": "user", "content": "Hello, my order is extremely delayed and I am angry!"},
        {"role": "assistant", "content": "I apologize. Let me look up your order details."},
        {"role": "user", "content": "Can you check order number 99123?"}
    ]
    
    # Prune to a very tight budget (e.g. 20 tokens)
    # The pruning algorithm should keep the system message and drop older messages
    pruned = prune_conversation_history(history, max_tokens=30, model_name="gpt-4")
    
    # System message must still exist in history
    assert pruned[0]["role"] == "system"
    assert len(pruned) < len(history)

def test_context_health_checks():
    """Verify health status ranges (SAFE, WARNING, CRITICAL) for various inputs."""
    safe_res = check_context_health("A very small prompt", warning_threshold=100, max_limit=200)
    assert safe_res["status"] == "SAFE"
    assert safe_res["is_healthy"] is True
    
    critical_res = check_context_health("A prompt that exceeds the maximum budget", warning_threshold=2, max_limit=4)
    assert critical_res["status"] == "CRITICAL"
    assert critical_res["is_healthy"] is False
