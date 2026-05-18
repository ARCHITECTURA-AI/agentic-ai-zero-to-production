"""
Starter file for Exercise 4.2.
Orchestrate RAG context assembly and injection within the agent system loop.
"""
from typing import List

def build_rag_prompt(user_query: str, retrieved_contexts: List[str]) -> str:
    """Compiles the final LLM prompt injecting the fetched context segments."""
    # TODO: Create a structured system prompt injecting the retrieved policy segments.
    # Keep it clean and structured.
    
    context_str = "\n---\n".join(retrieved_contexts)
    prompt = f"System: Use only the following context to answer.\nContext:\n{context_str}\nUser: {user_query}"
    
    return prompt
