# Troubleshooting Guide

This guide describes how to diagnose and resolve typical errors during workspace setup and course execution.

---

## 🐍 Environment & Pip Install Issues

### 1. "Python not found" or "Unsupported Python Version"
- **Symptom**: Running `python` fails or displays a version older than `3.10`.
- **Fix**: 
  - Windows: Verify that Python is added to your environment `PATH` variables.
  - Linux/Mac: Install Python via `pyenv` or your system packager (e.g., `brew install python@3.10`).

### 2. "ModuleNotFoundError: No module named '...'"
- **Symptom**: Code crashes with import errors.
- **Fix**: Confirm that your python virtual environment is activated:
  - Windows: `.venv\Scripts\activate`
  - Mac/Linux: `source .venv/bin/activate`
  - Re-run: `pip install -r requirements.txt`

---

## 🔑 API & Connectivity Failures

### 1. "AuthenticationError: No API key provided"
- **Symptom**: Chat completions throw key exceptions.
- **Fix**: 
  - Ensure that `.env` is located in the root of the workspace.
  - Check that keys do not contain trailing whitespaces or quotation marks:
    ```bash
    # Correct
    OPENAI_API_KEY=sk-proj-...
    
    # Incorrect
    OPENAI_API_KEY = "sk-proj-... "
    ```

### 2. Connection Timeout / Proxy Blocks
- **Symptom**: `httpx.ConnectError` or similar network exceptions.
- **Fix**: Add proxy exceptions or bypass corporate proxy check steps using mock environment variables (see [setup/install.md](file:///c:/Users/Richa/OneDrive/Documents/Projects/agentic-ai-zero-to-production/setup/install.md)).

---

## 🗄️ Vector Database (ChromaDB) Crashes

### 1. SQLite Version Incompatibility
- **Symptom**: `chromadb` fails with an exception saying SQLite version is too old.
- **Fix**: Install `pysqlite3-binary` and override sqlite3 before importing chromadb:
  ```python
  import sys
  __import__('pysqlite3')
  sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')
  ```
