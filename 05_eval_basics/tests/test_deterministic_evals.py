import pytest
import importlib
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

deterministic_evals = importlib.import_module("05_eval_basics.solution.deterministic_evals")
grade_routing_decision = deterministic_evals.grade_routing_decision
verify_ticket_id_present = deterministic_evals.verify_ticket_id_present
calculate_keyword_score = deterministic_evals.calculate_keyword_score

def test_grade_routing_decision():
    """Verify that routing checks normalize case and trim whitespace correctly."""
    assert grade_routing_decision("  REFUND  ", "refund") is True
    assert grade_routing_decision("billing", "BILLING") is True
    assert grade_routing_decision("shipping", "billing") is False

def test_verify_ticket_id_present():
    """Verify regex scans successfully detect ticket numbers of format TKT-#####."""
    assert verify_ticket_id_present("I am reporting ticket TKT-10243 today.") is True
    assert verify_ticket_id_present("Ref numbers 12345 and ticket 99312 are missing.") is False

def test_calculate_keyword_score():
    """Verify that the ratio of present keywords is accurately evaluated."""
    text = "We processed your corporate refund today."
    keywords = ["refund", "corporate", "delivery"]
    # 2 out of 3 matches -> 0.6667
    score = calculate_keyword_score(text, keywords)
    assert round(score, 2) == 0.67
