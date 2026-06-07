# Design Tic-Tac-Toe

**Difficulty:** Medium

Assume the following rules are for the tic-tac-toe game on an `n x n` board between two players:
1. A move is guaranteed to be valid and is placed on an empty block.
2. Once a winning condition is reached, no more moves are allowed.
3. A player who succeeds in placing `n` of their marks in a horizontal, vertical, or diagonal row wins the game.

Implement the `TicTacToe` class:
- `TicTacToe(int n)` Initializes the object the size of the board `n`.
- `int move(int row, int col, int player)` Indicates that the player with id `player` plays at the cell `(row, col)` of the board. The move is guaranteed to be a valid move, and the two players alternate turns. Return `0` if there is no winner after the move, `1` if player 1 wins, or `2` if player 2 wins.

## Approach: State Arrays ($O(1)$ Optimization)
A naive approach would be to store the `n x n` board and scan the entire row, column, and both diagonals every time a move is made. That would be $O(N)$ time per move.

We can achieve **$O(1)$ time per move** by realizing we don't actually need the board at all. We only need to know *how many* marks a player has in each row, column, and diagonal.

1.  **Arrays:** Maintain an array for rows (`rows`) of size `n` and columns (`cols`) of size `n`.
2.  **Diagonals:** Maintain two integer variables, one for the main diagonal (`diagonal`) and one for the anti-diagonal (`anti_diagonal`).
3.  **Scoring Strategy:** 
    - If Player 1 plays, we **add 1** to the corresponding row, col, and diagonals.
    - If Player 2 plays, we **subtract 1** from the corresponding row, col, and diagonals.
4.  **Winning Condition:** If any row, column, or diagonal reaches exactly `n` (Player 1 win) or `-n` (Player 2 win), we have a winner!

By mathematically tracking the sum of rows/cols/diagonals instead of the symbols themselves, we bypass the need to iterate through the board.

## Complexity
- **Time Complexity:** $O(1)$ per `move()` operation.
- **Space Complexity:** $O(N)$ to store the `rows` and `cols` arrays.
