# Exercises: Local RAG & Context Management

In this module, you will build a complete local RAG indexing pipeline and hook it up to a robust context budget containment manager.

---

## 🏋️ Exercise 4.1: Policy Document Chunking

**Location**: `starter/index_documents.py` → `solution/chroma_rag_pipeline.py`
**Goal**: Slice large Markdown corporate policies into clean, overlapping textual segments.

**Tasks**:
1. Open `starter/index_documents.py` and inspect the `chunk_text` function.
2. Implement standard sliding window chunking using configured character lengths and overlaps.
3. Validate that chunks are parsed clean of dangling headings and respect boundary parameters.

---

## 🏋️ Exercise 4.2: Local ChromaDB Vector Indexing

**Location**: `starter/retrieve_context.py` → `solution/chroma_rag_pipeline.py`
**Goal**: Ingest corporate policy chunks into a local vector collection and query them semantically.

**Tasks**:
1. Set up an in-memory ChromaDB client.
2. Index policy chunks using local mock embeddings (to prevent proxy, firewall, or external key requirements).
3. Implement `retrieve_relevant_chunks(query: str, top_k: int = 2)` to fetch the most relevant context nodes from the vector store.

---

## 🏋️ Exercise 4.3: Context Token Budget Manager

**Location**: `starter/context_budget.py` → `solution/token_budget_manager.py`
**Goal**: Prevent silent prompt overflow failures by programmatically monitoring prompt token usage and trimming older history.

**Tasks**:
1. Open `starter/context_budget.py`.
2. Use `tiktoken` to count the exact token consumption of standard agent system prompts.
3. Implement a pruner that drops older message logs recursively until the total prompt fits safely inside a predefined maximum token boundary.
