# Module 02: Building the Agent Loop from Scratch

In this module, you will peel back framework layers and write a robust, production-ready, manual agent loop in pure Python. You will implement active step limiters, loop detectors, and token costing safeguards to protect credit resources.

---

## 📂 Folder Index

- **[concept_notes.md](file:///c:/Users/Richa/OneDrive/Documents/Projects/agentic-ai-zero-to-production/02_agent_loop/concept_notes.md)**: Details manual agent loops, prompt compiling, and action execution.
- **[exercises.md](file:///c:/Users/Richa/OneDrive/Documents/Projects/agentic-ai-zero-to-production/02_agent_loop/exercises.md)**: Steps to diagnose and harden loops.
- **[starter/stage1_broken_loop.py](file:///c:/Users/Richa/OneDrive/Documents/Projects/agentic-ai-zero-to-production/02_agent_loop/starter/stage1_broken_loop.py)**: A runaway infinite cycle agent loop script.
- **[starter/stage2_partial_loop.py](file:///c:/Users/Richa/OneDrive/Documents/Projects/agentic-ai-zero-to-production/02_agent_loop/starter/stage2_partial_loop.py)**: Loop with basic tool calls but zero cost safety bounds.
- **[solution/production_agent_loop.py](file:///c:/Users/Richa/OneDrive/Documents/Projects/agentic-ai-zero-to-production/02_agent_loop/solution/production_agent_loop.py)**: Fully hardened pure Python agent loop with logging, costing, and step safety.
- **[tests/test_agent_loop.py](file:///c:/Users/Richa/OneDrive/Documents/Projects/agentic-ai-zero-to-production/02_agent_loop/tests/test_agent_loop.py)**: Verifies step budgets, costing halts, and infinite loops detection.
