import math_operation
import pytest

def custom_add(x, y):
    return x * y

@pytest.fixture
def monkeypatched_add(monkeypatch):
    monkeypatch.setattr(math_operation, 'add', custom_add)

def test_addition_with_mocked_function(monkeypatched_add):
    result = math_operation.add(3, 4)
    assert result == 12  # 3 * 4 = 12

if __name__ == '__main__':
    # Run the tests using pytest
    pytest.main([__file__])

print(math_operation.add(2,8))