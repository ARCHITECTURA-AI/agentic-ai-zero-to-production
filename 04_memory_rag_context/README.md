# Module 04: Local RAG Pipeline & Context Management

## What you will learn
- Document chunking strategies, including token count sweet spots and overlaps.
- Setting up a local, zero-network vector storage system (ChromaDB) for secure corporate data.
- Querying and retrieving high-relevance semantic contexts for prompt construction.
- Dynamic context token budget management and window health metrics.

## Files in this folder
- `concept_notes.md` — memory vs RAG vs static context window trade-offs
- `rag_architecture.md` — workflow diagram and design criteria for local indices
- `exercises.md` — practical instructions for building the vector pipelines
- `starter/` — skeleton templates
  - `index_documents.py` — document processing and vector loading skeleton
  - `retrieve_context.py` — semantic retrieval query skeleton
  - `rag_agent.py` — orchestrating retrieval context injection into the loop
  - `context_budget.py` — basic prompt trimming utility
- `solution/` — reference implementations
  - `chroma_rag_pipeline.py` — fully functional ChromaDB indexer and retriever
  - `token_budget_manager.py` — advanced context pruning, validation, and metadata filtering
  - `pgvector_notes.md` — blueprint reference for migrating to PostgreSQL pgvector
  - `context_health_checks.py` — runtime check utility for warning on token bloat
- `tests/` — validation checks
  - `test_chunking.py` — verifies overlap and character token boundaries
  - `test_retrieval_quality.py` — checks precision and vector retrieval ranking
  - `test_context_budget.py` — guarantees context limits are enforced during token injection

## Run order
1. Read `concept_notes.md` and `rag_architecture.md`
2. Open `exercises.md` for steps
3. Edit the templates in `starter/`
4. Run `pytest` to confirm operations
5. Check your work against the `solution/` implementations

## Success criteria
- Chunking methods correctly slice corporate policies with configured character bounds and overlap.
- ChromaDB loads documents and retrieves the exact relevant section given custom questions.
- Token budget utility trims prompt context to fit standard context limits safely.

## Common failure modes
- Large chunk overlap leading to duplicate information, bloating context and raising pricing.
- No semantic fallback when vector databases return zero matches or noisy irrelevant nodes.
- Exceeding maximum LLM input tokens (Silent Context Overflow) resulting in prompt truncation.
