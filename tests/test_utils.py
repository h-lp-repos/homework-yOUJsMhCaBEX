import src.utils as utils

def test_load_corpus_exists():
    assert hasattr(utils, 'load_corpus'), 'load_corpus function should exist'


def test_save_embeddings_exists():
    assert hasattr(utils, 'save_embeddings'), 'save_embeddings function should exist'
