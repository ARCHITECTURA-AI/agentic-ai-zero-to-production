# Module 06: Single-Agent Design Patterns: ReAct, Reflection & Human-In-The-Loop

## What you will learn
- The ReAct (Reasoning + Action) execution loop mechanics.
- Setting up a Reflection agent pattern where critiques drive output refinement.
- Integrating Human-in-the-Loop (HITL) approval hooks for high-risk actions.
- Logging and tracking intermediate agent trajectories.

## Files in this folder
- `concept_notes.md` — ReAct, Reflection, and HITL patterns
- `exercises.md` — guided instructions for building the loops
- `starter/` — exercise starter templates
  - `react_agent.py` — skeleton for the Thought-Action-Observation loop
  - `reflection_agent.py` — skeleton for the Generation-Critique cycle
  - `human_in_the_loop.py` — skeleton for pausing and requesting approval
- `solution/` — reference implementations
  - `react_framework.py` — fully functioning ReAct core runner with memory
  - `reflection_framework.py` — complete Generator-Reflector critique execution agent
  - `human_in_the_loop_hooks.py` — privilege boundaries with human feedback injection
  - `agent_visualization.md` — Mermaid flowcharts showing execution cycles
- `tests/` — validation checks
  - `test_react_loop.py` — verifies ReAct alternates correctly
  - `test_reflection_loop.py` — verifies critique feedback loops
  - `test_human_loop.py` — guarantees that the execution loop pauses and resumes on approval

## Run order
1. Read `concept_notes.md`
2. Follow instructions in `exercises.md`
3. Edit the files in `starter/`
4. Run `pytest` to confirm your loops operate correctly
5. Compare your design against `solution/`

## Success criteria
- ReAct loops successfully trace thoughts, trigger appropriate tools, and capture observations.
- Reflection loops correctly refine an unpolished draft over 2 iterations.
- Human-in-the-Loop locks high-value operations (e.g., refunds > $100) until explicit approval is granted.

## Common failure modes
- **Infinite execution loops**: ReAct loops spinning endlessly when the model repeats thoughts. You must set a strict `max_iterations` counter.
- **Over-reflection**: Endless generation-critique cycles degrading quality or raising costs. You should limit reflections to 1 or 2 rounds.
- **Bypassing HITL hooks**: Writing fragile conditions that fail to catch edge-case high-risk actions. You should implement strict validation boundaries.
