import pytest
from src.array.trapping_rain_water import max_water


@pytest.mark.parametrize("arr, expected", [
    ([2, 1, 5, 3, 1, 0, 4], 9),  # Multiple valleys
    ([3, 0, 1, 0, 4, 0, 2], 10), # Traps in mid
    ([3, 0, 2, 0, 4], 7),        # Nested valleys
    ([1, 2, 3, 4], 0),           # Increasing - no trap
    ([], 0),                     # Empty
    ([6], 0),                    # Single bar
    ([1, 2], 0),                 # Two bars
    ([1, 0, 2], 1)               # Smallest trapping possible
])
def test_max_water(arr, expected):
    assert max_water(arr) == expected
