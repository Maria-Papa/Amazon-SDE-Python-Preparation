import pytest
from src.array.find_duplicates_in_on_time_and_constant_extra_space import find_duplicates_1, find_duplicates_2, find_duplicates_3

@pytest.mark.parametrize('n, arr, expected', [
    (7, [1, 2, 3, 6, 3, 6, 1], [1, 3, 6]), # Multiple duplicates
    (5, [1, 2, 3, 4, 3], [3]),             # One duplicate
    (0, [], []),                           # Empty array
    (4, [1, 1, 1, 1], [1]),                # Same number repeated
    (6, [0, 0, 1, 2, 3, 4], [0])           # 0 multiple times
])
def test_find_duplicates(n, arr, expected):
    assert(find_duplicates_1(n, arr)) == expected
    assert(find_duplicates_2(n, arr)) == expected
    assert(find_duplicates_3(n, arr)) == expected
