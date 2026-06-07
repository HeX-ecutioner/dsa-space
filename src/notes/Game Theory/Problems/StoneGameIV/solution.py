class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        # dp[i] will be True if the player whose turn it is facing 'i' stones will win.
        dp = [False] * (n + 1)
        
        # Base case: dp[0] = False is already set. If you face 0 stones, you lose.
        
        for i in range(1, n + 1):
            # Try removing every perfect square <= i
            k = 1
            while k * k <= i:
                # If we can reach a losing state for the opponent, 
                # then this current state 'i' is a winning state for us.
                if not dp[i - k * k]:
                    dp[i] = True
                    break
                k += 1
                
        return dp[n]

# --- Example Usage ---
# sol = Solution()
# print(sol.winnerSquareGame(4)) # Output: True
# print(sol.winnerSquareGame(7)) # Output: False
