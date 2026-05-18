import pytest
import importlib
import sys
import os

# Securely inject workspace root to sys.path to guarantee packages are discoverable
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

production_agent_loop = importlib.import_module("02_agent_loop.solution.production_agent_loop")
HardenedAgentLoop = production_agent_loop.HardenedAgentLoop

def test_agent_loop_max_steps_containment():
    """Verify agent loop raises an error when steps exceed or meet max_steps limit boundaries."""
    # Test step ceiling boundary
    loop = HardenedAgentLoop(max_steps=3, max_cost_usd=10.00)
    
    # Executing 3 steps should trigger the StepLimitExceeded guardrail
    with pytest.raises(RuntimeError) as excinfo:
        loop.execute_react_cycle("Mock goal", mock_token_use_per_step=100)
        
    assert "Step guardrail triggered" in str(excinfo.value)

def test_agent_loop_budget_exhaustion():
    """Verify agent loop raises RuntimeError when the cumulative cost hits budget limitations."""
    # Setting budget to a very low threshold ($0.001) with heavy token cost step simulation
    loop = HardenedAgentLoop(max_steps=10, max_cost_usd=0.001)
    
    with pytest.raises(RuntimeError) as excinfo:
        loop.execute_react_cycle("Run heavy models", mock_token_use_per_step=50000)
        
    assert "Budget guardrail triggered" in str(excinfo.value)
