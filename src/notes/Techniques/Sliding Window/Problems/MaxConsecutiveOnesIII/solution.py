# Problem: Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.
from typing import List

def longest_ones(nums: List[int], k: int) -> int:
    """
    Approach: Variable-size Sliding Window.
    We maintain a window [left, right] that contains at most `k` zeroes.
    We expand the window by moving `right`. If we encounter a '0', we decrement `k`.
    If `k` becomes negative (we have more than `k` zeroes in our window), we must 
    shrink the window from the `left` until we discard a '0', thereby incrementing `k` back.
    The size of the maximum valid window is our answer.
    
    Time: O(n) - Both pointers left and right move forward at most n times.
    Space: O(1) - Constant extra space used.
    """
    left = 0
    max_len = 0
    
    for right in range(len(nums)):
        # If we see a 0, we "use" one of our flips
        if nums[right] == 0:
            k -= 1
            
        # If we used more flips than allowed, shrink the window from the left
        while k < 0:
            if nums[left] == 0:
                # We are discarding a 0 from our window, so we get a flip back
                k += 1
            left += 1
            
        # Record the maximum length of a valid window found so far
        max_len = max(max_len, right - left + 1)
        
    return max_len

# Example usage:
print(longest_ones([1,1,1,0,0,0,1,1,1,1,0], 2)) # Output: 6
print(longest_ones([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3)) # Output: 10
