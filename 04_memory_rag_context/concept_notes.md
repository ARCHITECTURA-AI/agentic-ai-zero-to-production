# Concept Notes: Memory, RAG & Context Management

AI Agents need access to domain-specific knowledge to make informed decisions. However, they are bounded by strict constraints:

## 1. Short-Term vs. Long-Term Memory

In agentic systems, memory is divided into two primary dimensions:
- **Short-Term Memory**: The ongoing conversation context, past execution steps, and intermediate thoughts inside the agent loop. This is ephemeral, volatile, and lives inside the prompt history (e.g. system state arrays or LangGraph state variables).
- **Long-Term Memory**: The permanent repository of information, rules, and facts (e.g. corporate policies, product schemas, user profiles). This is persistent, external, and queried on-demand.

---

## 2. Retrieval-Augmented Generation (RAG)

Instead of training or fine-tuning models on corporate documents—which is expensive, slow, and hard to update—we use **Retrieval-Augmented Generation (RAG)**:
1. **Ingest**: Convert corporate text documents (e.g., HR manuals, customer support ticket logs) into manageable segments (chunks).
2. **Embed**: Send these chunks through an embedding model (like OpenAI's `text-embedding-3-small` or standard local models) to represent the semantic meaning of each segment as a high-dimensional mathematical vector (e.g., 1536 dimensions).
3. **Index**: Store these vectors in a specialized vector database (ChromaDB, Pgvector, Pinecone).
4. **Retrieve**: When a customer files a ticket, convert their query into a query vector, calculate similarity (e.g., Cosine Similarity) against the index, and retrieve the top-$k$ most similar document chunks.
5. **Generate**: Insert these chunks into the LLM system prompt as verified context before calling the completion API.

```
                  ┌──────────────────────┐
                  │   Corporate Policy   │
                  └──────────┬───────────┘
                             ▼ (Chunk & Embed)
                  ┌──────────────────────┐
                  │   Vector Database    │
                  └──────────▲───────────┘
                             │
     Customer ticket ────────┼──────── (Retrieve top-k)
                             ▼
┌────────────────────────────────────────────────────────┐
│                      Agent Loop                        │
│                                                        │
│   System Prompt:                                       │
│   "Use this context to resolve the issue:              │
│    [Retrieved Policy Chunk]"                           │
│                                                        │
│   LLM generates validated resolution                   │
└────────────────────────────────────────────────────────┘
```

---

## 3. Context Health & Token Budgets

Large context windows (e.g., 1 million tokens in Gemini) have led to lazy prompt design. In production, stuffing entire manuals into the system prompt has major downsides:
1. **Extreme Latency**: Time-to-First-Token (TTFT) scales with the size of the input prompt. High latency frustrates users.
2. **Escalating Costs**: Every token sent to the model incurs a cost. Unmanaged prompts quickly blow through corporate budgets.
3. **Lost in the Middle**: LLMs often ignore details placed in the middle of long prompts. Keeping context short and highly relevant improves accuracy.

**The Golden Rules of Context Management**:
- **Sweet Spot Chunk Sizes**: 500-1000 characters (approx. 100-250 tokens) is optimal for retrieving specific details without bloated context.
- **Dynamic Pruning**: Programmatically monitor the total token size of the prompt using `tiktoken` and truncate or exclude older conversation history or lower-relevance chunks before hitting the model API.
