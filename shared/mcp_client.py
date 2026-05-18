from typing import Dict, Any, List, Optional
from pydantic import BaseModel, Field

class MCPTool(BaseModel):
    """Data structure representing an MCP-compliant tool profile."""
    name: str
    description: str
    input_schema: Dict[str, Any]

class MockMCPClient:
    """Simulates a Model Context Protocol (MCP) client connection to a server.
    
    Allows dynamic registration, listing, and validation of tool schemas.
    """
    def __init__(self, server_name: str = "mock-server"):
        self.server_name = server_name
        self.registry: Dict[str, MCPTool] = {}
        self.executors: Dict[str, Any] = {}

    def register_tool(self, tool: MCPTool, handler_callable: Any) -> None:
        """Register an available tool and its callback executor."""
        self.registry[tool.name] = tool
        self.executors[tool.name] = handler_callable

    def list_tools(self) -> List[MCPTool]:
        """Return all discovered tool profiles from the server."""
        return list(self.registry.values())

    def execute_tool(self, name: str, arguments: Dict[str, Any]) -> str:
        """Validate tool schema arguments and execute the associated callback handler."""
        if name not in self.registry:
            raise KeyError(f"Tool '{name}' is not registered on MCP server '{self.server_name}'.")
            
        tool = self.registry[name]
        # Validate that required keys in input_schema are present in arguments
        required_params = tool.input_schema.get("required", [])
        for req in required_params:
            if req not in arguments:
                raise ValueError(f"Missing required argument '{req}' for tool '{name}'.")
                
        # Run handler
        handler = self.executors[name]
        try:
            result = handler(**arguments)
            return str(result)
        except Exception as e:
            return f"Error executing tool '{name}': {str(e)}"
