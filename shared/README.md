# Shared Abstractions & Helpers

This directory contains core utility modules and helper frameworks designed to enforce enterprise guardrails, log structures, token budgets, and configurations.

These scripts are referenced globally across all modules in the course.

---

## 📁 Shared Module Index

- **[config.py](/shared/config.py)**: Loads environment variables securely and manages system-wide variables.
- **[models.py](/shared/models.py)**: Houses shared Pydantic models for validated state handoffs and routing.
- **[logging_utils.py](/shared/logging_utils.py)**: Standardizes structured JSON logging format.
- **[token_utils.py](/shared/token_utils.py)**: Provides tiktoken-based token counting and budget checks.
- **[eval_utils.py](/shared/eval_utils.py)**: Evaluates semantic similarity, response correctness, and regex structures.
- **[guardrails.py](/shared/guardrails.py)**: Implements step-based, cost-based, and human-in-the-loop validation checkpoints.
- **[mcp_client.py](/shared/mcp_client.py)**: Provides client wrappers to bind Model Context Protocol services.
- **[tracing.py](/shared/tracing.py)**: Configures OpenTelemetry logging pipelines for Arize Phoenix or LangSmith.
- **[costing.py](/shared/costing.py)**: Calculates model completions expenses using lookup schemas.
