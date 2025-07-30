import pytest
from src.array.print_a_given_matrix_in_spiral_form import print_matrix_in_spiral

@pytest.mark.parametrize("mat, expected", [
    (
        [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 16]
        ],
        [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10]
    ),
    (
        [
            [1, 2, 3, 4,  5, 6],
            [7, 8, 9, 10, 11, 12],
            [13, 14, 15, 16, 17, 18]
        ],
        [1, 2, 3, 4, 5, 6, 12, 18, 17, 16, 15, 14, 13, 7, 8, 9, 10, 11]
    )
])
def test_print_matrix_in_spiral(mat, expected):
    assert print_matrix_in_spiral(mat) == expected
    