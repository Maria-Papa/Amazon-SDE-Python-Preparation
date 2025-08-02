from typing import List


# Hashmap - Time Complexity = Space Complexity = O(n)
def find_duplicates_1(n: int, arr: List[int]) -> List[int]:
    duplicates = {}
    result = []

    for num in arr:
        duplicates[num] = duplicates.get(num, 0) + 1

    for key, value in duplicates.items():
        if value > 1:
            result.append(key)

    return result

# Set - Time Complexity = Space Complexity = O(n)
def find_duplicates_2(n: int, arr: List[int]) -> List[int]:
    duplicates = set()
    result = set()

    for num in arr:
        if num in duplicates:
            result.add(num)
        else:
            duplicates.add(num)

    return sorted(list(result))

# Auxilary Array - Time Complexity = Space Complexity = O(n)
def find_duplicates_3(n: int, arr: List[int]) -> List[int]:
    duplicates = [0] * n
    result = []

    for num in arr:
        duplicates[num] += 1

    print(duplicates)

    for i in range(n):
        if duplicates[i] > 1:
            result.append(i)

    return result
