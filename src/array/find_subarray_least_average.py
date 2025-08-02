from typing import List, Tuple


# Sliding Window
# Time: O(n), Space: O(1)
def find_subarray_least_avg(arr: List[int], k: int) -> Tuple[int, int]:
    arr_length = len(arr)

    if arr_length < k or k == 0:
        raise ValueError("Invalid input: k must be <= len(arr) and > 0")

    start_index = 0
    min_sum = current_sum = sum(arr[:k])

    for i in range(k, arr_length):
        current_sum += arr[i] - arr[i - k]

        if current_sum < min_sum:
            min_sum = current_sum
            start_index = i - k + 1

    return (start_index, start_index + k - 1)
