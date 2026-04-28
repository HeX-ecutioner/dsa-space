# Problem: The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other. Return all distinct solutions to the n-queens puzzle.
def solveNQueens(n):
    """
    Approach: Branch and Bound. We maintain bounds for columns, left diagonals, and right diagonals.
    Time: O(N!)
    Space: O(N)
    """
    cols = [False] * n
    diag1 = [False] * (2 * n - 1)
    diag2 = [False] * (2 * n - 1)
    res = []
    board = [["."] * n for _ in range(n)]

    def backtrack(r):
        if r == n:
            res.append(["".join(row) for row in board])
            return
        for c in range(n):
            if cols[c] or diag1[r + c] or diag2[r - c + n - 1]:
                continue
            cols[c] = diag1[r + c] = diag2[r - c + n - 1] = True
            board[r][c] = "Q"
            backtrack(r + 1)
            cols[c] = diag1[r + c] = diag2[r - c + n - 1] = False
            board[r][c] = "."
            
    backtrack(0)
    return res
