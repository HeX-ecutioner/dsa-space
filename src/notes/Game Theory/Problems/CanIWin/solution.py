class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        # If the desired total is 0 or less, the first player wins automatically
        if desiredTotal <= 0:
            return True
            
        # If the sum of all available numbers is less than the desired total, nobody can win
        sum_of_all = (maxChoosableInteger * (maxChoosableInteger + 1)) // 2
        if sum_of_all < desiredTotal:
            return False
            
        memo = {}

        def dfs(used_numbers_mask, current_total):
            # If this state has been computed before, return the cached result
            if used_numbers_mask in memo:
                return memo[used_numbers_mask]
                
            # Try picking every available number
            for i in range(1, maxChoosableInteger + 1):
                # Check if the i-th bit is 0 (meaning the number i is available)
                # We use (i - 1) for 0-indexed bit shifts
                if (used_numbers_mask & (1 << (i - 1))) == 0:
                    
                    # If picking this number reaches or exceeds the target, we win!
                    if current_total + i >= desiredTotal:
                        memo[used_numbers_mask] = True
                        return True
                        
                    # Otherwise, simulate picking this number and see if it forces the opponent to lose
                    new_mask = used_numbers_mask | (1 << (i - 1))
                    
                    # If the opponent cannot win from this new state, it means WE win
                    if not dfs(new_mask, current_total + i):
                        memo[used_numbers_mask] = True
                        return True
                        
            # If we try all available numbers and none force a win, we lose
            memo[used_numbers_mask] = False
            return False

        # Start with mask 0 (no numbers used) and total 0
        return dfs(0, 0)

# --- Example Usage ---
# sol = Solution()
# print(sol.canIWin(10, 11)) # Output: False
# print(sol.canIWin(10, 0))  # Output: True
# print(sol.canIWin(10, 1))  # Output: True
