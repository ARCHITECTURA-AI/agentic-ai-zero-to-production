# Agent Patterns: Workflow Visualization Diagrams

These flowcharts outline the exact logical trajectories followed by single-agent patterns in this module.

---

## 1. ReAct Reasoning Cycle

```mermaid
flowchart TD
    A["User Submits Issue"] --> B["Initialize Loop (Iter = 1)"]
    B --> C["Formulate Thought (Reasoning)"]
    C --> D{"Decide Action?"}
    D -- "Tool Call" --> E["Execute Tool & Capture Observation"]
    E --> F["Increment Iteration Counter"]
    F --> G{"Iter > max_iterations?"}
    G -- "Yes" --> H["Safely Terminate with Warning"]
    G -- "No" --> C
    D -- "Final Answer" --> I["Deliver Resolution to User"]
```

---

## 2. Generator-Reflector Critique Cycle

```mermaid
flowchart TD
    A["User Request"] --> B["Generator: Create Initial Draft"]
    B --> C["Reflector: Evaluate Tone & Compliance"]
    C --> D{"Meets Quality Standard (APPROVED)?"}
    D -- "No" --> E["Incorporate Critique Feedback"]
    E --> B
    D -- "Yes" --> F["Return Polished Refined Output"]
```

---

## 3. Human-in-the-Loop (HITL) Security Gate

```mermaid
flowchart TD
    A["Agent Requests Refund Action"] --> B{"Is Amount > $100?"}
    B -- "No" --> C["Execute Refund Automatically"]
    B -- "Yes" --> D["Pause Loop & Serialize Current State"]
    D --> E["Prompt Admin for Manual Authorization"]
    E --> F{"Admin Decision?"}
    F -- "APPROVED" --> G["Inject APPROVED Status into Agent State & Finalize"]
    F -- "REJECTED" --> H["Inject REJECTED Status & Cancel Transaction"]
```
