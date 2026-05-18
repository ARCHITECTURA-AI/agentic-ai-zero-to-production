# Concept Notes: Typed Tools, Schemas & Model Context Protocol

## Why Structured Boundaries Matter

In early agent designs, tool execution was handled via unstructured strings or raw JSON dictionaries:
- The model outputs a thought and a command string (e.g. `EXECUTE: calculate_refund(ticket_id="123", amount="45.00")`).
- The parser extracts this string using regular expressions or `json.loads`.
- The system executes the action and returns the output to the agent.

This approach works for simple demos but breaks in enterprise production because of **hallucinations, parsing errors, and loose type safety**:
1. **Type Hallucinations**: An LLM might pass a string like `"forty-five dollars"` instead of a float `45.00` to a financial API.
2. **Missing Parameters**: The LLM might call a database query tool and forget a required filtering key, leading to database errors or unsafe full table scans.
3. **Implicit Schemas**: When tool definitions are passed to the model as unstructured text prompts, the model has to infer the parameter names, resulting in high variance and fragile outputs.

### The Pydantic Solution

Pydantic bridges the gap between natural language instruction and deterministic system execution:
- You define the tool arguments as a structured Pydantic class (`BaseModel`).
- Pydantic validates types at runtime (e.g., converting `"45.00"` to `45.00` if appropriate, or raising `ValidationError` if given `"forty-five"`).
- We can auto-generate standardized JSON schemas directly from the Pydantic classes to feed into modern LLM Tool Calling APIs (like OpenAI's tool definitions or Gemini's function declarations).

---

## 🛠️ The Model Context Protocol (MCP)

As the ecosystem of AI agents has expanded, building custom integrations for every tool (Jira, Slack, PostgreSQL, ServiceNow) became a bottleneck. The **Model Context Protocol (MCP)**, introduced by Anthropic, acts as a standard protocol for connecting AI models to context sources and tools.

### MCP Core Architecture

The protocol defines three core actors:
1. **Host**: The orchestrator (often an agent system or chat client like Claude Desktop) that controls the model and requests data.
2. **Client**: A sub-component inside the Host that establishes standard transport connections (like stdio or SSE) to MCP servers.
3. **Server**: A standalone service that exposes resources, tools, and prompts.

```
┌──────────────────────────────────────────────┐
│                  MCP Host                    │
│   (State Loop, LangGraph, CrewAI, Python)    │
│        ┌────────────────────────────┐        │
│        │         MCP Client         │        │
└────────┼──────────────┬─────────────┼────────┘
                        │ (JSON-RPC 2.0 over Stdio/SSE)
         ┌──────────────▼─────────────┐
         │         MCP Server         │
         │  (Tools, Prompts, Files)   │
         └────────────────────────────┘
```

### The Three MCP Concepts

1. **Resources**: Read-only data sources (like files, database tables, or logs) exposed to the model.
2. **Tools**: Executable functions that can perform operations (e.g., running shell commands, editing a file, sending an API call) after receiving client approval.
3. **Prompts**: Pre-structured prompt templates that models can call to perform common operations.
