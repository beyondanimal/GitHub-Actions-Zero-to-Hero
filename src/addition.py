# app.py
# This is not a test commit but to check the pipeline
def add(a, b):
    return a + b

def test_add():
    assert add(1, 2) == 3
    assert add(1, -1) == 0
