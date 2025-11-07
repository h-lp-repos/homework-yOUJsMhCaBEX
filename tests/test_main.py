import src.main as main_module

def test_run_local_embeddings_exists():
    assert hasattr(main_module, 'run_local_embeddings'), 'run_local_embeddings function should exist'


def test_main_callable():
    assert callable(main_module.main), 'main should be callable'
