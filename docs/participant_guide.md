# Participant Guide

Welcome to the **Agentic AI: Zero to Production** hands-on training course! This guide outlines how to prepare and successfully navigate this technical curriculum.

---

## 🏁 Prerequisites & Setup Check

Prior to Session 1, you must perform these steps:
1. Confirm that you have **Python 3.10+** and **git** installed.
2. Complete all steps in the [Installation Guide](/setup/install.md).
3. Ensure your local verification scripts run successfully:
   ```bash
   python setup/verify_environment.py
   python setup/test_api_keys.py
   ```
4. Verify that the local test framework is working:
   ```bash
   pytest
   ```

---

## 🛠️ Sandbox Structure

Every numbered module folder (`00` to `12`) contains the following components:
1. **`README.md`**: Outlines learning goals, file directories, run orders, success metrics, and typical pitfalls.
2. **`concept_notes.md`**: Provides core theoretical context and technical designs.
3. **`exercises.md`**: Details hands-on instructions for coding the exercise.
4. **`starter/`**: Contains broken or partially complete boilerplate code with `# TODO` blocks.
5. **`solution/`**: Contains fully implemented, working solutions to cross-reference if you get stuck.
6. **`tests/`**: Contains custom pytest assertions that verify your starter or solution implementation.

---

## 🎓 Tips for Success

- **Write tests first**: Module 05 teaches evaluation-driven design. Build your validation metrics before writing your prompt strings!
- **Track token limits**: Watch your LLM costs and execution lengths in Module 02. Loops can consume credits rapidly!
- **Harden input parsing**: In Module 03, focus on structured output schemas. Always enforce Pydantic types to prevent failures.
- **Reference shared scripts**: Do not rewrite basic tokenizers or configurations. Utilize the [shared/](/shared) folder utility functions.
