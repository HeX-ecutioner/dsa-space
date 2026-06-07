from typing import List

class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        memo = {}
        
        # Returns the max score difference the current player can achieve starting from index i
        def dp(i):
            if i >= len(stoneValue):
                return 0
                
            if i in memo:
                return memo[i]
                
            max_diff = float('-inf')
            current_sum = 0
            
            # The player can take 1, 2, or 3 stones
            for x in range(1, 4):
                if i + x - 1 < len(stoneValue):
                    # Add the value of the stone we just took
                    current_sum += stoneValue[i + x - 1]
                    
                    # Score difference = (what we gained) - (max difference opponent can get from remaining)
                    diff = current_sum - dp(i + x)
                    max_diff = max(max_diff, diff)
                    
            memo[i] = max_diff
            return max_diff
            
        alice_diff = dp(0)
        
        if alice_diff > 0:
            return "Alice"
        elif alice_diff < 0:
            return "Bob"
        else:
            return "Tie"

# --- Example Usage ---
# sol = Solution()
# print(sol.stoneGameIII([1,2,3,7])) # Output: "Bob"
# print(sol.stoneGameIII([1,2,3,-9])) # Output: "Alice"
