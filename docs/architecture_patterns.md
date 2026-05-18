# Architecture Patterns

A guide to the core agentic patterns implemented and examined throughout the course.

---

## 🧩 1. The ReAct Pattern (Reasoning & Acting)
Generates thoughts followed by actions in an iterative cycle:
```
Thought -> Action (Tool Call) -> Observation (Tool Output) -> Repeat
```
- **Strengths**: Intuitive, easy to implement, versatile.
- **Weaknesses**: Can easily drift; highly susceptible to infinite loop patterns.

---

## 🧩 2. Planning & Decomposition
Splits a complex task into discrete milestones prior to executing actions:
```
Objective -> Generate Plan -> Execute Step 1 -> Update Plan -> Execute Step 2 -> Final Output
```
- **Strengths**: Extremely effective for long-horizon or complex tasks.
- **Weaknesses**: Requires higher capability models; plan updates can consume substantial tokens.

---

## 🧩 3. Self-Reflection
Uses a dual-role prompt configuration where one model executes a task and another (or the same) model evaluates the outcome, feeding corrections back in:
```
Draft -> Review -> Identify Flaws -> Correct Draft -> Success Check
```
- **Strengths**: Signficantly elevates code generation and copywriting quality.
- **Weaknesses**: Doubles completion latency and token consumption metrics.

---

## 🧩 4. Human-in-the-Loop (HITL) Handoff
Enforces authorization checkpoints prior to execution of disruptive tool commands:
```
Agent -> Proposes Refund -> Halts Loop & Updates State -> Requests Human Approval -> Execute
```
- **Strengths**: Critical compliance layer for finance, health, and infrastructure agents.
- **Weaknesses**: Introduces manual bottlenecks in fully autonomous pipelines.
