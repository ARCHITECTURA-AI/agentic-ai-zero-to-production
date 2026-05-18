"""
Solution file for Exercise 5.2.
Implements the LLM-as-a-Judge semantic rubric feedback and grading evaluator.
"""
from pydantic import BaseModel, Field

class JudgeFeedback(BaseModel):
    """Pydantic model representing structured feedback from our LLM Judge."""
    explanation: str = Field(..., description="Chain-of-thought justification for the assigned grade.")
    score: int = Field(..., description="Semantic score from 1 (unhelpful/inaccurate) to 5 (perfect execution).")

def evaluate_response_with_judge(query: str, response: str, gold_reference: str) -> JudgeFeedback:
    """Invokes a simulated LLM-as-a-Judge evaluator to score agent responses against gold standards."""
    # Normalize inputs
    resp_clean = response.strip().lower()
    gold_clean = gold_reference.strip().lower()
    
    # Calculate simple word token intersections to make the offline simulated judge smart
    resp_words = set(resp_clean.split())
    gold_words = set(gold_clean.split())
    intersection = resp_words.intersection(gold_words)
    
    # Smart classification rules mimicking actual LLM evaluations
    if "unable to process" in resp_clean or "sorry" in resp_clean:
        score = 2
        explanation = (
            "The agent returned an apologetic refusal or error bypass. "
            "It failed to execute the customer instruction."
        )
    elif len(intersection) >= 3 or resp_clean == gold_clean:
        score = 5
        explanation = (
            "Outstanding resolution. The agent addressed the core query cleanly "
            "and matched all verification keywords present in the gold key."
        )
    else:
        score = 3
        explanation = (
            "The response is grammatically acceptable but lacks complete semantic alignment "
            "or misses critical action items outlined in the reference model."
        )
        
    return JudgeFeedback(explanation=explanation, score=score)
