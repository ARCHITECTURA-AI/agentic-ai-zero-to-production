"""
Solution code for Capstone Option C: Resilient DevOps Incident Coordinator.
Coordinates incident tracing telemetry and registers API syncs through a Circuit Breaker client.
"""
import importlib
import sys
import os
from typing import Dict, Any

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

# Import Tracer using importlib
tracing_provider = importlib.import_module("08_advanced_eval_observability.solution.tracing_provider")
Tracer = tracing_provider.Tracer

# Import Enterprise Client using importlib
enterprise_connector = importlib.import_module("09_production_security_enterprise.solution.enterprise_connector")
EnterpriseClient = enterprise_connector.EnterpriseClient
CircuitBreakerError = enterprise_connector.CircuitBreakerError

class DevOpsCoordinator:
    """Enterprise Incident Response Coordinator combining Tracing and Circuit Breakers."""
    def __init__(self):
        self.tracer = Tracer()
        self.client = EnterpriseClient(failure_threshold=3, cooloff_period_sec=0.5)

    def process_incident(self, incident_details: Dict[str, Any], simulate_api_failure: bool = False) -> Dict[str, Any]:
        """Traces the incoming incident and dispatches ticket logs to Jira using circuit breakers."""
        # 1. Start parent span tracking
        span = self.tracer.start_span("incident_dispatcher")
        
        try:
            # 2. Call service with circuit breaker controls
            payload = {"ticket_id": incident_details.get("id", "TKT-UNKNOWN")}
            res = self.client.call_service(payload, simulate_failure=simulate_api_failure)
            
            # End timing span successfully
            self.tracer.end_span(
                span.span_id, 
                status="OK", 
                tags={"ticket_id": incident_details.get("id"), "service": "Jira"}
            )
            return {"status": "SUCCESS", "message": res["data"], "state": self.client.state}
            
        except Exception as e:
            # End timing span with error status
            self.tracer.end_span(
                span.span_id, 
                status="FAILED", 
                tags={"error": str(e), "service": "Jira"}
            )
            return {"status": "FAILED", "error": str(e), "state": self.client.state}
