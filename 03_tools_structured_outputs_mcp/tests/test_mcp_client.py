import pytest
import importlib
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

mcp_demo_solution = importlib.import_module("03_tools_structured_outputs_mcp.solution.mcp_demo_solution")
run_mcp_client_demo = mcp_demo_solution.run_mcp_client_demo

def test_mcp_demo_execution():
    """Verify that the MCP demonstration configures, discovers, and executes tools."""
    res = run_mcp_client_demo()
    
    assert "client" in res
    assert "tools" in res
    assert "result" in res
    
    # Verify tool metadata profile list
    discovered_tools = res["tools"]
    assert len(discovered_tools) == 1
    assert discovered_tools[0].name == "get_user_email"
    assert "user_id" in discovered_tools[0].input_schema["properties"]
    
    # Verify execution output result
    assert res["result"] == "user_12345@corporate.com"
