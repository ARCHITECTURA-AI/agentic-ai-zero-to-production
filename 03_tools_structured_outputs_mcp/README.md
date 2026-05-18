# Module 03: Typed Tools, Schemas & Model Context Protocol

## What you will learn
- How to design reliable tools with strict type boundaries.
- How to enforce structured outputs from LLMs using Pydantic validation.
- How to implement secure schema transitions and parameter verification.
- The core architecture and implementation of the Model Context Protocol (MCP) clients.

## Files in this folder
- `concept_notes.md` — core architectural patterns for robust tool interfaces
- `tool_design_guide.md` — strict typing guidelines and Pydantic best practices
- `exercises.md` — structured tasks to complete
- `starter/` — template files with incomplete parts
  - `simple_tools.py` — basic tool definitions with type hints
  - `broken_unstructured_handoff.py` — demonstration of unstructured parameter corruption
  - `schemas.py` — starter Pydantic schemas
  - `mcp_demo.py` — client integration skeleton
- `solution/` — reference implementations
  - `typed_tools.py` — type-enforced and runtime-validated tool implementations
  - `validated_handoff.py` — structured transition and handoff state machine
  - `pydantic_models.py` — production schemas using Pydantic V2
  - `mcp_demo_solution.py` — full MCP mock server interaction suite
- `tests/` — validation suites for checking correct behavior
  - `test_tool_outputs.py` — verifies typing and validation constraints
  - `test_schema_validation.py` — checks structured extraction behavior
  - `test_mcp_client.py` — validates standard MCP server tool registry operations

## Run order
1. Read `concept_notes.md` and `tool_design_guide.md`
2. Review tasks in `exercises.md`
3. Fill in the skeletons under `starter/`
4. Run `pytest` to verify your implementation
5. Compare your changes with the files in `solution/`

## Success criteria
- Schemas strictly validate outputs and block untyped/unstructured dictionaries.
- Tool boundaries successfully validate input parameters at runtime.
- The MCP client discovers, registers, and dispatches tools successfully.

## Common failure modes
- Weak typing in JSON schemas (e.g., using generic Dict without properties) leading to parameter hallucinations.
- Swallowing validation exceptions (silent failures) rather than escalating parsing issues back to the agent or loop.
- Large, bloated schemas that exceed model context windows and cause output parsing issues.
