# tests/test_integration.py

from app.main import add, multiply

def test_add_and_multiply():
    result = add(2, 3)
    assert multiply(result, 2) == 10

