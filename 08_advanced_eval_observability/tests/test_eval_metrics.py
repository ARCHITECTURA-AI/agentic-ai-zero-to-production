import pytest
import importlib
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

eval_framework = importlib.import_module("08_advanced_eval_observability.starter.eval_pipeline")
calculate_faithfulness = eval_framework.calculate_faithfulness
calculate_relevance = eval_framework.calculate_relevance

def test_eval_high_faithfulness():
    """Verify that a response drawing solely from context scores highly."""
    context = "Refunds take three to five business days to clear."
    response = "Your refund will clear in three to five business days."
    res = calculate_faithfulness(response, context)
    
    assert res["score"] >= 0.8

def test_eval_low_faithfulness():
    """Verify that unsupported claims cause lower faithfulness scores."""
    context = "Refunds take three to five business days to clear."
    # Adding hallucinated words: 'bitcoin coupon promotion deposit bonus payment'
    response = "Your refund will clear in five days. Also deposit bitcoin for a promo bonus payment."
    res = calculate_faithfulness(response, context)
    
    assert res["score"] < 0.6

def test_eval_high_relevance():
    """Verify that a response directly matching query keywords scores highly."""
    query = "How do I cancel my subscription billing?"
    response = "To cancel your subscription billing, click cancel under account billing settings."
    res = calculate_relevance(response, query)
    
    assert res["score"] >= 0.8
