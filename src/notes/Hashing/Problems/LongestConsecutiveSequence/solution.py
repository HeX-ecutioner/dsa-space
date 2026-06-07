from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Convert list to a set for O(1) lookups
        num_set = set(nums)
        longest = 0
        
        for num in num_set:
            # Check if 'num' is the start of a sequence
            # It's the start if 'num - 1' is NOT in the set
            if (num - 1) not in num_set:
                current_length = 1
                
                # Keep checking for consecutive numbers in the set
                while (num + current_length) in num_set:
                    current_length += 1
                    
                # Update the max length found so far
                longest = max(longest, current_length)
                
        return longest

# --- Example Usage ---
# sol = Solution()
# print(sol.longestConsecutive([100, 4, 200, 1, 3, 2])) # Output: 4
# print(sol.longestConsecutive([0,3,7,2,5,8,4,6,0,1]))  # Output: 9
