# Local vs Cloud Embeddings Homework

## Project Overview
In this assignment, you will implement and compare local (open-source) embeddings versus cloud embeddings using a subset of the course corpus. You will measure retrieval quality, latency, and operational metrics to inform a provider decision.

## Repository Structure
```
data/
src/
tests/
notebooks/
README.md
requirements.txt
implementation_notes.md
```

## Reproduction Steps
```bash
git clone <repository-url>
cd homework-yOUJsMhCaBEX
python -m venv .venv
source .venv/bin/activate  # On Windows use: .venv\\Scripts\\activate
pip install -r requirements.txt
```

## Expected Inputs/Outputs
- **Input corpus**: `data/corpus_subset.csv` (CSV with `id,text`)
- **Cloud embeddings**: `data/cloud_embeddings.jsonl`
- **Embeddings output**: NumPy `.npy` file of shape (N, D)
- **Retrieval outputs**: top-5 neighbor IDs per query
- **Metrics**: timing JSON, overlap calculations

## What to Submit and Grading Criteria
- `run_local_embeddings.py` or `local_embedding_inference.ipynb`
- `retrieval_integration.py`
- `compare_notebook.ipynb` or `compare_results.md`
- `implementation_notes.md`
- Passing tests in `tests/`
