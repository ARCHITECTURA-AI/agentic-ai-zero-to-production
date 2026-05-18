"""
Starter file for Exercise 5.2.
Construct LLM-as-a-Judge schemas and call evaluators.
"""
from pydantic import BaseModel, Field

class JudgeFeedback(BaseModel):
    """Pydantic model representing structured feedback from our LLM Judge."""
    # TODO: Add fields
    # 1. explanation: str (Chain of thought reasoning)
    # 2. score: int (Helpfulness rating from 1 to 5)
    pass

def evaluate_response_with_judge(query: str, response: str, gold_reference: str) -> JudgeFeedback:
    """Invokes our LLM-as-a-Judge model to compare the actual response against a gold reference."""
    # TODO: Formulate prompt injecting query, response, and gold_reference.
    # Return a simulated or real JudgeFeedback object.
    
    return JudgeFeedback(explanation="Placeholder explanation", score=5)
