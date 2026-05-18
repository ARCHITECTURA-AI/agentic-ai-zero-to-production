"""
Solution code for Capstone Option B: Sandboxed Autonomous Data Analyst.
Leverages the AST-audited and timed sandbox environment to process mathematical operations securely.
"""
import importlib
import sys
import os
from typing import Dict, Any

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

# Import the secure sandbox using importlib
secure_sandbox = importlib.import_module("09_production_security_enterprise.solution.secure_sandbox")
run_code_sandbox = secure_sandbox.run_code_sandbox

def run_analyst(code_str: str) -> Dict[str, Any]:
    """Runs data processing requests inside the security-hardened thread-timed sandbox."""
    return run_code_sandbox(code_str, timeout_sec=0.2)
