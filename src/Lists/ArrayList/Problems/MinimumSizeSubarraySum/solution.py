"""
Problem: Minimum Size Subarray Sum
Statement: Given an array of positive integers nums and a positive integer target, return the minimal length of a contiguous subarray whose sum is greater than or equal to target. If there is no such subarray, return 0.
"""

def minSubArrayLen(target, nums):
    # Time Complexity: O(n) - Each element is added and removed at most once.
    # Space Complexity: O(1) - Only pointers are used.
    
    left = 0
    current_sum = 0
    min_length = float('inf')
    
    for right in range(len(nums)):
        current_sum += nums[right] # Expand the window by adding the right element
        
        # Shrink the window from the left as long as the condition is met
        while current_sum >= target:
            min_length = min(min_length, right - left + 1)
            current_sum -= nums[left]
            left += 1
            
    return min_length if min_length != float('inf') else 0

if __name__ == "__main__":
    nums = [2, 3, 1, 2, 4, 3]
    target = 7
    print("Min Subarray Length:", minSubArrayLen(target, nums)) # Expected: 2 (subarray [4, 3])