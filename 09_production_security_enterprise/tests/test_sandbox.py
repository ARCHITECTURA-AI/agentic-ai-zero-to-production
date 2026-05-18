import pytest
import importlib
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

secure_sandbox = importlib.import_module("09_production_security_enterprise.solution.secure_sandbox")
run_code_sandbox = secure_sandbox.run_code_sandbox

def test_sandbox_benign_run():
    """Verify that a standard arithmetic script runs successfully."""
    code = "result = 5 * 12"
    res = run_code_sandbox(code)
    
    assert res["status"] == "SUCCESS"
    assert res["output"] == "60"

def test_sandbox_blocked_import():
    """Verify that importing libraries is blocked prior to execution."""
    code = "import os\nresult = os.getcwd()"
    res = run_code_sandbox(code)
    
    assert res["status"] == "BLOCKED"
    assert "Imports are blocked" in res["output"]

def test_sandbox_blocked_forbidden_call():
    """Verify that dangerous functions like 'eval' are blocked prior to execution."""
    code = "result = eval('1 + 1')"
    res = run_code_sandbox(code)
    
    assert res["status"] == "BLOCKED"
    assert "blocked" in res["output"].lower()

def test_sandbox_timeout():
    """Verify that hanging processes trigger safety timeouts."""
    # We can model a loop using a delay that exceeds safety timeout limits
    code = "import time\ntime.sleep(1.0)" 
    # But wait, our auditor blocks 'import time'! That is double-security!
    # Instead, we can simulate an infinite loop
    code = "result = 0\nfor i in range(10000000):\n    result += 1"
    
    # Run with very short timeout of 0.05 seconds
    res = run_code_sandbox(code, timeout_sec=0.05)
    
    assert res["status"] == "TIMEOUT"
    assert "timed out" in res["output"]
