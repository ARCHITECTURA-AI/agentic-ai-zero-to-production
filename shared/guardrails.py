import os
import sys
from typing import Optional, Callable

class StepLimitExceeded(Exception):
    """Exception raised when an agent loop exceeds the maximum step budget."""
    pass

class CostLimitExceeded(Exception):
    """Exception raised when execution costs exceed the corporate safety ceiling."""
    pass

def verify_step_limit(current_step: int, max_steps: int = 10) -> None:
    """Raise an error if the agent is stuck in an infinite cycle."""
    if current_step >= max_steps:
        raise StepLimitExceeded(f"Agent loop halted: exceeded step threshold of {max_steps} steps.")

def verify_cost_limit(accumulated_cost_usd: float, max_cost_usd: float = 2.00) -> None:
    """Halt executing loops to prevent credit drainage."""
    if accumulated_cost_usd > max_cost_usd:
        raise CostLimitExceeded(f"Agent loop halted: spent ${accumulated_cost_usd:.4f} which exceeds corporate limit of ${max_cost_usd:.4f}.")

def human_approval_gate(
    action_description: str,
    mock_input: Optional[bool] = None,
    interactive: bool = False
) -> bool:
    """Enforce an approval checkpoint before high-risk actions.
    
    In testing/CI, returns the mock_input value if provided.
    """
    print(f"\n🚨 [HUMAN APPROVAL NEEDED] Action: {action_description}")
    
    if mock_input is not None:
        print(f"  Mock input provided: {'APPROVED' if mock_input else 'REJECTED'}")
        return mock_input
        
    if interactive:
        try:
            choice = input("Approve action? [y/N]: ").strip().lower()
            return choice in ["y", "yes"]
        except (IOError, EOFError):
            print("  Interactive console not available. Action automatically REJECTED for safety.")
            return False
            
    # Default to safety
    print("  Escalating... Action automatically REJECTED (Non-interactive mode).")
    return False
