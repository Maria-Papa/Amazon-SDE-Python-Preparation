from typing import List


# Kadane's Algorithm
# Time: O(n), Space: O(1)
def max_subarray_sum(arr: List[int]) -> int:
    n = len(arr)

    if n < 1:
        raise ValueError("Invalid input: array must have at least one element")

    max_ending = max_sum = arr[0]

    for i in range(1, n):
        max_ending = max(max_ending + arr[i], arr[i])
        max_sum = max(max_sum, max_ending)

    return max_sum
