import pytest
from src.array.convert_array_into_zig_zag_fashion import convert

@pytest.mark.parametrize("n, arr, expected", [
    (7, [4, 3, 7, 8, 6, 2, 1], [3, 7, 4, 8, 2, 6, 1]), # Many swaps
    (4, [1, 4, 3, 2], [1, 4, 2, 3]),                   # One swap
    (5, [1, 3, 2, 4, 3], [1, 3, 2, 4, 3]),             # Already zig-zag
    (5, [1, 2, 3, 4, 5], [1, 3, 2, 5, 4]),             # Sorted Asc
    (5, [5, 4, 3, 2, 1], [4, 5, 2, 3, 1]),             # Sorted Desc
    (2, [1, 2], [1, 2]),                               # Small Array
    (0, [], []),                                       # Empty Array
    (1, [5], [5])                                      # Single Element
])
def test_convert(n, arr, expected):
    assert convert(n, arr) == expected
    