# Exercises: Module 02 - Developing and Hardening Agent Loops

## 🛠️ Tasks

1. **Investigate Runaway Loops**: Open [starter/stage1_broken_loop.py](./02_agent_loop/starter/stage1_broken_loop.py) and identify the flaw leading to an infinite cycle.
2. **Review Stage 2**: Open [starter/stage2_partial_loop.py](./02_agent_loop/starter/stage2_partial_loop.py) and note how the lack of cost guardrails leaves the program vulnerable to financial budget runaway.
3. **Analyze Solution**: Compare these with [solution/production_agent_loop.py](./02_agent_loop/solution/production_agent_loop.py) to study the implementation of structured safety gates.
4. **Validate**:
   ```bash
   pytest 02_agent_loop
   ```
