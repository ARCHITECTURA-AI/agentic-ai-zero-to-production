import pytest
import importlib
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

chroma_rag_pipeline = importlib.import_module("04_memory_rag_context.solution.chroma_rag_pipeline")
chunk_text = chroma_rag_pipeline.chunk_text

def test_chunk_text_normal():
    """Verify that text is correctly sliced into chunk sizes."""
    text = "abcdefghijklmnop"  # 16 chars
    # Size 5, overlap 2.
    # Chunk 1: indices 0 to 5 -> 'abcde'
    # Next start: 5 - 2 = 3.
    # Chunk 2: indices 3 to 8 -> 'defgh'
    # Next start: 8 - 2 = 6.
    # Chunk 3: indices 6 to 11 -> 'ghijk'
    # Next start: 11 - 2 = 9.
    # Chunk 4: indices 9 to 14 -> 'jklmn'
    # Next start: 14 - 2 = 12.
    # Chunk 5: indices 12 to 17 -> 'mnop'
    chunks = chunk_text(text, chunk_size=5, chunk_overlap=2)
    assert chunks[0] == "abcde"
    assert chunks[1] == "defgh"
    assert chunks[-1] == "mnop"

def test_chunk_text_overlap_error():
    """Verify that configuring overlap equal to or greater than chunk size raises error."""
    text = "short text block"
    with pytest.raises(ValueError):
        chunk_text(text, chunk_size=10, chunk_overlap=10)

def test_chunk_text_very_short():
    """Verify that text shorter than chunk size returns a single clean chunk."""
    text = "short"
    chunks = chunk_text(text, chunk_size=50, chunk_overlap=5)
    assert len(chunks) == 1
    assert chunks[0] == "short"
