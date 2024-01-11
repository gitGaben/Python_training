# test_my_module.py
import pytest
from my_module import Sleeper

class A:
        x = 1

def test_delattr():
    monkeypatch = pytest.MonkeyPatch()
    monkeypatch.delattr(A, 'x')
    assert not hasattr(A, 'x')
    monkeypatch.undo()

def test_attr():
    assert A.x == 1

if __name__ == '__main__':
    # Run the tests using pytest
    pytest.main([__file__])