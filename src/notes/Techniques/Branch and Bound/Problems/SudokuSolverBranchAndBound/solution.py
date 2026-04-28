# Problem: Write a program to solve a Sudoku puzzle by filling the empty cells.
def solveSudoku(board):
    """
    Approach: Branch and Bound (Forward checking/Backtracking).
    Time: O(9^(empty_cells))
    Space: O(81)
    """
    def isValid(r, c, k):
        for i in range(9):
            if board[i][c] == k or board[r][i] == k or board[3*(r//3)+i//3][3*(c//3)+i%3] == k:
                return False
        return True

    def backtrack():
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    for k in map(str, range(1, 10)):
                        if isValid(r, c, k):
                            board[r][c] = k
                            if backtrack(): return True
                            board[r][c] = "."
                    return False
        return True

    backtrack()
