#!/usr/bin/python3
"""
N queens
"""
import sys

def is_safe(board, row, col, n):
    """
    Check if it's safe to place a queen in board[row][col]
    """
    # Check this row on the left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, n), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_nqueens_util(board, col, n, result):
    """
    Solve N queens problem recursively
    """
    if col >= n:
        result.append([[i, row] for i, row in enumerate(board)])
        return True

    res = False
    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 1
            res = solve_nqueens_util(board, col + 1, n, result) or res
            board[i][col] = 0  # Backtrack if placing queen at board[i][col] doesn't lead to a solution

    return res

def solve_nqueens(n):
    """
    Solve N queens problem
    """
    if not isinstance(n, int):
        print("N must be a number")
        return 1
    if n < 4:
        print("N must be at least 4")
        return 1

    board = [[0 for _ in range(n)] for _ in range(n)]
    result = []
    solve_nqueens_util(board, 0, n, result)

    for sol in result:
        print(sol)

    return 0

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    sys.exit(solve_nqueens(n))
