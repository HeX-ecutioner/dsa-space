"""
Problem: Max Consecutive Ones III (Sliding Window Pattern)
Statement: Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.
"""

def longestOnes(nums, k):
    # Time Complexity: O(n) - The right pointer and left pointer both traverse the array at most once.
    # Space Complexity: O(1) - Only a few integer variables are used.
    
    left = 0
    max_length = 0
    zero_count = 0
    
    for right in range(len(nums)):
        if nums[right] == 0:
            zero_count += 1
            
        # If we have flipped too many zeros, shrink the window from the left
        while zero_count > k:
            if nums[left] == 0:
                zero_count -= 1
            left += 1
            
        # The window is valid, calculate its length
        current_length = right - left + 1
        max_length = max(max_length, current_length)
        
    return max_length

if __name__ == "__main__":
    nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
    k = 2
    print("Max Consecutive Ones (max 2 flips):", longestOnes(nums, k)) # Expected: 6