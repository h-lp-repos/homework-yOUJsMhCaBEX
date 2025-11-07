import os

def test_structure():
    expected = [
        'data', 'src', 'tests', 'notebooks', 'README.md',
        'requirements.txt', 'implementation_notes.md'
    ]
    items = os.listdir(os.getcwd())
    for e in expected:
        assert e in items, f"Expected {e} in project root"
