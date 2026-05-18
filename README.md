# Agentic AI: Zero to Production

A comprehensive, hands-on developer training program designed to take you from a basic understanding of LLMs to building production-ready, safe, observable, and validated Agentic AI applications.

---

## 🗺️ Course Roadmap & Progression

The repository is structured sequentially to allow a step-by-step learning progression:

```
agentic-ai-zero-to-production/
│
├── setup/                             # Installation & API key verification tests
│
├── docs/                              # Learning guides, rubrics, and pattern catalogs
│
├── shared/                            # Core shared abstractions (logging, guardrails, tokens, evals)
│
├── data/                              # Sandboxed corporate tickets, knowledge base, & broken scripts
│
├── 00_pre_assessment/                 # Calibration phase
├── 01_foundations/                    # Chatbot vs Copilot vs Autonomous Agent framework
├── 02_agent_loop/                     # Designing the core loop, loop detection, and safety budget
├── 03_tools_structured_outputs_mcp/   # Type-safe schemas and Model Context Protocol integrations
├── 04_memory_rag_context/             # In-memory retrieval pipelines & token context management
├── 05_eval_basics/                    # Continuous integration testing & Unit evaluation suites
├── 06_design_patterns/                # Building ReAct, Reflection, Planning, and HITL patterns
├── 07_multi_agent/                    # Hierarchical structures, handoffs, and Graph execution (LangGraph/CrewAI)
├── 08_advanced_eval_observability/    # Tracing, mock LLM execution, OpenTelemetry monitoring
├── 09_production_security_enterprise/ # Sandbox isolation, dangerous tools protection, and RBAC gates
├── 10_failure_modes/                  # Vulnerabilities, injection injection, and mitigation strategies
├── 11_capstone/                       # Capstone projects & build prompts
└── 12_post_course/                    # 30-60-90 Day Production Execution Plan
```

---

## 🚀 Quick Start Setup

### 1. Prerequisites
- **Python**: `>=3.10`
- **OpenAI API Key**: (Required for course execution)
- **Pip / Virtualenv**

### 2. Environment Installation
Clone this workspace and run:
```bash
# Create a virtual environment
python -m venv venv

# Activate on Windows
.\venv\Scripts\activate

# Install requirements
pip install -r requirements.txt
```

### 3. Diagnose Setup & Connection
Verify that your environmental imports and API credentials work correctly:
```bash
# 1. Copy sample variables
copy setup\sample.env .env

# 2. Add your keys to the .env file

# 3. Run diagnostics
python setup/verify_environment.py
python setup/test_api_keys.py
```

### 4. Running the Tests
To ensure all course exercises and solution validations compile and run seamlessly, execute:
```bash
pytest
```

---

## 🎯 Course Goals

1. **Move past wrappers**: Understand the low-level state-loops of autonomous systems.
2. **Deterministic safety**: Build guardrails that enforce max budgets, loop detection, and schema validation.
3. **Enterprise Hardening**: Learn sandboxed script execution, human-in-the-loop escalation paths, and prompt-injection barriers.
4. **Data-Driven Engineering**: Leverage automated tests and offline evals instead of "vibes-based" prompting.

---

## 📄 License
This repository is licensed under the MIT License. See [LICENSE](file:///c:/Users/Richa/OneDrive/Documents/Projects/agentic-ai-zero-to-production/LICENSE) for details.