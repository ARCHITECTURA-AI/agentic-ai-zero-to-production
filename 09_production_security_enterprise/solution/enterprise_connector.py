"""
Solution file for Exercise 9.2.
Resilient API connector wrapper integrating an automated Circuit Breaker state machine.
"""
from typing import Dict, Any
import time

class CircuitBreakerError(Exception):
    """Raised when requests are rejected because the circuit is open."""
    pass

class EnterpriseClient:
    """Enterprise client managing connection health using the Circuit Breaker pattern."""
    def __init__(self, failure_threshold: int = 3, cooloff_period_sec: float = 0.3):
        self.state = "CLOSED"  # CLOSED, OPEN, HALF-OPEN
        self.consecutive_failures = 0
        self.failure_threshold = failure_threshold
        self.cooloff_period = cooloff_period_sec
        self.last_state_change = time.time()

    def _check_cooloff(self) -> None:
        """Flips state from OPEN to HALF-OPEN if the cooloff period has expired."""
        if self.state == "OPEN":
            if time.time() - self.last_state_change > self.cooloff_period:
                self.state = "HALF-OPEN"
                self.last_state_change = time.time()

    def call_service(self, request_payload: Dict[str, Any], simulate_failure: bool = False) -> Dict[str, Any]:
        """Calls live system endpoints, checking circuit safety triggers."""
        self._check_cooloff()

        if self.state == "OPEN":
            raise CircuitBreakerError("Circuit Breaker is OPEN. Request blocked to prevent systemic load.")

        if simulate_failure:
            self.consecutive_failures += 1
            if self.consecutive_failures >= self.failure_threshold:
                self.state = "OPEN"
                self.last_state_change = time.time()
            raise ConnectionError("Downstream server connection timeout.")

        # On success, reset counts and close circuit
        self.consecutive_failures = 0
        self.state = "CLOSED"
        self.last_state_change = time.time()

        return {
            "status": "SUCCESS",
            "data": f"Enterprise Sync Complete for ticket {request_payload.get('ticket_id', 'TKT-UNKNOWN')}"
        }
