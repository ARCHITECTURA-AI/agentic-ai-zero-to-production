import pytest
import importlib
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

llm_as_judge = importlib.import_module("05_eval_basics.starter.semantic_similarity")
evaluate_response_with_judge = llm_as_judge.evaluate_response_with_judge

ab_testing_framework = importlib.import_module("05_eval_basics.starter.ab_testing_framework")
run_ab_benchmark = ab_testing_framework.run_ab_benchmark

def test_judge_grading_logic():
    """Verify that the simulated LLM-as-a-Judge returns structured Pydantic feedback."""
    feedback = evaluate_response_with_judge(
        query="Refund me please",
        response="We will process a full refund for your ticket TKT-99123 within 30 days.",
        gold_reference="We will process a full refund for your ticket TKT-99123 within 30 days of purchase."
    )
    
    assert feedback.score == 5
    assert "explanation" in feedback.model_fields
    assert len(feedback.explanation) > 0

def test_ab_benchmark_pipeline():
    """Verify that A/B benchmark runners compile accurate comparative performance metrics."""
    # Build simulated generated outputs for Version A
    generated_v_a = {
        "CASE-101": {
            "category": "refund",
            "response": "We will process a full refund for your ticket TKT-99123 within 30 days."
        },
        "CASE-102": {
            "category": "billing",
            "response": "Double charge identified. We will reverse the secondary charge for ticket TKT-88421."
        },
        "CASE-103": {
            "category": "shipping",
            "response": "We have updated your delivery address to 100 Main St for shipment SHP-551."
        }
    }
    
    res = run_ab_benchmark("Version_A", generated_v_a)
    
    assert res["version"] == "Version_A"
    assert res["routing_accuracy"] == 1.0
    assert res["average_keyword_score"] > 0.8
    assert res["average_judge_score"] == 5.0
