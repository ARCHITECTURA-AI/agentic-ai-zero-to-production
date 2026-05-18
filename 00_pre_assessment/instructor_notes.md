# Instructor Notes: Module 00 Calibration

Use these guidelines to calibrate students during Session 1.

---

## 🔑 Expected Answers

### 1. LLM State Persistence
- **Answer**: Standard LLMs are mathematically stateless functions. Memory is managed by compiling history into the prompt payload list on every successive API request.

### 2. The Infinite Loop Problem
- **Answer**: Loop detection and step bounds (e.g., `verify_step_limit()`) raise errors once step counts exceed limits, interrupting runaway recursion.

### 3. Structured Output Parsing
- **Answer**: Free-form texts yield high parsing failure rates. Enforcing Pydantic schemas using native tool calling (e.g. `response_format` or JSON modes) binds parameters to specific types.

### 4. Semantic Evaluation
- **Answer**: Traditional string comparison checks fail. Use keyword checking (`evaluate_keyword_overlap()`) or LLM-as-a-judge scorers.

### 5. Injection Containment
- **Answer**: Prompts are in-band data. System instructions can be easily overridden. Secure architectures use runtime sandboxes (Docker), sandboxed tools, and separate input scanners.
