"""
Solution file for Exercise 4.1 & 4.2.
Implements document chunking, indexing, and semantic vector retrieval in ChromaDB.
"""
from typing import List, Any
import uuid
import chromadb

def chunk_text(text: str, chunk_size: int = 500, chunk_overlap: int = 50) -> List[str]:
    """Slices text into overlapping character chunks using a sliding window.
    
    Args:
        text: Raw document text string.
        chunk_size: Target character limit per chunk.
        chunk_overlap: Overlap character limit between successive segments.
        
    Raises:
        ValueError: If overlap is greater than or equal to chunk_size.
    """
    if chunk_overlap >= chunk_size:
        raise ValueError("Overlap must be strictly less than chunk size.")
        
    chunks = []
    start = 0
    text_len = len(text)
    
    while start < text_len:
        end = start + chunk_size
        chunk = text[start:end]
        chunks.append(chunk)
        
        # If the window has reached or passed the end of the text, terminate
        if end >= text_len:
            break
            
        start += chunk_size - chunk_overlap
        
    return chunks

def setup_in_memory_kb(documents: List[str]) -> Any:
    """Sets up an in-memory ChromaDB collection and populates it with document chunks."""
    client = chromadb.Client()
    collection_name = f"policies_{uuid.uuid4().hex[:8]}"
    collection = client.create_collection(collection_name)
    
    # Batch load items securely
    for i, doc in enumerate(documents):
        collection.add(
            documents=[doc],
            metadatas=[{"source": f"policy_doc_{i}"}],
            ids=[f"chunk_{i}"]
        )
        
    return collection

def retrieve_relevant_chunks(collection: Any, query: str, top_k: int = 2) -> List[str]:
    """Queries local database and outputs matching plaintext document segments."""
    results = collection.query(
        query_texts=[query],
        n_results=top_k
    )
    
    if results and "documents" in results and results["documents"]:
        # Return the flat list of extracted texts
        return results["documents"][0]
        
    return []
