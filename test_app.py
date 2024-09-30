import pytest
from app import add, subtract

def test_add():
    assert add(2, 3) == 4

def test_subtract():
    assert subtract(-2, 2) == -4
