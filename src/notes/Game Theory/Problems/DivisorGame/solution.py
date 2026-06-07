class Solution:
    def divisorGame(self, n: int) -> bool:
        # If 'n' is even, Alice can always pick 'x = 1', leaving Bob with an odd number.
        # Bob is then forced to pick an odd divisor, leaving Alice with an even number.
        # This cycle continues until Bob is forced to face 'n = 1' and loses.
        # Therefore, Alice wins if and only if 'n' is initially even.
        return n % 2 == 0

# --- Example Usage ---
# sol = Solution()
# print(sol.divisorGame(2)) # Output: True
# print(sol.divisorGame(3)) # Output: False
