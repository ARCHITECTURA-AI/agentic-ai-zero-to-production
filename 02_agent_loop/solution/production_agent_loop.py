"""
Production-grade Agent Loop with full safety, costing, and step guardrails.
"""
# Import configuration details securely if needed
from shared.guardrails import verify_step_limit, verify_cost_limit
from shared.costing import calculate_step_cost
from shared.logging_utils import get_logger

logger = get_logger("agent")

class HardenedAgentLoop:
    def __init__(self, max_steps: int = 5, max_cost_usd: float = 1.00):
        self.max_steps = max_steps
        self.max_cost_usd = max_cost_usd
        self.accumulated_cost = 0.0
        self.steps_executed = 0
        
    def execute_react_cycle(self, objective: str, mock_token_use_per_step: int = 5000) -> dict:
        """Executes the loop safely while tracking costing and execution limits."""
        logger.info(f"Agent starting objective: {objective}", extra={"max_steps": self.max_steps})
        
        while self.steps_executed < self.max_steps:
            self.steps_executed += 1
            
            # 1. Enforce Step guardrails
            try:
                verify_step_limit(self.steps_executed, self.max_steps)
            except Exception as e:
                logger.error("Guardrail halt: step threshold exceeded", extra={"reason": "max_steps_exceeded", "steps": self.steps_executed})
                raise RuntimeError(f"Step guardrail triggered: {e}")
                
            # 2. Simulate API Call token usage and cost calculation
            step_cost = calculate_step_cost(
                model_name="gemini-1.5-pro",
                prompt_tokens=mock_token_use_per_step,
                completion_tokens=200
            )
            self.accumulated_cost += step_cost
            
            # 3. Enforce Budget guardrails
            try:
                verify_cost_limit(self.accumulated_cost, self.max_cost_usd)
            except Exception as e:
                logger.error("Guardrail halt: budget exhausted", extra={"reason": "budget_exhausted", "cost": self.accumulated_cost})
                raise RuntimeError(f"Budget guardrail triggered: {e}")
                
            logger.info(f"Step {self.steps_executed} completed.", extra={
                "step": self.steps_executed,
                "cost_usd": self.accumulated_cost
            })
            
        return {
            "status": "completed",
            "steps": self.steps_executed,
            "cost_usd": self.accumulated_cost
        }
