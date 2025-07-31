import pytest
from src.array.count_pairs_with_given_sum import count_pairs

@pytest.mark.parametrize("arr, target, expected", [
    ([1, 5, 7, -1, 5], 6, 3),       # (1,5), (7,-1), (1,5)
    ([1, 1, 1, 1], 2, 6),           # All combinations of (1,1)
    ([10, 12, 10, 15, -1], 125, 0), # No pairs
    ([0, 0, 0], 0, 3),              # (0,0), (0,0), (0,0)
    ([], 4, 0),                     # Empty array
    ([3], 3, 0),                    # Single element
])
def test_count_pairs(arr, target, expected):
    assert count_pairs(arr, target) == expected
