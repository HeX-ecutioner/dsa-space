from typing import List

class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        # Mathematical Trick:
        # Because the number of piles is even, Alice can always force a win 
        # by choosing either all even-indexed piles or all odd-indexed piles.
        # Since the total sum is odd, one of those sets of piles will have a greater sum.
        return True

    # Alternatively, the DP approach (identical to Predict the Winner):
    # def stoneGameDP(self, piles: List[int]) -> bool:
    #     memo = {}
    #     def max_diff(left, right):
    #         if left == right:
    #             return piles[left]
    #         if (left, right) in memo:
    #             return memo[(left, right)]
    #         
    #         pick_left = piles[left] - max_diff(left + 1, right)
    #         pick_right = piles[right] - max_diff(left, right - 1)
    #         
    #         memo[(left, right)] = max(pick_left, pick_right)
    #         return memo[(left, right)]
    #         
    #     return max_diff(0, len(piles) - 1) > 0

# --- Example Usage ---
# sol = Solution()
# print(sol.stoneGame([5, 3, 4, 5])) # Output: True
