"""
Problem: 3Sum
Statement: Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0. Notice that the solution set must not contain duplicate triplets.
"""

def threeSum(nums):
    # Time Complexity: O(n^2) - Sorting is O(n log n), nested loop is O(n^2).
    # Space Complexity: O(1) or O(n) depending on the sorting algorithm implementation.
    
    res = []
    nums.sort() # Sorting is crucial for the two-pointer approach to work
    
    for i, val in enumerate(nums):
        # Skip duplicate elements for the first position to avoid duplicate triplets
        if i > 0 and val == nums[i - 1]:
            continue
            
        left, right = i + 1, len(nums) - 1
        
        while left < right:
            three_sum = val + nums[left] + nums[right]
            
            if three_sum > 0:
                right -= 1 # Sum is too large, need a smaller number
            elif three_sum < 0:
                left += 1  # Sum is too small, need a larger number
            else:
                res.append([val, nums[left], nums[right]])
                left += 1
                # Skip duplicates for the second position
                while nums[left] == nums[left - 1] and left < right:
                    left += 1
                    
    return res

if __name__ == "__main__":
    nums = [-1, 0, 1, 2, -1, -4]
    print("3Sum Triplets:", threeSum(nums)) # Expected: [[-1, -1, 2], [-1, 0, 1]]