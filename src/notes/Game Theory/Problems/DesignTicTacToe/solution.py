class TicTacToe:

    def __init__(self, n: int):
        self.n = n
        self.rows = [0] * n
        self.cols = [0] * n
        self.diagonal = 0
        self.anti_diagonal = 0

    def move(self, row: int, col: int, player: int) -> int:
        # Player 1 adds 1. Player 2 subtracts 1.
        val = 1 if player == 1 else -1
        
        # Update row and column
        self.rows[row] += val
        self.cols[col] += val
        
        # Update main diagonal (top-left to bottom-right)
        if row == col:
            self.diagonal += val
            
        # Update anti-diagonal (top-right to bottom-left)
        if col == (self.n - row - 1):
            self.anti_diagonal += val
            
        # Check for a winner
        # If absolute value reaches 'n', someone won
        if (abs(self.rows[row]) == self.n or 
            abs(self.cols[col]) == self.n or 
            abs(self.diagonal) == self.n or 
            abs(self.anti_diagonal) == self.n):
            return player
            
        return 0

# --- Example Usage ---
# obj = TicTacToe(3)
# print(obj.move(0, 0, 1)) # Output: 0
# print(obj.move(0, 2, 2)) # Output: 0
# print(obj.move(2, 2, 1)) # Output: 0
# print(obj.move(1, 1, 2)) # Output: 0
# print(obj.move(2, 0, 1)) # Output: 0
# print(obj.move(1, 0, 2)) # Output: 0
# print(obj.move(2, 1, 1)) # Output: 1 (Player 1 wins on bottom row)
