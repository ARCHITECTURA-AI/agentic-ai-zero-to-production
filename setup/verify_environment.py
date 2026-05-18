"""
Environment verification script.
Run this before the training starts to confirm everything is set up correctly.

Usage:
    python setup/verify_environment.py
"""

import sys
import os
import importlib

def check(label: str, condition: bool, fix: str = "") -> bool:
    """Print a check result."""
    status = "✅" if condition else "❌"
    print(f"  {status}  {label}")
    if not condition and fix:
        print(f"       Fix: {fix}")
    return condition

def check_import(module_name: str, display_name: str = None) -> bool:
    """Try to import a module and report result."""
    name = display_name or module_name
    try:
        importlib.import_module(module_name)
        return check(f"{name} installed", True)
    except ImportError:
        return check(
            f"{name} installed",
            False,
            f"pip install {module_name}"
        )

def main():
    print("\n" + "="*50)
    print("  Agentic AI: Environment Verification")
    print("="*50 + "\n")

    all_passed = True

    # Python version
    print("📌 Python version:")
    version = sys.version_info
    passed = version.major == 3 and version.minor >= 10
    all_passed &= check(
        f"Python {version.major}.{version.minor} (need 3.10+)",
        passed,
        "Download Python 3.10+ from python.org"
    )

    # Core dependencies
    print("\n📌 Core dependencies:")
    packages = [
        ("openai", "openai"),
        ("pydantic", "pydantic"),
        ("langgraph", "langgraph"),
        ("crewai", "crewai"),
        ("chromadb", "chromadb"),
        ("tiktoken", "tiktoken"),
        ("pytest", "pytest"),
        ("httpx", "httpx"),
        ("dotenv", "python-dotenv"),
        ("requests", "requests"),
    ]
    for module, display in packages:
        all_passed &= check_import(module, display)

    # Observability (optional)
    print("\n📌 Observability (optional but recommended):")
    obs_packages = [
        ("opentelemetry.api", "opentelemetry-api"),
    ]
    for module, display in obs_packages:
        check_import(module, display)

    # Environment variables
    print("\n📌 Environment variables:")
    try:
        from dotenv import load_dotenv
        load_dotenv()
    except ImportError:
        pass

    required_vars = [
        ("OPENAI_API_KEY", "OpenAI API key"),
    ]
    optional_vars = [
        ("ANTHROPIC_API_KEY", "Anthropic API key"),
        ("LANGSMITH_API_KEY", "LangSmith API key"),
    ]

    for var, label in required_vars:
        value = os.environ.get(var, "")
        passed = bool(value) and len(value) > 10
        all_passed &= check(
            f"{label} present",
            passed,
            f"Add {var}=your_key to .env file"
        )

    for var, label in optional_vars:
        value = os.environ.get(var, "")
        check(f"{label} present (optional)", bool(value))

    # Final result
    print("\n" + "="*50)
    if all_passed:
        print("  ✅ All checks passed. You are ready for the training.")
    else:
        print("  ❌ Some checks failed.")
        print("  Fix the issues above and run this script again.")
        print("  See setup/install.md for help.")
    print("="*50 + "\n")

    return 0 if all_passed else 1

if __name__ == "__main__":
    sys.exit(main())
