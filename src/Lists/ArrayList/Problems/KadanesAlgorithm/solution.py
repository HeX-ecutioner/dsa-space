"""
Problem: Maximum Subarray (Kadane's Algorithm)
Statement: Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
"""

def maxSubArray(nums):
    # Time Complexity: O(n) - Single pass through the array.
    # Space Complexity: O(1) - Only using two variables.
    
    current_sum = nums[0]
    max_sum = nums[0]
    
    for i in range(1, len(nums)):
        # Decide whether to add the current number to the existing subarray, 
        # or start a new subarray beginning with the current number.
        current_sum = max(nums[i], current_sum + nums[i])
        
        # Update the maximum sum encountered so far
        max_sum = max(max_sum, current_sum)
        
    return max_sum

if __name__ == "__main__":
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    result = maxSubArray(nums)
    print("Maximum Subarray Sum:", result) # Expected: 6 (from [4, -1, 2, 1])