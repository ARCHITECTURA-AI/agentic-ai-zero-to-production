import pytest
import importlib
import sys
import os
import time

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

enterprise_connector = importlib.import_module("09_production_security_enterprise.starter.enterprise_client")
EnterpriseClient = enterprise_connector.EnterpriseClient
CircuitBreakerError = enterprise_connector.CircuitBreakerError

def test_circuit_breaker_flow():
    """Verify that consecutive failures trip the circuit breaker state to OPEN."""
    client = EnterpriseClient(failure_threshold=3, cooloff_period_sec=0.1)
    
    # CLOSED state initially
    assert client.state == "CLOSED"
    
    # First 2 simulated failures shouldn't trip
    with pytest.raises(ConnectionError):
        client.call_service({"ticket_id": "TKT-100"}, simulate_failure=True)
    assert client.state == "CLOSED"
    
    with pytest.raises(ConnectionError):
        client.call_service({"ticket_id": "TKT-100"}, simulate_failure=True)
    assert client.state == "CLOSED"
    
    # 3rd failure trips the circuit
    with pytest.raises(ConnectionError):
        client.call_service({"ticket_id": "TKT-100"}, simulate_failure=True)
    assert client.state == "OPEN"
    
    # Consecutive calls immediately reject without hitting downstream service
    with pytest.raises(CircuitBreakerError):
        client.call_service({"ticket_id": "TKT-100"})

def test_circuit_breaker_recovery():
    """Verify that after cooling downtime, the circuit changes to HALF-OPEN and can recover."""
    client = EnterpriseClient(failure_threshold=2, cooloff_period_sec=0.05)
    
    with pytest.raises(ConnectionError):
        client.call_service({"ticket_id": "1"}, simulate_failure=True)
    with pytest.raises(ConnectionError):
        client.call_service({"ticket_id": "1"}, simulate_failure=True)
        
    assert client.state == "OPEN"
    
    # Wait for cooloff period to expire
    time.sleep(0.06)
    
    # Calling service now triggers recovery path
    res = client.call_service({"ticket_id": "TKT-200"})
    assert res["status"] == "SUCCESS"
    assert client.state == "CLOSED"
