from typing import List


# Boundary Traversal
# Time: O(m*n), Space: O(1)
def spiral_order_traversal(mat: List[List[int]]) -> List[int]:
    if not mat or not mat[0]:
        return []
    
    result = []
    top, left, bottom, right = 0, 0, len(mat) - 1, len(mat[0]) - 1

    while top <= bottom and left <= right:

        # Left to Right
        for col in range(left, right + 1):
            result.append(mat[top][col])
        top += 1

        # Top to Bottom
        for row in range(top, bottom + 1):
            result.append(mat[row][right])
        right -= 1

        # Right to Left
        if top <= bottom:
            for col in range(right, left - 1, -1):
                result.append(mat[bottom][col])
            bottom -= 1

        # Bottom to Top
        if left <= right:
            for row in range(bottom, top - 1, - 1):
                result.append(mat[row][left])
            left += 1

    return result
