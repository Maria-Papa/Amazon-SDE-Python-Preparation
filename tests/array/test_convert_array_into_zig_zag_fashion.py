import pytest
from src.array.convert_array_into_zig_zag_fashion import convert_to_zig_zag


@pytest.mark.parametrize("n, arr, expected", [
    (7, [4, 3, 7, 8, 6, 2, 1], [3, 7, 4, 8, 2, 6, 1]), # Many swaps needed
    (4, [1, 4, 3, 2], [1, 4, 2, 3]),                   # One swap needed
    (5, [1, 3, 2, 4, 3], [1, 3, 2, 4, 3]),             # Already in zig-zag
    (5, [1, 2, 3, 4, 5], [1, 3, 2, 5, 4]),             # Strictly increasing
    (5, [5, 4, 3, 2, 1], [4, 5, 2, 3, 1]),             # Strictly decreasing
    (2, [1, 2], [1, 2]),                               # Minimum zig-zag length
    (0, [], []),                                       # Empty array
    (1, [5], [5])                                      # Single element
])
def test_convert_to_zig_zag(n, arr, expected):
    assert convert_to_zig_zag(n, arr) == expected
