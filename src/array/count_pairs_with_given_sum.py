from typing import List


# Dictionary - Time Complexity = O(n), Space Complexity = O(n)
def count_pairs(arr: List[int], target: int) -> int:
    if sum(arr) < target:
        return 0
    
    occurencies = {}
    count = 0

    for num in arr:
        if (target - num) in occurencies:
            count += occurencies[target - num] 
        
        occurencies[num] = occurencies.get(num, 0) + 1 

    return count
