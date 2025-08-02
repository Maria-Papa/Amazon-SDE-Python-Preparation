import pytest
from src.array.search_in_a_row_wise_and_column_wise_sorted_matrix import search_in_sorted_matrix

@pytest.mark.parametrize("x, mat, expected", [
    (62, [[3, 30, 38], [20, 52, 54], [35, 60, 69]], False), # Not found
    (55, [[18, 21, 27], [38, 55, 67]], True),               # Found
    (35, [[3, 30, 38], [20, 52, 54], [35, 60, 69]], True),  # Bottom-left
    (69, [[3, 30, 38], [20, 52, 54], [35, 60, 69]], True),  # Bottom-right
    (3, [[3, 30, 38], [20, 52, 54], [35, 60, 69]], True),   # Top-left
    (38, [[3, 30, 38], [20, 52, 54], [35, 60, 69]], True),  # Top-right
    (100, [[1, 2, 3], [4, 5, 6], [7, 8, 9]], False),        # Out of bounds high
    (-1, [[1, 2, 3], [4, 5, 6], [7, 8, 9]], False),         # Out of bounds low
    (5, [], False),                                         # Empty matrix
    (5, [[]], False),                                       # Matrix with empty row
    (5, [[5]], True),                                       # Single element match
    (2, [[5]], False),                                      # Single element mismatch
])
def test_search_in_sorted_matrix(x, mat, expected):
    assert search_in_sorted_matrix(x, mat) == expected
