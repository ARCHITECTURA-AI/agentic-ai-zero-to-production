# Concept Notes: Multi-Agent Collaboration & Orchestration

When a single agent is tasked with handling multiple disparate tools, files, and rules, it suffers from several failure modes:
1. **Context Bloat**: Feeding all tools, system rules, and schemas into one prompt consumes significant tokens, raising cost and latency.
2. **Action Confusion**: High-entropy prompts cause the model to invoke incorrect tools or misinterpret rules.
3. **Fragile State Management**: A single agent loop is difficult to debug or secure against edge-case failures.

To scale, we partition the agent's responsibilities into a team of specialized agents: **Multi-Agent Systems (MAS)**.

---

## 1. The Supervisor (Orchestrator) Pattern

The most popular corporate MAS architecture is the **Supervisor/Orchestrator** model. 
A central orchestrator acts as the "manager":
1. The supervisor receives the user request.
2. It evaluates the intent and selects the best specialist agent for the task (e.g. routing billing questions to the Billing Specialist).
3. The selected specialist executes its sub-task and returns its findings.
4. The supervisor compiles the final response or routes the task to another specialist if needed.

```
                  ┌──────────────────────┐
                  │    User Ticket       │
                  └──────────┬───────────┘
                             ▼
                  ┌──────────────────────┐
                  │ Supervisor/Router    │
                  └──────┬────────┬──────┘
                         │        │
         ┌───────────────┘        └───────────────┐
         ▼                                        ▼
┌─────────────────┐                      ┌─────────────────┐
│  Billing Agent  │                      │  Refund Agent   │
└─────────────────┘                      └─────────────────┘
```

---

## 2. Orchestration vs. Choreography

MAS frameworks generally follow one of two orchestration patterns:
- **Orchestration (LangGraph / Autogen)**: Driven by strict, directed state machines. The path of execution is explicitly designed (e.g. Agent A always passes to Agent B, or routes through a Supervisor). This is ideal for regulated enterprise environments.
- **Choreography (CrewAI)**: Driven by free-form, goal-based interactions. You define agent roles and backstories, and the agents dynamically negotiate who performs each task. This is highly flexible but less deterministic.

---

## 3. The Inter-Agent Handshake Protocol

To prevent information loss when tasks are handed off between agents, we define a structured **Handshake Protocol**:
- **Case ID**: Traceable session tracking number.
- **Payload State**: Standardized dictionary containing critical variables (e.g. validated refund amounts, user email, billing address).
- **Handoff Notes**: Short context summary written by the departing specialist to help the receiving specialist resume work seamlessly.
- **Hop Count**: Counter indicating how many times a case has been transferred between agents. If it exceeds a strict limit (e.g., 5 hops), the system triggers an automatic safety halt to prevent infinite routing loops.
