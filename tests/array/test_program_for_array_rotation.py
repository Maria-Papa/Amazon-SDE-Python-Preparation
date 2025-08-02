import pytest
from src.array.program_for_array_rotation import array_rotate_1, array_rotate_2, array_rotate_3

@pytest.mark.parametrize("arr, d, expected", [
    ([1, 2, 3, 4, 5, 6], 2, [3, 4, 5, 6, 1, 2]),         # Basic rotation
    ([1, 2, 3], 0, [1, 2, 3]),                           # No rotation
    ([1, 2, 3], 3, [1, 2, 3]),                           # Full rotation
    ([1, 2, 3], 6, [1, 2, 3]),                           # d % n == 0
    ([1, 2, 3], 7, [2, 3, 1]),                           # d > len(arr)
    ([], 1, []),                                         # Empty
    ([10], 1, [10]),                                     # Single element
    ([1, 2], 1, [2, 1]),                                 # Small array
    ([5, 5, 5, 5], 2, [5, 5, 5, 5]),                     # All same values
    (list(range(1, 6)), 5, [1, 2, 3, 4, 5]),             # Full cycle
    (list(range(1, 6)), 6, [2, 3, 4, 5, 1]),             # d > len
    (list(range(10000)), 1, list(range(1, 10000)) + [0]) # Large input
])
def test_array_rotate(arr, d, expected):
    assert array_rotate_1(arr, d) == expected
    assert array_rotate_2(arr, d) == expected
    assert array_rotate_3(arr, d) == expected
