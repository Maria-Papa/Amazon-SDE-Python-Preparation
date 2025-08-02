from typing import List


# Slicing
# Time: O(n), Space: O(n)
def array_rotate_1(arr: List[int], d: int) -> List[int]:
    length = len(arr)
    
    if length == 0:
        return arr

    if d > length:
        d = d % length

    return [*arr[d:], *arr[:d]]

# Reversal Using Extra Arrays
# Time: O(n), Space: O(n)
def array_rotate_2(arr: List[int], d: int) -> List[int]:
    length = len(arr)
    
    if length == 0:
        return arr
    
    d %= length

    arr = arr[:d][::-1] + arr[d:][::-1]
    arr.reverse()

    return arr

# Temporary Array
# Time: O(n), Space: O(n)
def array_rotate_3(arr: List[int], d: int) -> List[int]:
    length = len(arr)

    if length == 0:
        return arr
    
    temp = []

    d %= length

    for i in range(d, length):
        temp.append(arr[i])

    for i in range(0, d):
        temp.append(arr[i])

    return temp

# In-place Reversal Algorithm
# Time: O(n), Space: O(1)
def array_rotate_4(arr: List[int], d: int) -> List[int]:
    def reverse(a, start, end):
        while start < end:
            a[start], a[end] = a[end], a[start]
            start += 1
            end -= 1

    length = len(arr)
    
    if length == 0:
        return arr
    
    d %= length

    reverse(arr, 0, d - 1)
    reverse(arr, d, length - 1)
    reverse(arr, 0, length - 1)

    return arr
