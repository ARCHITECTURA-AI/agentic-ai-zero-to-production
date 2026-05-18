# Exercises: Multi-Agent Collaboration & Orchestration

In this module, you will build a cooperative multi-agent team capable of routing, solving, and handing off task states securely.

---

## 🏋️ Exercise 7.1: Implementing the Supervisor Orchestrator

**Location**: `starter/supervisor.py` → `solution/orchestrator.py`
**Goal**: Build a supervisor routing loop that parses customer queries and delegates them to the appropriate domain specialist.

**Tasks**:
1. Open `starter/supervisor.py` and inspect the `route_ticket` skeleton.
2. Implement logic to classify incoming queries based on intent (refund, billing, or shipping).
3. Connect the router to trigger your specialist agents and return a compiled team response.

---

## 🏋️ Exercise 7.2: Structuring Specialist Handshakes

**Location**: `starter/billing_agent.py` & `starter/refund_agent.py` → `solution/specialist_agents.py`
**Goal**: Define a strict handshake payload structure to exchange case IDs and execution states safely between agents.

**Tasks**:
1. Implement the Specialist response payload, containing a mandatory case state dictionary.
2. Ensure that when a specialist completes a sub-task, it includes `case_id`, a `status` indicator, and a `summary` of its work.
3. Validate that the supervisor can unpack this payload and print a clean final summary for the user.

---

## 🏋️ Exercise 7.3: Mitigating Routing Hops (Ping-Pong Defense)

**Location**: `solution/orchestrator.py`
**Goal**: Prevent infinite routing loops (where Specialist A repeatedly hands a ticket back to Specialist B) by implementing an active hop counter.

**Tasks**:
1. Add a `hop_count` tracking variable to the handshake payload.
2. Increment `hop_count` on every agent transfer.
3. If `hop_count` exceeds 3, abort the transaction and escalate the ticket to a human manager.
