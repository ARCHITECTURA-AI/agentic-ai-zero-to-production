"""
Solution file for Exercise 10.2.
Automated system degradation runbook executing actions with fast backup model failover and incident tracking.
"""
from typing import Dict, Any, List, Callable
import time

class IncidentLedger:
    """WORM-like (Write Once, Read Many) in-memory repository to store security and service incidents."""
    def __init__(self):
        self.incidents: List[Dict[str, Any]] = []

    def record_incident(self, error_msg: str, recovery_action: str) -> None:
        self.incidents.append({
            "timestamp": time.time(),
            "error": error_msg,
            "action": recovery_action
        })

global_ledger = IncidentLedger()

def execute_with_fallback(primary_fn: Callable[[], str], fallback_fn: Callable[[], str]) -> Dict[str, Any]:
    """Tries primary pipeline, and on network errors automatically triggers backup failovers."""
    try:
        output = primary_fn()
        return {
            "status": "SUCCESS",
            "output": output,
            "degraded": False
        }
    except (ConnectionError, TimeoutError, OSError) as err:
        # Record outage in the global incident ledger
        error_msg = f"Outage triggered: {str(err)}"
        recovery_action = "Dynamic model degradation completed. Redirected execution to backup model."
        global_ledger.record_incident(error_msg, recovery_action)
        
        # Execute secondary fallback function
        fallback_output = fallback_fn()
        return {
            "status": "DEGRADED",
            "output": fallback_output,
            "degraded": True,
            "error_logged": str(err)
        }
