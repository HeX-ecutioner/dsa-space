from typing import List

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        # Map to store {prefix_sum_count: first_index_seen}
        # Initialize with {0: -1} for subarrays that start at index 0
        count_map = {0: -1}
        
        max_length = 0
        count = 0
        
        for i in range(len(nums)):
            # Treat 0 as -1, and 1 as 1
            if nums[i] == 1:
                count += 1
            else:
                count -= 1
                
            # If we've seen this count before, the subarray between
            # that index and current index has a sum of 0
            if count in count_map:
                # Calculate length: current_index - first_seen_index
                length = i - count_map[count]
                max_length = max(max_length, length)
            else:
                # Only store the FIRST time we see a count
                # to maximize the length of the subarray later
                count_map[count] = i
                
        return max_length

# --- Example Usage ---
# sol = Solution()
# print(sol.findMaxLength([0, 1]))       # Output: 2
# print(sol.findMaxLength([0, 1, 0]))    # Output: 2
# print(sol.findMaxLength([0, 0, 1, 0, 0, 0, 1, 1])) # Output: 6
