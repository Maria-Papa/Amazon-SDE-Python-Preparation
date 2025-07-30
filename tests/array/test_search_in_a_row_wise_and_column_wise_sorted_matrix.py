import pytest
from src.array.search_in_a_row_wise_and_column_wise_sorted_matrix import is_integer_present

@pytest.mark.parametrize("x, mat, expected", [
    (62, [[3, 30, 38], [20, 52, 54], [35, 60, 69]], False),
    (55, [[18, 21, 27], [38, 55, 67]], True),
    (35, [[3, 30, 38], [20, 52, 54], [35, 60, 69]], True)
])
def test_is_integer_present(x, mat, expected):
    assert is_integer_present(x, mat) == expected
