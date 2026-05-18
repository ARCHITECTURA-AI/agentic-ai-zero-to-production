# Tool Design Guide: Building Production-Grade Agentic Tools

To build agentic tools that work consistently in corporate production environments, follow these four foundational rules:

---

## 1. Explicit Parameter Typing & Runtime Validation

Never allow tools to accept arbitrary `*args` or `**kwargs` or generic `dict` collections unless absolutely necessary. Be explicit:
- Use standard Python type annotations (`int`, `str`, `float`, `bool`, `List`, `Dict`).
- Use Pydantic schemas to validate parameters at the gate of the tool function.
- Validate ranges (e.g. `confidence: float = Field(..., ge=0.0, le=1.0)`).

```python
# Bad: Weak type safety
def process_refund(data: dict):
    ticket_id = data.get("ticket_id")
    amount = float(data.get("amount")) # Risks TypeError/ValueError at runtime
    ...

# Good: Strict schema validation
from pydantic import BaseModel, Field

class RefundRequest(BaseModel):
    ticket_id: str = Field(..., description="Unique alphanumeric ticket identifier")
    amount: float = Field(..., gt=0.0, description="Refund value in USD. Must be greater than 0")

def process_refund(req: RefundRequest):
    # Parameter request is guaranteed to be clean here
    ...
```

---

## 2. Leverage High-Fidelity Docstrings

LLM model function calling relies on compiling code definitions into prompt schemas. Most modern LLM APIs extract the description of the tool and the descriptions of individual parameters from the function docstrings.
- Always write detailed, clear docstrings for tool functions.
- Keep parameter descriptions actionable (state limits, formats, examples).

---

## 3. Sandboxing & Error Containment

If a tool fails, it must throw an explicit, clear error string that the agent can read and reason about.
- Catch raw database or network errors at the tool level and wrap them in user-friendly messages.
- Avoid catching and swallowing exceptions silently. If a tool fails, tell the agent *why* it failed so it can adjust its strategy.

---

## 4. State Handoffs Must Be Atomic

When transitioning a task from one stage to another:
- Ensure the state container passes through a strict Pydantic model.
- Prevent partial state corruption where some parameters are mutated but validation fails on others.
- Ensure state schemas are version-controlled.
