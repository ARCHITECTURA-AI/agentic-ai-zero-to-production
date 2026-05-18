"""
Starter file for Exercise 4.2.
Query and retrieve semantic context from a local, in-memory ChromaDB database.
"""
from typing import List, Dict, Any
import chromadb

def setup_in_memory_kb(documents: List[str]) -> Any:
    """Sets up an in-memory ChromaDB database and indexes the supplied documents.
    
    To make testing fully reliable, use a local, mock-embedding function.
    """
    # TODO:
    # 1. Initialize an in-memory chromadb Client.
    # 2. Create a collection named "policies".
    # 3. Add documents into the collection with simple, unique metadata and string IDs.
    # 4. Return the collection object.
    
    client = chromadb.Client()
    collection = client.create_collection("policies")
    
    # Write indexing loop here:
    
    return collection

def retrieve_relevant_chunks(collection: Any, query: str, top_k: int = 2) -> List[str]:
    """Queries the ChromaDB collection and returns top-k matching documents."""
    # TODO: Query the collection with the search query.
    # Return a list of plain string matching documents.
    
    return []
