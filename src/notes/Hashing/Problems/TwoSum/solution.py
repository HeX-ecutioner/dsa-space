from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Hash Map to store value -> index
        # This acts as our "memory" of numbers we have already seen.
        seen = {}
        
        for i, num in enumerate(nums):
            # The number we need to find to reach the target
            complement = target - num
            
            # Check if the complement is already in our hash map
            if complement in seen:
                # If found, return the index of the complement and our current index
                return [seen[complement], i]
            
            # Otherwise, store the current number and its index in the map
            seen[num] = i
            
        # The problem guarantees exactly one solution, 
        # so we will never practically reach here.
        return []

# --- Example Usage ---
# sol = Solution()
# print(sol.twoSum([2, 7, 11, 15], 9)) # Output: [0, 1]
# print(sol.twoSum([3, 2, 4], 6))      # Output: [1, 2]
