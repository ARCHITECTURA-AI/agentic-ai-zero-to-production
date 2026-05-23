# Course Map: Agentic AI Zero to Production

This document outlines the session flow, learning outcomes, and files related to each curriculum module. Use this map to navigate the zero-to-production learning path.

---

## 🗺️ Curriculum Module Breakdown

### [Module 00: Pre-Assessment Calibration](/00_pre_assessment)
- **Goal**: Gauge student comfort levels around stateless LLM execution, vector RAG query behaviors, agent loops, schema boundaries, and basic safety boundaries.
- **Run Order**: Day 1, Hour 0.

### [Module 01: Paradigm Foundations](/01_foundations)
- **Goal**: Define Chatbots vs. Copilots vs. Autonomous Agents. Build a decision matrix to categorize when a task requires custom agentic logic or static logic.

### [Module 02: Building the Agent Loop from Scratch](/02_agent_loop)
- **Goal**: Code the state loop of an autonomous agent manually using pure Python.
- **Topics**: Prompt state compilation, infinite loop detection, and budget limiters.

### [Module 03: Typed Tools, Schemas & Model Context Protocol](/03_tools_structured_outputs_mcp)
- **Goal**: Enforce system outputs using Pydantic validation schemas.
- **Topics**: Safe structured parser handoffs, typed parameters, and MCP clients.

### [Module 04: Local RAG Pipeline & Context Management](/04_memory_rag_context)
- **Goal**: Implement standard RAG document retrievers with local vector stores.
- **Topics**: ChromaDB pipelines, chunking strategics, and context token budget pruning.

### [Module 05: Evaluation Basics & Unit Testing](/05_eval_basics)
- **Goal**: Implement deterministic and semantic evaluation metrics.
- **Topics**: CI verification of agent execution, assertion libraries, and mock evaluators.

### [Module 06: Core Agent Design Patterns](/06_design_patterns)
- **Goal**: Code classic single-agent architectures.
- **Topics**: ReAct, Planning, Self-Reflection, and Human-in-the-Loop approval locks.

### [Module 07: Multi-Agent Architectures & Graph Orchestration](/07_multi_agent)
- **Goal**: Build collaborative workflows.
- **Topics**: Hierarchical trees, routing logic, state transitions, LangGraph states, and CrewAI setups.

### [Module 08: Production Observability & Tracing](/08_advanced_eval_observability)
- **Goal**: Configure tracing diagnostics for production tracking.
- **Topics**: OpenTelemetry, Phoenix dashboard instrumentation, and prompt debugging.

### [Module 09: Enterprise Governance & Tool Safety Gateways](/09_production_security_enterprise)
- **Goal**: Harden agent runtimes against catastrophic failures.
- **Topics**: Dangerous tool isolation, secure Docker execution sandboxes, and RBAC policies.

### [Module 10: Failures Modes & Injection Vulnerabilities](/10_failure_modes)
- **Goal**: Secure agent prompt templates.
- **Topics**: Indirect prompt injections, silent routing failures, and parser containment defenses.

### [Module 11: Capstone Execution Projects](/11_capstone)
- **Goal**: Build an end-to-end sandboxed research assistant or corporate support escalation loop.

### [Module 12: Post-Course Roadmaps](/12_post_course)
- **Goal**: Formulate 30, 60, and 90-day deployment guidelines for corporate rollouts.
