# Pre-Assessment Calibration Quiz

Examine your understanding of autonomous engineering before starting Module 1.

---

### Question 1: LLM State Persistence
Explain why a standard LLM completion call is stateless and how agentic frameworks maintain memory across separate tool execution loops.

---

### Question 2: The Infinite Loop Problem
What code mechanisms prevent a ReAct agent from recursively querying the same calculator tool endlessly when it fails to parse a calculation result?

---

### Question 3: Structured vs. Unstructured Parsing
Why is it dangerous to allow an LLM to select tool handoffs by outputting free-form conversational text, and how does Pydantic schema validation enforce structural bounds?

---

### Question 4: Semantic Evaluation
How do you automatically verify that a customer support agent returned the correct cancellation instructions if the exact phrasing changes across completions?

---

### Question 5: Injection Containment
Why are simple system prompts ("Do not share secrets") vulnerable to indirect injection attacks, and what architectural containment measures secure production runtimes?
