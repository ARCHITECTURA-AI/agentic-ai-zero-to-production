# RAG Architecture: Local Chromadb Vector Pipelines

Building a local RAG vector pipeline inside corporate firewalls requires a reliable, zero-network, local-only architecture. 

```
 ┌──────────────────────┐
 │    Local Documents   │ (e.g. data/knowledge_base/refund_policy.md)
 └──────────┬───────────┘
            ▼
 ┌──────────────────────┐
 │ Character Splitter   │ (Chunk Size: 500 chars, Overlap: 50 chars)
 └──────────┬───────────┘
            ▼
 ┌──────────────────────┐
 │ Embedding Generator  │ (Local mock embeddings or sentence-transformers)
 └──────────┬───────────┘
            ▼
 ┌──────────────────────┐
 │ In-Memory ChromaDB   │ (Local Client, client.create_collection)
 └──────────────────────┘
```

## Core Design Decisions

### 1. In-Memory Vector Storage (ChromaDB)
For development, training environments, and unit testing, we initialize ChromaDB using an in-memory client configuration:
```python
import chromadb
client = chromadb.Client() # Fully self-contained, zero disk state, no external ports
```
In production corporate environments, we transition this client to a persistent local SQLite storage or a server-based PostgreSQL instance:
```python
# Local SQLite SQLite-backed vector store
client = chromadb.PersistentClient(path="./chroma_db")
```

### 2. Mocking Embeddings for Zero-Dependency Testing
To make sure our test suite runs quickly and reliably without hitting external API keys or hitting corporate proxies, we implement a lightweight, deterministic local embedding function.
This function translates text chunks into a mock 128-dimensional vector based on the hash value of the text. This allows us to test indexing, retrieval precision, and top-$k$ sorting without making any external API calls.
In production, this is swapped for a real embedding model (like OpenAI's `text-embedding-3-small` or a local SentenceTransformers model).
