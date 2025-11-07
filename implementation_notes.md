# Implementation Notes

## Framework Usage
Using frameworks such as LangChain, LlamaIndex, or similar for embedding generation, indexing, retrieval, or ranking is **allowed**.

## Documentation Requirements
You must document in this file:
1. The steps you delegated to frameworks (e.g., embedding, indexing, retrieval, ranking).
2. Pseudocode or helper snippets showing step-by-step RAG pipeline:
```python
# Question → Embedding
query_vec = model.encode([question])[0]

# Indexing → Retrieval
index = faiss.IndexFlatL2(dim)
index.add(embeddings)
D, I = index.search(query_vec.reshape(1, -1), top_k)

# Ranking
results = [corpus_ids[i] for i in I[0]]
```
3. Instructions to run custom code outside frameworks.
