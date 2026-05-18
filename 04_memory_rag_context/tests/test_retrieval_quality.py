import pytest
import importlib
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

chroma_rag_pipeline = importlib.import_module("04_memory_rag_context.solution.chroma_rag_pipeline")
setup_in_memory_kb = chroma_rag_pipeline.setup_in_memory_kb
retrieve_relevant_chunks = chroma_rag_pipeline.retrieve_relevant_chunks

def test_retrieval_finds_correct_chunk():
    """Verify that a vector query retrieves the most similar policy chunk from ChromaDB."""
    documents = [
        "Refund Policy: Customers can request a full refund within 30 days of purchase.",
        "Shipping Policy: Standard shipping takes 3-5 business days to arrive.",
        "Privacy Policy: We do not share customer data with third parties."
    ]
    
    collection = setup_in_memory_kb(documents)
    
    # Query for refund info
    results = retrieve_relevant_chunks(collection, query="How do I get a refund?", top_k=1)
    assert len(results) == 1
    assert "Refund Policy" in results[0]
    
    # Query for shipping info
    results_shipping = retrieve_relevant_chunks(collection, query="delivery shipping time", top_k=1)
    assert len(results_shipping) == 1
    assert "Shipping Policy" in results_shipping[0]
