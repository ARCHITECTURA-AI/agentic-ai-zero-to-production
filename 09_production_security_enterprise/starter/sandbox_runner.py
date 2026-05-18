"""
Starter file for Exercise 9.1.
Implements restricted execution boundaries and timeout guards.
"""
from typing import Dict, Any

def run_code_sandbox(code_str: str, timeout_sec: float = 0.5) -> Dict[str, Any]:
    """Runs a Python script string inside an isolated sandbox with a execution timeout.
    
    Returns:
        A dictionary containing "status" (SUCCESS, TIMEOUT, or BLOCKED) and "output".
    """
    # TODO:
    # 1. Strip access to dangerous builtins.
    # 2. Spawn and run the code.
    # 3. Enforce timeout gates.
    return {
        "status": "SUCCESS",
        "output": "Placeholder execution output"
    }
