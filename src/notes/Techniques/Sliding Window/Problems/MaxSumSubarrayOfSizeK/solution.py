# Problem: Given an array of integers and a number k, find the maximum sum of a contiguous subarray of size k.
from typing import List

def max_sum_subarray(arr: List[int], k: int) -> int:
    """
    Approach: Fixed-size Sliding Window.
    Instead of calculating the sum of every k elements from scratch (O(n*k)),
    we compute the sum of the first window of size k. Then, for each subsequent
    element, we add the new element to the sum and subtract the element that
    leaves the window from the left.
    
    Time: O(n) - We traverse the array exactly once.
    Space: O(1) - Only storing a few integer variables.
    """
    if not arr or k <= 0 or k > len(arr):
        return 0
        
    # Step 1: Calculate the sum of the very first window of size k.
    window_sum = sum(arr[:k])
    max_sum = window_sum
    
    # Step 2: Slide the window from the k-th element to the end of the array.
    for i in range(k, len(arr)):
        # Add the next element in the array (entering the window)
        # and subtract the element that is left behind (exiting the window).
        window_sum += arr[i] - arr[i - k]
        
        # Update the maximum sum found so far.
        max_sum = max(max_sum, window_sum)
        
    return max_sum

# Example usage:
# The window sizes are fixed at k=3
print(max_sum_subarray([2, 1, 5, 1, 3, 2], 3)) # Output: 9 (Subarray: [5, 1, 3])
print(max_sum_subarray([2, 3, 4, 1, 5], 2))    # Output: 7 (Subarray: [3, 4])
