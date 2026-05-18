# Scaling to Production: Migrating from Chromadb to PostgreSQL pgvector

While ChromaDB is excellent for local development, rapid prototyping, and unit tests, enterprise-grade AI applications running in production require standard database capabilities (ACID transactions, parallel indexing, backups, and unified relational queries).

For projects already utilizing a SQL backend, the standard upgrade path is to migrate vector embeddings to **PostgreSQL** with the **pgvector** extension.

---

## 1. Enabling the Extension
To begin using vector stores inside PostgreSQL, enable the extension:
```sql
CREATE EXTENSION IF NOT EXISTS vector;
```

---

## 2. Table Schema Definition
Define a column with the `vector` type. You must declare the fixed dimensions of your target embedding model (e.g., 1536 for OpenAI `text-embedding-3-small` or 384 for standard local models):

```sql
CREATE TABLE corporate_policy_chunks (
    id SERIAL PRIMARY KEY,
    document_name VARCHAR(255) NOT NULL,
    chunk_index INT NOT NULL,
    content TEXT NOT NULL,
    embedding vector(1536) -- Define vector type with dimension constraint
);
```

---

## 3. High-Speed Indexing (HNSW)
By default, PostgreSQL performs an exact flat search (sequential scan), which gets slow as collections grow. To perform fast, approximate nearest neighbor (ANN) searches, create an **HNSW** (Hierarchical Navigable Small World) index:

```sql
CREATE INDEX ON corporate_policy_chunks 
USING hnsw (embedding vector_cosine_ops);
```

---

## 4. Querying Semantic Matches (Python & SQL)
With `pgvector` loaded, you can perform hybrid queries combining metadata filters and semantic similarity in a single standard SQL command. 
The standard operators are:
- `<=>` for Cosine Distance (most common for text embedding comparisons)
- `<->` for Euclidean (L2) Distance
- `<#>` for Negative Inner Product

```python
import psycopg2

def retrieve_policy_pgvector(query_embedding: list, category_filter: str, top_k: int = 3):
    conn = psycopg2.connect("dbname=corporate_kb user=postgres password=secret")
    cur = conn.cursor()
    
    # Combined relational filters and vector cosine similarity search in one query
    sql = """
        SELECT content, (1 - (embedding <=> %s::vector)) AS similarity
        FROM corporate_policy_chunks
        WHERE document_name = %s
        ORDER BY embedding <=> %s::vector
        LIMIT %s;
    """
    
    cur.execute(sql, (query_embedding, category_filter, query_embedding, top_k))
    results = cur.fetchall()
    cur.close()
    conn.close()
    
    return [row[0] for row in results]
```
This migration ensures zero-copy data reads and makes prompt-assembly latency negligible even under heavy concurrent loads.
