import pytest
from src.array.print_a_given_matrix_in_spiral_form import spiral_order_traversal


@pytest.mark.parametrize("mat, expected", [
    # Regular square matrix
    (
        [[1,   2,  3,  4],
         [5,   6,  7,  8],
         [9,  10, 11, 12],
         [13, 14, 15, 16]],
        [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10]
    ),
    # Rectangular matrix (more columns than rows)
    (
        [[1,   2,  3,  4,  5,  6],
         [7,   8,  9, 10, 11, 12],
         [13, 14, 15, 16, 17, 18]],
        [1, 2, 3, 4, 5, 6, 12, 18, 17, 16, 15, 14, 13, 7, 8, 9, 10, 11]
    ),
    # Rectangular matrix (more rows than columns)
    (
        [[1, 2],
         [3, 4],
         [5, 6],
         [7, 8]],
        [1, 2, 4, 6, 8, 7, 5, 3]
    ),
    # Single element
    (
        [[1]],
        [1]
    ),
    # Single row
    (
        [[1, 2, 3, 4]],
        [1, 2, 3, 4]
    ),
    # Single column
    (
        [[1], [2], [3], [4]],
        [1, 2, 3, 4]
    ),
    # Empty matrix
    (
        [],
        []
    ),
    # Matrix with one empty row
    (
        [[]],
        []
    ),
])
def test_spiral_order_traversal(mat, expected):
    assert spiral_order_traversal(mat) == expected
