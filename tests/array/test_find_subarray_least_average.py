import pytest
from src.array.find_subarray_least_average import find_subarray_least_avg

@pytest.mark.parametrize("arr, k, expected", [
    ([3, 7, 90, 20, 10, 50, 40], 3, [20, 10, 50]),         # Array with positives
    ([3, 7, 5, 20, -10, 0, 12], 2, [-10, 0]),              # Mixed array
    ([4, 65, 834, 43, -2], 5, [4, 65, 834, 43, -2]),       # Only one possible subarray
    ([4, 56, -3, 5, 100], 1, [-3]),                        # Find the smallest element
    ([-3, -100, -89, -4, -976], 4, [-100, -89, -4, -976]), # Array with negatives
    ([6, 6, 6, 6, 6, 6, 6], 2, [6, 6])                     # All elements same
])
def test_find_subarray_least_avg(arr, k , expected):
    assert find_subarray_least_avg(arr, k) == expected
