from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # A Hash Set to store unique numbers we have seen so far
        seen = set()
        
        for num in nums:
            # If the number is already in the set, we found a duplicate
            if num in seen:
                return True
            # Add the unique number to the set
            seen.add(num)
            
        # If we successfully iterate through the entire array, there are no duplicates
        return False

    # Alternative Pythonic 1-liner solution:
    # def containsDuplicateOneLiner(self, nums: List[int]) -> bool:
    #     # Creating a set automatically removes duplicates.
    #     # If the length shrinks, there was a duplicate.
    #     return len(set(nums)) != len(nums)

# --- Example Usage ---
# sol = Solution()
# print(sol.containsDuplicate([1,2,3,1])) # Output: True
# print(sol.containsDuplicate([1,2,3,4])) # Output: False
