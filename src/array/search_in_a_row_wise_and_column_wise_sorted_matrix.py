from typing import List


def is_integer_present(x: int, mat: List[List[int]]) -> bool:
    print(f"x = {x}, mat = {mat}")

    rows, cols = len(mat), len(mat[0])
    row, col = 0, cols - 1

    while row < rows and col >= 0:
        if mat[row][col] == x:
            return True
        elif mat[row][col] < x:
            row += 1
        else:
            col -= 1

    return False
