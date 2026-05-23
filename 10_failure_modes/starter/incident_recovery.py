"""
Starter file for Exercise 10.2.
Graceful degradation loop skeleton when primary endpoints fail.
"""
from typing import Dict, Any, Callable

global_ledger = []

def execute_with_fallback(primary_fn: Callable[[], str], fallback_fn: Callable[[], str]) -> Dict[str, Any]:
    """Runs primary action, and on connection outages logs incident and runs fallback."""
    # TODO: Wrap with try-except, write logs, and degrade gracefully.
    return {
        "status": "SUCCESS",
        "output": "Placeholder execution result"
    }
