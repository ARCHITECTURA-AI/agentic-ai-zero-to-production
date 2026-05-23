import pytest
import importlib
import sys
import os

# Securely inject workspace root to sys.path to guarantee packages are discoverable
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

classify_systems_solution = importlib.import_module("01_foundations.starter.classify_systems")
solution_classify = classify_systems_solution.classify_task

def test_classification_matrix():
    """Assert that the classifier accurately labels systems based on taxonomy properties."""
    # Chatbot cases
    assert solution_classify(requires_tools=False, interactive_human_in_loop=True, steps_horizon_greater_than_one=False) == "chatbot"
    assert solution_classify(requires_tools=False, interactive_human_in_loop=False, steps_horizon_greater_than_one=False) == "chatbot"
    
    # Copilot cases
    assert solution_classify(requires_tools=True, interactive_human_in_loop=True, steps_horizon_greater_than_one=False) == "copilot"
    
    # Agent cases
    assert solution_classify(requires_tools=True, interactive_human_in_loop=False, steps_horizon_greater_than_one=True) == "agent"
    assert solution_classify(requires_tools=True, interactive_human_in_loop=True, steps_horizon_greater_than_one=True) == "agent"
