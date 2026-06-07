from typing import List

class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        # Memoization cache
        # memo[left][right] stores the max score difference the current player
        # can get from the subarray nums[left:right+1]
        memo = {}
        
        def max_diff(left, right):
            # Base case: only one element left
            if left == right:
                return nums[left]
            
            if (left, right) in memo:
                return memo[(left, right)]
            
            # The current player can either pick the left end or the right end.
            # If they pick left, they gain nums[left], but lose whatever score difference
            # the OPPONENT can achieve from the remaining array (hence the subtraction).
            pick_left = nums[left] - max_diff(left + 1, right)
            pick_right = nums[right] - max_diff(left, right - 1)
            
            # Current player wants to maximize their net difference
            memo[(left, right)] = max(pick_left, pick_right)
            return memo[(left, right)]
        
        # If the max difference Player 1 can achieve over the whole array is >= 0, they win or tie.
        return max_diff(0, len(nums) - 1) >= 0

# --- Example Usage ---
# sol = Solution()
# print(sol.predictTheWinner([1, 5, 2]))       # Output: False
# print(sol.predictTheWinner([1, 5, 233, 7]))  # Output: True
