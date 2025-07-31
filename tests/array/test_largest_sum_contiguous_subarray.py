import pytest
from src.array.largest_sum_contiguous_subarray import max_subarray_sum

@pytest.mark.parametrize("input, expected", [
    ([2, 3, -8, 7, -1, 2, 3], 11),
    ([-2, -4], -2),
    ([5, 4, 1, 7, 8], 25),
    ([1], 1),
])
def test_max_subarray_sum(input, expected):
    assert max_subarray_sum(input) == expected
    