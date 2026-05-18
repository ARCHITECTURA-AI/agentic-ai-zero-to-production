# Exercises: Typed Tools, Schemas & Model Context Protocol

In this module, you will transition a loose, unstructured toolset into a production-hardened, schema-enforced, and MCP-ready architecture.

---

## 🏋️ Exercise 3.1: Runtime Type Validation

**Location**: `starter/simple_tools.py` → `solution/typed_tools.py`
**Goal**: Enforce strict parameters and runtime constraints on a financial processing tool.

**Tasks**:
1. Open `starter/simple_tools.py` and inspect the `process_refund` function.
2. Define a Pydantic V2 model `RefundArgs` containing `ticket_id: str` and `amount: float`.
3. Add custom validation rules using Pydantic's `Field` (e.g. `amount` must be strictly positive).
4. Update the `process_refund` function to instantiate and validate incoming raw dictionary arguments before executing processing logic.

---

## 🏋️ Exercise 3.2: Hardening Unstructured Handoffs

**Location**: `starter/broken_unstructured_handoff.py` → `solution/validated_handoff.py`
**Goal**: Observe how messy, untyped dictionary state transitions corrupt downstream agents, and fix it using standard schemas.

**Tasks**:
1. Inspect `starter/broken_unstructured_handoff.py`. Note how the routing decision is passed as a raw python dictionary, leading to parameter naming mismatch (`dept` vs `department`) and silent type conversion failures.
2. Implement `validated_handoff.py` using the `RouterDecision` Pydantic model imported from `shared.models`.
3. Wrap the routing handoff transition function to validate the decision state and guarantee that only typed, sanitized records are transmitted to the downstream ticket router.

---

## 🏋️ Exercise 3.3: Mock MCP Client Connection

**Location**: `starter/mcp_demo.py` → `solution/mcp_demo_solution.py`
**Goal**: Dynamically query, discover, and execute backend database tools using the Model Context Protocol standards.

**Tasks**:
1. Inspect `shared/mcp_client.py` to understand how the mock server connection acts as a secure local tool router.
2. Complete `starter/mcp_demo.py` to establish a client link, register a local user information tool, query tool listings, and call the handler using JSON-RPC standard dictionary payloads.
