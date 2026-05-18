"""
Stage 2 Starter: Partial Agent Loop.
Implements a step limit but lacks token budgeting or financial guardrails.
"""

class PartialAgentLoop:
    def __init__(self, max_steps: int = 5):
        self.max_steps = max_steps
        
    def run(self, objective: str) -> dict:
        print(f"Goal: {objective}")
        step = 0
        
        while step < self.max_steps:
            step += 1
            print(f"Step {step} processing...")
            # DANGEROUS: If we consume 100,000 tokens per call, we can blow through
            # our entire enterprise credit tier in seconds without costing checks!
            
        return {"status": "max_steps_reached", "steps": step}
