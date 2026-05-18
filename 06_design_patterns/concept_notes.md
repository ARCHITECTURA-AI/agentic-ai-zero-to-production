# Concept Notes: Single-Agent Design Patterns

To make agents autonomous yet reliable, we structure their execution loops using design patterns:

---

## 1. The ReAct (Reasoning + Action) Pattern

Introduced by Yao et al. (2022), **ReAct** combines reasoning (Thoughts) with task-specific actions (Tool Calls and Observations) in a structured cycle:

```
┌────────────────────────────────────────────────────────┐
│                        User Query                      │
└───────────────────────────┬────────────────────────────┘
                            ▼
                   ┌─────────────────┐
                   │     Thought     │ ◄────────────────┐
                   └────────┬────────┘                  │
                            ▼                           │
                   ┌─────────────────┐                  │
                   │     Action      │ (Call Tool)      │
                   └────────┬────────┘                  │
                            ▼                           │
                   ┌─────────────────┐                  │
                   │   Observation   │ (Tool Return) ───┘
                   └────────┬────────┘
                            ▼
                   ┌─────────────────┐
                   │   Final Answer  │
                   └─────────────────┘
```

**Key benefits**: Improves model tracking accuracy and allows developers to inspect intermediate thoughts, resolving "black-box" agent concerns.

---

## 2. Reflection & Self-Correction

A major failure mode of direct prompting is that the model's first draft of a complex answer often contains subtle logical mistakes, formatting bugs, or poor wording. 
To fix this, we use a **Generator-Reflector** pattern:
1. **Generate**: The Generator agent creates a draft solution (e.g. drafting a response email).
2. **Reflect**: A separate Critique prompt (often simulated or running a specialized persona) reviews the draft against standard rubrics (safety, length, tone).
3. **Refine**: The Generator agent takes the critique and updates the draft.

```
 [User Request] ──► [Generator Agent] ───► [Draft Output] 
                          ▲                    │
                          │                    ▼
                    (Refine Draft)      [Reflector Agent] (Critique)
                          │                    │
                          └────────────────────┘
```

---

## 3. Human-In-The-Loop (HITL) Hooks

For security and governance, agents must not have unchecked access to mutate systems or initiate financial transactions. 
We establish **Human-In-The-Loop (HITL)** checkpoints:
- **Rule Boundary**: High-risk actions (e.g., spending money, modifying database users, deleting files) trigger a pause.
- **State Serialization**: The execution loop halts, serializes its current execution trace, and prompts a human reviewer.
- **Resume Injection**: The human approves or rejects the action, injecting their decision directly back into the execution loop's environment state to let the agent resume.
