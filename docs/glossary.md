# Glossary of Agentic AI Terms

A quick-reference guide to terminology utilized throughout the Zero to Production curriculum.

---

## 🅰️ Terms

### Agent (Autonomous Agent)
An AI system that receives an objective, evaluates state, plans, calls tools, observes environments, and iteratively executes a state-loop to accomplish the goal without constant human intervention.

### Chatbot vs. Copilot vs. Agent
- **Chatbot**: Stateless conversational interface (responds directly to requests).
- **Copilot**: Interactive workspace assistant (suggests code, helps complete fields, but keeps human in control of execution).
- **Agent**: Goal-directed, autonomous state loop capable of selecting and running tools independently.

### ChromaDB
An open-source, highly lightweight embedding database optimized for local context search and vector similarity retrieval.

### Cost Breaker
A safety guardrail that counts cumulative LLM API token spends during a task execution and terminates execution immediately if the budget threshold is breached.

### Human-in-the-Loop (HITL)
A governance pattern where an agent pauses its loop and escalates to a human operator for permission or feedback before executing high-risk tools.

### Model Context Protocol (MCP)
An open standard that defines a uniform protocol for agents to connect with and discover contextual data and tools provided by external secure servers.

### Prompt Injection
A security vulnerability where untrusted user input contains instructions that override or bypass the core developer-configured system guidelines.

### ReAct (Reasoning and Acting)
A single-agent architecture pattern that prompts the model to generate alternating segments of thought (Reasoning) and tool invocations (Acting), observing tool outputs to decide subsequent actions.

### State-Loop
The core cycle of an agent: Compiling context -> Querying model -> Parsing action -> Executing tool -> Updating state.
