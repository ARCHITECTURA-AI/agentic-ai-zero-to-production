"""
Solution file for Exercise 3.3.
Full execution of tool registration, schemas, and calling using the MCP protocol.
"""
from shared.mcp_client import MockMCPClient, MCPTool

def get_user_email_handler(user_id: str) -> str:
    """Mock handler callback for retrieving emails."""
    return f"user_{user_id}@corporate.com"

def run_mcp_client_demo() -> dict:
    """Orchestrates an MCP server setup, registers a tool, and executes it."""
    # 1. Initialize MockMCPClient
    client = MockMCPClient(server_name="user-service")
    
    # 2. Define input schema for the tool
    schema = {
        "type": "object",
        "properties": {
            "user_id": {
                "type": "string",
                "description": "Unique alphanumeric customer user ID"
            }
        },
        "required": ["user_id"]
    }
    
    # 3. Create MCPTool profile
    tool = MCPTool(
        name="get_user_email",
        description="Retrieves the corporate email address for a given user ID.",
        input_schema=schema
    )
    
    # 4. Register tool and callback
    client.register_tool(tool, get_user_email_handler)
    
    # 5. List registered tools
    tools = client.list_tools()
    
    # 6. Execute the tool via MCP standard client protocol
    result = client.execute_tool("get_user_email", {"user_id": "12345"})
    
    return {
        "client": client,
        "tools": tools,
        "result": result
    }
