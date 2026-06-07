from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # Hash map to store {prefix_sum : count}
        # Initialize with 0: 1 to handle subarrays that start from index 0
        prefix_sums = {0: 1}
        
        current_sum = 0
        result = 0
        
        for num in nums:
            current_sum += num
            
            # The target prefix sum we are looking for in the history
            diff = current_sum - k
            
            # If we've seen this prefix sum before, it means the elements
            # between that point and our current point sum up to 'k'
            result += prefix_sums.get(diff, 0)
            
            # Add the current prefix sum to our map for future elements to use
            prefix_sums[current_sum] = prefix_sums.get(current_sum, 0) + 1
            
        return result

# --- Example Usage ---
# sol = Solution()
# print(sol.subarraySum([1, 1, 1], 2)) # Output: 2
# print(sol.subarraySum([1, 2, 3], 3)) # Output: 2
# print(sol.subarraySum([1, -1, 1, 1, 1, 1], 3)) # Output: 4
