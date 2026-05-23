import pytest
import importlib
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

devops_solution = importlib.import_module("11_capstone.starters.devops_starter")
DevOpsCoordinator = devops_solution.DevOpsCoordinator

def test_capstone_c_success():
    """Verify that healthy incident reporting creates traces and Jira tickets."""
    coord = DevOpsCoordinator()
    incident = {"id": "INC-101", "details": "Database load high"}
    
    res = coord.process_incident(incident)
    
    assert res["status"] == "SUCCESS"
    assert "Enterprise Sync Complete" in res["message"]
    assert coord.client.state == "CLOSED"
    
    # Assert span was recorded
    spans = list(coord.tracer.spans.values())
    assert len(spans) == 1
    assert spans[0].name == "incident_dispatcher"
    assert spans[0].status == "OK"

def test_capstone_c_circuit_breaker():
    """Verify that multiple failures trip the circuit breaker and record errors in traces."""
    coord = DevOpsCoordinator()
    incident = {"id": "INC-102"}
    
    # Trigger 3 failures to trip the circuit breaker
    res = coord.process_incident(incident, simulate_api_failure=True)
    assert res["status"] == "FAILED"
    
    res = coord.process_incident(incident, simulate_api_failure=True)
    res = coord.process_incident(incident, simulate_api_failure=True)
    
    # Verify that the circuit breaker is now OPEN
    assert coord.client.state == "OPEN"
    
    # Next call fails fast via circuit breaker
    res_fast = coord.process_incident(incident)
    assert res_fast["status"] == "FAILED"
    assert "Circuit Breaker is OPEN" in res_fast["error"]
