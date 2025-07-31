import pytest
from src.array.trapping_rain_water import max_water

@pytest.mark.parametrize("arr, expected", [
    ([2, 1, 5, 3, 1, 0, 4], 9),  # Trap at valleys
    ([3, 0, 1, 0, 4, 0, 2], 10), # Trap between peaks
    ([3, 0, 2, 0, 4], 7),        # Multiple traps
    ([[1, 2, 3, 4]], 0),         # Ascending bars, no trap
    ([], 0),                     # Empty array, no trap
    ([6], 0),                    # Single bar, no trap
    ([1, 2], 0),                 # Two bars, no trap
    ([1, 0, 2], 1)               # Least amount of bars to trap
])
def test_max_water(arr, expected):
    assert max_water(arr) == expected
