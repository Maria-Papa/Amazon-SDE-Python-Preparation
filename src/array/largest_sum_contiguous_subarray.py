from typing import List


def max_subarray_sum(input: List) -> int:
    print(f"Finding max subarray sum of: {input}")

    maxEnding = maxSum = input[0]

    for i in range (1, len(input)):
        maxEnding = max(maxEnding + input[i], input[i])
        maxSum = max(maxSum, maxEnding)

    return maxSum
