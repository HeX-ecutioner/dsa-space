from typing import List

class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        # Suffix sums to quickly calculate the remaining stones from an index to the end
        # suffix_sum[i] = sum(piles[i:])
        suffix_sum = [0] * len(piles)
        suffix_sum[-1] = piles[-1]
        for i in range(len(piles) - 2, -1, -1):
            suffix_sum[i] = suffix_sum[i+1] + piles[i]
            
        memo = {}
        
        # Returns the max stones the CURRENT player can get starting from 'idx' with 'M'
        def dp(idx, M):
            # Base case: no more piles
            if idx >= len(piles):
                return 0
                
            # If we can take all remaining piles, do it
            if idx + 2 * M >= len(piles):
                return suffix_sum[idx]
                
            if (idx, M) in memo:
                return memo[(idx, M)]
                
            max_stones = 0
            
            # The current player can take X piles, where 1 <= X <= 2M
            for X in range(1, 2 * M + 1):
                # The total stones available from idx to the end is suffix_sum[idx]
                # The opponent will play optimally from the next state and get dp(idx + X, max(M, X))
                # So we get whatever is left over from the total remaining stones
                stones_we_get = suffix_sum[idx] - dp(idx + X, max(M, X))
                max_stones = max(max_stones, stones_we_get)
                
            memo[(idx, M)] = max_stones
            return max_stones
            
        return dp(0, 1)

# --- Example Usage ---
# sol = Solution()
# print(sol.stoneGameII([2,7,9,4,4])) # Output: 10
