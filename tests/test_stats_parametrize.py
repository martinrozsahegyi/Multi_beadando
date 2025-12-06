import pytest
from statistics import mean

@pytest.mark.parametrize("data, expected", [
    ([1, 2, 3], {"min": 1, "max": 3, "avg": 2}),
    ([10, 20, 30], {"min": 10, "max": 30, "avg": 20}),
])
def test_stats(data, expected):
    assert min(data) == expected["min"]
    assert max(data) == expected["max"]
    assert mean(data) == expected["avg"]
