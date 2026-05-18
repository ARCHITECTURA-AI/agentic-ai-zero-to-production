"""
Solution code for Capstone Option D: Secure Semantic Guardrail Gateway Proxy.
Integrates input injection shields, semantic groundedness checkers, and outbound PII/secret redactions.
"""
import importlib
import sys
import os
from typing import Dict, Any

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

# Import Guardrail systems using importlib
guardrails = importlib.import_module("10_failure_modes.solution.guardrails")
is_safe_input = guardrails.is_safe_input
sanitize_output = guardrails.sanitize_output

# Import Faithfulness Scorer using importlib
eval_framework = importlib.import_module("08_advanced_eval_observability.solution.eval_framework")
calculate_faithfulness = eval_framework.calculate_faithfulness

def run_gateway_proxy(query: str, context: str, response: str) -> Dict[str, Any]:
    """Intercepts and filters query injections, scores groundedness, and redacts outgoing PII/secrets."""
    # 1. Audit user prompt using Input Guardrail shields
    if not is_safe_input(query):
        return {
            "status": "BLOCKED",
            "output": "Blocked by Input Guardrail Shield: Security injection threat flagged."
        }

    # 2. Check semantic faithfulness of generated response against source context docs
    faith_eval = calculate_faithfulness(response, context)
    if faith_eval["score"] < 0.5:
        return {
            "status": "BLOCKED",
            "output": f"Blocked by Output Groundedness Guardrail: Hallucination detected (Score: {faith_eval['score']})."
        }

    # 3. Redact private tokens and PII before dispatching to client
    clean_output = sanitize_output(response)

    return {
        "status": "APPROVED",
        "output": clean_output,
        "faithfulness_score": faith_eval["score"]
    }
