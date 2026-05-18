"""
Starter file for Exercise 4.1.
Implement text chunking strategies for corporate policy documents.
"""
from typing import List

def chunk_text(text: str, chunk_size: int = 500, chunk_overlap: int = 50) -> List[str]:
    """Slices raw text into overlapping textual chunks of size `chunk_size` characters.
    
    Args:
        text: Raw document text string.
        chunk_size: Target size of each chunk in characters.
        chunk_overlap: Size of overlapping context between adjacent chunks.
        
    Returns:
        List of chunk strings.
    """
    # TODO: Implement character-based sliding window chunking with overlap
    # Ensure chunk_overlap is strictly less than chunk_size.
    # Return a list of text segments.
    
    if chunk_overlap >= chunk_size:
        raise ValueError("Overlap must be strictly less than chunk size.")
        
    chunks = []
    # Write sliding window index logic here:
    
    return chunks
