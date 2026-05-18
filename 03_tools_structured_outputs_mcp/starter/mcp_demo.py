"""
Starter file for Exercise 3.3.
Skeleton showing how to orchestrate client connections and tool executions using MCP.
"""
from shared.mcp_client import MockMCPClient, MCPTool

def get_user_email_handler(user_id: str) -> str:
    """Mock handler callback for retrieving emails."""
    return f"user_{user_id}@corporate.com"

def run_mcp_client_demo() -> dict:
    """Orchestrates an MCP server setup, registers a tool, and executes it."""
    # TODO:
    # 1. Initialize the MockMCPClient with a server name "user-service"
    # 2. Define the input schema for `get_user_email` containing a required `user_id` parameter (type string).
    # 3. Create an MCPTool object.
    # 4. Register the tool with the handler: `get_user_email_handler`
    # 5. List the registered tools to verify.
    # 6. Execute the tool with user_id="12345" and return the results.
    
    return {}
