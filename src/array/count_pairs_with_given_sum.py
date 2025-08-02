from typing import List


# Dictionary
# Time: O(n), Space: O(n)
def count_pairs(arr: List[int], target: int) -> int:
    occurencies = {}
    count = 0

    for num in arr:
        if (target - num) in occurencies:
            count += occurencies[target - num] 
        
        occurencies[num] = occurencies.get(num, 0) + 1 

    return count
