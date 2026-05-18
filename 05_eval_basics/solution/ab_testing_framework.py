"""
Solution file for Exercise 5.3.
Runs offline benchmarks over gold dataset cases and outputs A/B comparison metrics.
"""
import json
import importlib
import sys
import os
from typing import List, Dict, Any

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

deterministic_evals = importlib.import_module("05_eval_basics.solution.deterministic_evals")
grade_routing_decision = deterministic_evals.grade_routing_decision
calculate_keyword_score = deterministic_evals.calculate_keyword_score

llm_as_judge = importlib.import_module("05_eval_basics.solution.llm_as_judge")
evaluate_response_with_judge = llm_as_judge.evaluate_response_with_judge

def load_gold_dataset() -> List[Dict[str, Any]]:
    """Loads the version-controlled evaluation dataset from JSON."""
    dataset_path = os.path.join(os.path.dirname(__file__), "eval_dataset.json")
    with open(dataset_path, "r") as f:
        return json.load(f)

def run_ab_benchmark(
    agent_version: str, 
    generated_responses: Dict[str, Dict[str, str]]
) -> Dict[str, Any]:
    """Evaluates a batch of generated answers against gold cases and outputs performance aggregates."""
    dataset = load_gold_dataset()
    total_cases = len(dataset)
    
    if total_cases == 0:
        return {"version": agent_version, "routing_accuracy": 0.0, "average_keyword_score": 0.0, "average_judge_score": 0.0}
        
    routing_matches = 0
    total_kw_score = 0.0
    total_judge_score = 0.0
    
    for case in dataset:
        case_id = case["id"]
        response_payload = generated_responses.get(case_id, {})
        
        pred_category = response_payload.get("category", "")
        pred_response = response_payload.get("response", "")
        
        # 1. Routing classification exact match evaluation
        if grade_routing_decision(pred_category, case["expected_category"]):
            routing_matches += 1
            
        # 2. Keyword overlap evaluation
        kw_score = calculate_keyword_score(pred_response, case["required_keywords"])
        total_kw_score += kw_score
        
        # 3. Semantic LLM Judge evaluation
        judge_res = evaluate_response_with_judge(
            query=case["query"],
            response=pred_response,
            gold_reference=case["gold_reference"]
        )
        total_judge_score += judge_res.score
        
    return {
        "version": agent_version,
        "routing_accuracy": round(routing_matches / total_cases, 4),
        "average_keyword_score": round(total_kw_score / total_cases, 4),
        "average_judge_score": round(total_judge_score / total_cases, 4)
    }
