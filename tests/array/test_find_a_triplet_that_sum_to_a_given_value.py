import pytest
from src.array.find_a_triplet_that_sum_to_a_given_value import find_triplet_sum


@pytest.mark.parametrize('arr, target, expected', [
    ([1, 4, 45, 6, 10, 8], 13, True),   # One matching triplet
    ([1, 2, 4, 3, 6, 7], 10, True),     # Multiple matching triplets
    ([40, 20, 10, 3, 6, 7], 24, False), # No triplets
    ([2, 3, 5], 10, True),              # One matching triplet in an array of 3 elements
    ([1, 2, 3], 10, False),             # No matching triplet in an array of 3 elements
    ([1, 2], 3, False),                 # Less than 3 elements, can't form a triplet
    ([], 0, False),                     # Empty array
    ([0, -1, 2, -3, 1], 0, True),       # Negative numbers included
    ([-5, -3, -2, -1], -10, True),      # All negative numbers
    ([0, 0, 0, 0], 0, True)             # All zeros
])
def test_find_duplicates(arr, target, expected):
    assert(find_triplet_sum(arr, target)) == expected
