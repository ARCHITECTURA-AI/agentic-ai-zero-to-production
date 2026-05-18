# Module 07: Multi-Agent Collaboration & Orchestration

## What you will learn
- Single vs Multi-Agent architecture trade-offs.
- Implementing the Supervisor/Orchestrator pattern to coordinate team assignments.
- Building Specialist Agents (Billing, Refunds) with customized prompts and tools.
- Formulating robust inter-agent handshake and state exchange boundaries.

## Files in this folder
- `concept_notes.md` — Multi-agent system patterns and Crew structures
- `exercises.md` — detailed specialist routing instructions
- `starter/` — exercise starter templates
  - `supervisor.py` — orchestrator router skeleton
  - `billing_agent.py` — billing domain specialist skeleton
  - `refund_agent.py` — refund domain specialist skeleton
- `solution/` — reference implementations
  - `orchestrator.py` — complete Supervisor orchestration loop with handshake validations
  - `specialist_agents.py` — functional Billing and Refund specialists with custom logic
  - `crew_structures.md` — architectural comparison of LangGraph vs CrewAI orchestration
- `tests/` — validation checks
  - `test_routing.py` — verifies supervisor routes queries to the correct specialist
  - `test_handshakes.py` — verifies state is safely passed between agent boundaries

## Run order
1. Read `concept_notes.md`
2. Follow instructions in `exercises.md`
3. Edit files in `starter/`
4. Run `pytest` to confirm your team orchestrations pass tests
5. Compare your design against `solution/`

## Success criteria
- The Supervisor correctly classifies ticket types and routes queries to specialists.
- Specialists process queries using specialized logic and return structural handshakes.
- Handshake protocol retains case IDs and notes across agent transitions without losing context.

## Common failure modes
- **Orchestration ping-pong**: Specialists passing task states back and forth endlessly. You should enforce strict hop limits.
- **Context fragmentation**: Losing state details (like transaction IDs) when passing payloads between agents. You must use shared schemas or structured handshakes.
- **Vague specialist bounds**: Overlapping agent capabilities causing routing confusion for the Supervisor. You must define clear, distinct agent responsibilities.
