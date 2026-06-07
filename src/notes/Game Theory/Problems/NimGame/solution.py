class Solution:
    def canWinNim(self, n: int) -> bool:
        # If the number of stones is a multiple of 4, the first player will always lose 
        # (assuming optimal play from the second player).
        # In any other case, the first player can take n % 4 stones,
        # leaving the second player with a multiple of 4, guaranteeing a win.
        return n % 4 != 0

# --- Example Usage ---
# sol = Solution()
# print(sol.canWinNim(4)) # Output: False
# print(sol.canWinNim(1)) # Output: True
# print(sol.canWinNim(7)) # Output: True
