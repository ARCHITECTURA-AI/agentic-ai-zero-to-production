# Worked Example: 30 / 60 / 90 Day Agentic AI Roadmap

This document serves as a filled-in exemplar of how to structure your 30/60/90-day learning and development roadmap after completing the **Agentic AI: From Zero to Production** cohort.

---

## 📅 The 90-Day Execution Plan

### 🟩 30 DAYS BLOCK: Consolidate
*Focus: Grounding your course learnings and establishing local operational security.*

* **Build**:
  * **Production-Harden Your Capstone**: Review your selected Capstone option (A, B, C, or D) and refine error handling.
  * **Add Missing Tests and Guardrails**: Ensure boundary conditions, token limiters, and prompt security layers are covered in your unit tests.
  * **Deploy Locally**: Package your agent system inside a secure Docker container and run it in a local sandbox environment.
  * **Write a Governance Readiness Checklist**: Draft an internal security review policy using [docs/governance_checklist.md](/docs/governance_checklist.md) as a starting point.
* **Learn**:
  * **ReAct Paper**: Read *ReAct: Synergizing Reasoning and Acting in Language Models* by Yao et al. (2022).
  * **Agentic AI Patterns**: Watch Andrew Ng's agentic design pattern lectures and video summaries.
  * **State Graph Concepts**: Deep dive into LangGraph's conceptual state reducer documentation.
  * **MCP Specifications**: Read the Model Context Protocol (MCP) specifications on the Anthropic developer portal.
* **Do at Work**:
  * **Audit a Workflow**: Select one repetitive manual process in your department and map it onto the chatbot-vs-copilot-vs-agent decision tree.
  * **Business Case Pitch**: Create a single-slide business proposal pitching an agentic solution for that process.
  * **Vendor Clearance**: Check with your IT security or compliance officers to find out which LLM vendors are approved for enterprise sandbox usage.

---

### 🟨 60 DAYS BLOCK: Expand
*Focus: Scaling out to your first work-relevant system using internal data and monitoring.*

* **Build**:
  * **Work-Relevant Agent**: Build an agent prototype processing a real dataset (with dummy PII or sanitized records).
  * **Observability from Day One**: Configure OpenTelemetry tracing spans using a dashboard (e.g., Arize Phoenix, Langfuse, or LangSmith).
  * **Connect to Internal Systems**: Implement a tool execution hook connecting to a read-only endpoint or mock internal database.
  * **Test-Driven Evals**: Write your evaluation suite and reference test cases *before* writing the agent's prompt routing code.
* **Learn**:
  * **Toolformer Paper**: Read *Toolformer: Language Models Can Teach Themselves to Use Tools* by Schick et al. (2023).
  * **A2A Protocol**: Review the Agent-to-Agent communication models published by major developer teams.
  * **Evaluation Best Practices**: Study the AWS Machine Learning blog posts regarding automated LLM agent evaluations.
  * **smolagents**: Explore lightweight tool-calling architectures (like Hugging Face's `smolagents`).
* **Do at Work**:
  * **Demonstrate the Agent**: Host a demo session showcasing your first working production agent to colleagues.
  * **Business Metric Translation**: Correlate agent latency and token cost reductions directly to business hours saved.
  * **Incident Playbook**: Draft and share a basic incident response playbook (for sandbox errors or circuit breaker trips) with your team.

---

### 🟥 90 DAYS BLOCK: Lead
*Focus: Driving enterprise adoption, multi-agent coordination, and team capability building.*

* **Build**:
  * **Level 3 Multi-Agent System**: Implement an orchestrator-specialist or hierarchical worker graph with loop limiters.
  * **Shared Evaluation Suite**: Deploy a centralized evaluation framework that your team can run against different model releases.
  * **Custom MCP Server**: Build a proprietary MCP server exposing one repeat internal enterprise database or tool.
  * **Agent A/B Testing**: Run a shadow deployment comparing two agent architectures (e.g., single ReAct loop vs. plan-and-execute) to collect statistical safety and latency results.
* **Learn**:
  * **Tree of Thoughts**: Read *Tree of Thoughts: Deliberate Problem Solving with Large Language Models* by Yao et al. (2023).
  * **MetaGPT Paper**: Study *MetaGPT: Meta Programming for Multi-Agent Collaborative Framework* by Hong et al. (2023).
  * **Anthropic Research Blog**: Follow weekly AI model scaling and safety research.
  * **Tech Industry Blogs**: Read Simon Willison's weblog weekly for the latest prompt injection, tooling, and LLM news.
* **Do at Work**:
  * **Internal Training**: Teach the Module 10 "Failure Modes & Vulnerabilities" session to your team or department.
  * **Post-Mortem Drills**: Run a mock incident drill where a circuit breaker trips or an input guardrail blocks a request.
  * **Champion Architecture**: Serve as the go-to technical advisor for agentic software design patterns and safety boundaries in your company.

---

> [!TIP]
> **"Teaching is the fastest way to find the gaps in your own understanding. If you can teach Session 9 (Enterprise Governance & Tool Safety Gateways), you have mastered the core production requirements of Agentic AI."**
