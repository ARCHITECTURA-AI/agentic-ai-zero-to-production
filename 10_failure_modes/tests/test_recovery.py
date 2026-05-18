import pytest
import importlib
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

recovery_playbook = importlib.import_module("10_failure_modes.solution.recovery_playbook")
execute_with_fallback = recovery_playbook.execute_with_fallback
global_ledger = recovery_playbook.global_ledger

def test_recovery_normal_operation():
    """Verify that under healthy conditions the primary function runs successfully."""
    primary = lambda: "Primary System Resolution"
    fallback = lambda: "Backup Local Response"
    
    res = execute_with_fallback(primary, fallback)
    
    assert res["status"] == "SUCCESS"
    assert res["output"] == "Primary System Resolution"
    assert res["degraded"] is False

def test_recovery_failover_degradation():
    """Verify that network outages trigger automatic fallback failovers and record incident logs."""
    def primary_fail():
        raise ConnectionError("LLM API Timeout: Server 503 Outage")
        
    fallback = lambda: "Backup Local Response"
    
    initial_log_count = len(global_ledger.incidents)
    
    res = execute_with_fallback(primary_fail, fallback)
    
    assert res["status"] == "DEGRADED"
    assert res["output"] == "Backup Local Response"
    assert res["degraded"] is True
    assert "Server 503 Outage" in res["error_logged"]
    
    # Assert incident was recorded in global ledger
    assert len(global_ledger.incidents) == initial_log_count + 1
    assert "Outage triggered" in global_ledger.incidents[-1]["error"]
