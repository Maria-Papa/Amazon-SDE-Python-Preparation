from typing import List


# Flag - Time Complexity = O(n), Space Complexity = O(1)
def convert(n: int, arr: List[int]) -> List[int]:
    flag = True

    for i in range(n - 1):
        if flag is True:
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
        else:
            if arr[i] < arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
        flag = not flag

    return arr
