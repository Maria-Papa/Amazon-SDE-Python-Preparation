import pytest
from src.array.largest_sum_contiguous_subarray import max_subarray_sum


@pytest.mark.parametrize("arr, expected", [
    ([2, 3, -8, 7, -1, 2, 3], 11), # Mixed signs
    ([-2, -4], -2),                # All negative
    ([5, 4, 1, 7, 8], 25),         # All positive
    ([1], 1),                      # Single element
    ([5, 4, 1, 7, 8], 25),         # Entire array
])
def test_max_subarray_sum(arr, expected):
    assert max_subarray_sum(arr) == expected
