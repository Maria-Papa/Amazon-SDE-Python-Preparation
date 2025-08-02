import pytest
from src.array.find_subarray_least_average import find_subarray_least_avg


@pytest.mark.parametrize("arr, k, expected", [
    ([3, 7, 90, 20, 10, 50, 40], 3, (3, 5)), # Window (20, 10, 50)
    ([3, 7, 5, 20, -10, 0, 12], 2, (4, 5)),  # Window (-10, 0)
    ([4, 65, 834, 43, -2], 5, (0, 4)),       # Whole array
    ([4, 56, -3, 5, 100], 1, (2, 2)),        # Smallest single element
    ([-3, -100, -89, -4, -976], 4, (1, 4)),  # Negative values
    ([6, 6, 6, 6, 6], 2, (0, 1))             # All same values
])
def test_find_subarray_least_avg(arr, k, expected):
    assert find_subarray_least_avg(arr, k) == expected
