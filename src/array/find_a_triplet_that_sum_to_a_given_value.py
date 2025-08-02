from typing import List


# Sorting and Pointers
# Time: O(n^2), Space: O(1)
def find_triplet_sum(arr: List[int], target: int) -> bool:
    n = len(arr)
    arr.sort()

    for i in range(n - 2):
        left_index = i + 1
        right_index = n - 1
        target_remaining = target - arr[i]

        while left_index < right_index:
            if arr[left_index] + arr[right_index] == target_remaining:
                return True
            
            if arr[left_index] + arr[right_index] < target_remaining:
                left_index += 1
            else:
                right_index -= 1

    return False
