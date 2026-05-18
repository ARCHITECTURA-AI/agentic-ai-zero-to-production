"""
API key connectivity test.
Run this to confirm your API keys work and you can reach
the required services from your network.

Usage:
    python setup/test_api_keys.py
"""

import os
import sys
import time

def load_env():
    """Load environment variables from .env file."""
    try:
        from dotenv import load_dotenv
        load_dotenv()
    except ImportError:
        print("python-dotenv not installed. Run: pip install python-dotenv")
        sys.exit(1)

def test_openai():
    """Test OpenAI API connectivity."""
    print("\n📌 Testing OpenAI...")
    api_key = os.environ.get("OPENAI_API_KEY", "")
    if not api_key:
        print("  ❌ OPENAI_API_KEY not found in .env")
        return False
    try:
        from openai import OpenAI
        client = OpenAI(api_key=api_key)
        start = time.time()
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": "Reply with one word: ready"}],
            max_tokens=5
        )
        elapsed = round(time.time() - start, 2)
        reply = response.choices[0].message.content.strip()
        print(f"  ✅ OpenAI connected ({elapsed}s) → '{reply}'")
        return True
    except Exception as e:
        print(f"  ❌ OpenAI failed: {e}")
        return False

def test_anthropic():
    """Test Anthropic API connectivity (optional)."""
    print("\n📌 Testing Anthropic (optional)...")
    api_key = os.environ.get("ANTHROPIC_API_KEY", "")
    if not api_key:
        print("  ⚠️  ANTHROPIC_API_KEY not set — skipping")
        return True
    try:
        import anthropic
        client = anthropic.Anthropic(api_key=api_key)
        start = time.time()
        response = client.messages.create(
            model="claude-3-haiku-20240307",
            max_tokens=5,
            messages=[{"role": "user", "content": "Reply with one word: ready"}]
        )
        elapsed = round(time.time() - start, 2)
        reply = response.content[0].text.strip()
        print(f"  ✅ Anthropic connected ({elapsed}s) → '{reply}'")
        return True
    except ImportError:
        print("  ⚠️  anthropic not installed — skipping")
        return True
    except Exception as e:
        print(f"  ❌ Anthropic failed: {e}")
        return False

def test_chromadb():
    """Test ChromaDB works locally."""
    print("\n📌 Testing ChromaDB (local)...")
    try:
        import chromadb
        client = chromadb.Client()
        collection = client.create_collection("test_collection")
        collection.add(
            documents=["test document"],
            ids=["test_1"]
        )
        results = collection.query(
            query_texts=["test"],
            n_results=1
        )
        client.delete_collection("test_collection")
        print("  ✅ ChromaDB working locally")
        return True
    except Exception as e:
        print(f"  ❌ ChromaDB failed: {e}")
        return False

def main():
    print("\n" + "="*50)
    print("  Agentic AI: API Key Test")
    print("="*50)

    load_env()

    results = []
    results.append(("OpenAI", test_openai()))
    results.append(("Anthropic", test_anthropic()))
    results.append(("ChromaDB", test_chromadb()))

    print("\n" + "="*50)
    print("  Summary:")
    all_required_passed = True
    for name, passed in results:
        status = "✅" if passed else "❌"
        print(f"  {status}  {name}")
        if name == "OpenAI" and not passed:
            all_required_passed = False

    if all_required_passed:
        print("\n  ✅ Required APIs working. Ready for training.")
    else:
        print("\n  ❌ Required API check failed.")
        print("  Fix OpenAI connection before the training starts.")
        print("  See setup/install.md for help.")
    print("="*50 + "\n")

    return 0 if all_required_passed else 1

if __name__ == "__main__":
    sys.exit(main())
