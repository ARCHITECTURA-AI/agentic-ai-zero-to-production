# Shared Abstractions & Helpers

This directory contains core utility modules and helper frameworks designed to enforce enterprise guardrails, log structures, token budgets, and configurations.

These scripts are referenced globally across all modules in the course.

---

## 📁 Shared Module Index

- **[config.py](file:///c:/Users/Richa/OneDrive/Documents/Projects/agentic-ai-zero-to-production/shared/config.py)**: Loads environment variables securely and manages system-wide variables.
- **[models.py](file:///c:/Users/Richa/OneDrive/Documents/Projects/agentic-ai-zero-to-production/shared/models.py)**: Houses shared Pydantic models for validated state handoffs and routing.
- **[logging_utils.py](file:///c:/Users/Richa/OneDrive/Documents/Projects/agentic-ai-zero-to-production/shared/logging_utils.py)**: Standardizes structured JSON logging format.
- **[token_utils.py](file:///c:/Users/Richa/OneDrive/Documents/Projects/agentic-ai-zero-to-production/shared/token_utils.py)**: Provides tiktoken-based token counting and budget checks.
- **[eval_utils.py](file:///c:/Users/Richa/OneDrive/Documents/Projects/agentic-ai-zero-to-production/shared/eval_utils.py)**: Evaluates semantic similarity, response correctness, and regex structures.
- **[guardrails.py](file:///c:/Users/Richa/OneDrive/Documents/Projects/agentic-ai-zero-to-production/shared/guardrails.py)**: Implements step-based, cost-based, and human-in-the-loop validation checkpoints.
- **[mcp_client.py](file:///c:/Users/Richa/OneDrive/Documents/Projects/agentic-ai-zero-to-production/shared/mcp_client.py)**: Provides client wrappers to bind Model Context Protocol services.
- **[tracing.py](file:///c:/Users/Richa/OneDrive/Documents/Projects/agentic-ai-zero-to-production/shared/tracing.py)**: Configures OpenTelemetry logging pipelines for Arize Phoenix or LangSmith.
- **[costing.py](file:///c:/Users/Richa/OneDrive/Documents/Projects/agentic-ai-zero-to-production/shared/costing.py)**: Calculates model completions expenses using lookup schemas.
