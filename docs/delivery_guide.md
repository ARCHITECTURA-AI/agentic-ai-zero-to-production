# Delivery Guide

This document is for instructors and facilitators delivering the **Agentic AI: Zero to Production** course. It provides guidelines for timing, presentation strategies, and live-coding demonstrations.

---

## ⏱️ Module Schedule & Timing

This is a **10-hour intensive program** optimized for corporate engineering teams.

| Module | Topic | Duration | Style | Key Deliverable |
| :--- | :--- | :--- | :--- | :--- |
| **00** | Pre-Assessment & Calibration | 30 mins | Interactive | Baseline diagnostics |
| **01** | Foundations & Classifications | 45 mins | Lecture/Discussion | Decision trees |
| **02** | Core Agent Loops from Scratch | 60 mins | Live-Coding | Manual loop + Safety limits |
| **03** | Typed Tools & Schema Handoffs | 60 mins | Exercise | Safe schema validation & MCP |
| **04** | Local RAG & Vector Memory | 60 mins | Lecture + Sandbox | Chroma index + Budget manager |
| **05** | Evaluation Driven Design | 60 mins | Interactive | Pre-launch test assertion suites |
| **06** | Single-Agent Patterns | 75 mins | Live-Coding | ReAct, Planning, Reflection |
| **07** | Multi-Agent Systems & Graphs | 90 mins | Exercise | LangGraph / CrewAI orchestration |
| **08** | Production Observability & Phoenix | 45 mins | Demo | Tracing spans & OTel pipelines |
| **09** | Security & Sandboxed Execution | 45 mins | Lecture/Sandbox | Execution environments & RBAC |
| **10** | Vulnerability Failures & Injection | 45 mins | Exercise | Injection exploit & defenses |
| **11** | Capstone Execution Project | 120 mins| Workshop | Working Agentic sandbox |
| **12** | Post-Course Production Roadmap | 30 mins | Wrap-Up | 30-60-90 Day execution plan |

---

## 🎓 Instructor Strategies & Pitfalls

### 1. The Cost Trap (Module 02)
- **Problem**: Student loops get stuck in infinite execution cycles, consuming massive token budgets.
- **Defense**: Enforce step bounds (`max_steps=10`) and cost limiters before allowing students to run free-form prompts.

### 2. Vibes-Based Engineering (Module 05)
- **Problem**: Students spend hours tweaking prompt strings rather than building metric check systems.
- **Defense**: Do not write code until they have defined standard semantic or deterministic tests.

### 3. Proxy/Firewall Failures (Module 03 & 04)
- **Problem**: Corporate firewalls block third-party endpoints or database clouds.
- **Defense**: Use local in-memory Chroma vectors (`Module 04`) and standard local mocks for multi-agent loops if internet reachability fluctuates.
