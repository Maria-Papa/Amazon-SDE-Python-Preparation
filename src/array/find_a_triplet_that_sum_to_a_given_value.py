from typing import List


# Sorting and Pointers - Time Complexity = O(n^2), Space Complexity = O(1)
def find_triplet_sum(arr: List[int], target: int) -> bool:
    n = len(arr)
    arr.sort()

    for i in range(n - 2):
        left_index = i + 1
        right_index = n - 1
        sum = target - arr[i]

        print(arr)

        print(f"l = {left_index}, r = {right_index}, sum = {sum}")

        while left_index < right_index:
            if arr[left_index] + arr[right_index] == sum:
                return True
            
            if arr[left_index] + arr[right_index] < sum:
                left_index += 1
            else:
                right_index -= 1

    return False
