from typing import List


# Eliminating rows or columns
# Time: O(n + m), Space: O(1)
def search_in_sorted_matrix(x: int, mat: List[List[int]]) -> bool:
    n = len(mat)

    if n < 1:
        return False

    rows, cols = n, len(mat[0])
    row, col = 0, cols - 1

    while row < rows and col >= 0:
        if mat[row][col] == x:
            return True
        elif mat[row][col] < x:
            row += 1
        else:
            col -= 1

    return False
