"""
Starter file for Exercise 5.3.
Runs offline benchmarks over gold dataset cases and outputs A/B comparison metrics.
"""
import json
import importlib
import sys
import os
from typing import List, Dict, Any

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

# Import from starters using importlib
exact_match = importlib.import_module("05_eval_basics.starter.exact_match")
grade_routing_decision = exact_match.grade_routing_decision
regex_match = importlib.import_module("05_eval_basics.starter.regex_match")
calculate_keyword_score = regex_match.calculate_keyword_score

llm_as_judge = importlib.import_module("05_eval_basics.starter.semantic_similarity")
evaluate_response_with_judge = llm_as_judge.evaluate_response_with_judge

def load_gold_dataset() -> List[Dict[str, Any]]:
    """Loads the version-controlled evaluation dataset from JSON."""
    # Find eval_dataset.json in the solution folder
    dataset_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../solution/eval_dataset.json"))
    with open(dataset_path, "r") as f:
        return json.load(f)

def run_ab_benchmark(
    agent_version: str, 
    generated_responses: Dict[str, Dict[str, str]]
) -> Dict[str, Any]:
    """Evaluates a batch of generated answers against gold cases and outputs performance aggregates."""
    # TODO: Implement benchmarking loop loaded from load_gold_dataset
    # Utilize exact_match, calculate_keyword_score, and evaluate_response_with_judge
    return {
        "version": agent_version,
        "routing_accuracy": 0.0,
        "average_keyword_score": 0.0,
        "average_judge_score": 0.0
    }
