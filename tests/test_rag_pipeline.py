import src.rag_pipeline as rp

def test_build_faiss_index_exists():
    assert hasattr(rp, 'build_faiss_index'), 'build_faiss_index function should exist'


def test_query_index_exists():
    assert hasattr(rp, 'query_index'), 'query_index function should exist'
