from typing import List


# 2 Pointers
# Time: O(n), Space: O(1)
def max_water(arr: List[int]) -> int:
    arr_length = len(arr)

    if not arr or arr_length < 3:
        return 0

    left = 1
    right = arr_length - 2

    max_left = arr[left - 1]
    max_right = arr[right + 1]
    total_water = 0

    while left <= right:
        if max_right <= max_left:
            total_water += max(0, max_right - arr[right])
            max_right = max(max_right, arr[right])
            right -= 1
        else:
            total_water += max(0, max_left - arr[left])
            max_left = max(max_left, arr[left])
            left += 1

    return total_water
