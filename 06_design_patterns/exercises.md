# Exercises: Single-Agent Design Patterns

In this module, you will construct autonomous reasoning loops, critique engines, and manual authorization gates.

---

## 🏋️ Exercise 6.1: The ReAct Execution Engine

**Location**: `starter/react_agent.py` → `solution/react_framework.py`
**Goal**: Build a standard Thought-Action-Observation loop that manages system steps and terminates cleanly.

**Tasks**:
1. Implement a parser that extracts `Thought:`, `Action:`, and `Observation:` tags.
2. Formulate the loop that calls tools sequentially and appends observations to prompt histories.
3. Enforce a strict `max_iterations` counter (e.g. 5 steps) to prevent costly infinite tool loops.

---

## 🏋️ Exercise 6.2: Generator-Critic Reflection Cycles

**Location**: `starter/reflection_agent.py` → `solution/reflection_framework.py`
**Goal**: Build a self-correction architecture that critiques and improves its own drafted responses.

**Tasks**:
1. Implement a generator function that drafts customer emails.
2. Implement a critic function that scans drafted emails for professional tone and word length constraints.
3. Set up the refinement loop to run exactly twice, passing the critique feedback back to the generator.

---

## 🏋️ Exercise 6.3: Human-in-the-Loop Approval Gates

**Location**: `starter/human_in_the_loop.py` → `solution/human_in_the_loop_hooks.py`
**Goal**: Place security guardrails around high-risk transactions (refunds > $100) that pause execution until human authorization is received.

**Tasks**:
1. Write a check that monitors proposed refund tool payloads.
2. If the amount exceeds $100.00, pause execution and output a pending authorization state.
3. Implement a resume function that receives the human approval string, processes the refund upon "APPROVED", and blocks it upon "REJECTED".
