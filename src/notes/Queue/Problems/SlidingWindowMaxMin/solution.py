"""
Sliding Window Maximum & Minimum (Monotonic Queue)

The Sliding Window Max/Min problem asks:
Given an array and a window size k,
find the MAXIMUM or MINIMUM element in every contiguous window of size k.

Why a QUEUE is mandatory:
- We need to REMOVE elements from the front (out of window)
- We need to MAINTAIN order of useful candidates
- A MONOTONIC DEQUE guarantees O(n) time

Brute force → O(n * k)
Heap → O(n log k)
Monotonic Deque → O(n) ✅ (optimal)
"""

from collections import deque


# Sliding Window Maximum
def sliding_window_max(nums, k):
    """
    Return a list of maximums for each sliding window of size k.

    Time Complexity: O(n)
    Space Complexity: O(k)
    """
    dq = deque()   # stores indices, values are in decreasing order
    result = []

    for i in range(len(nums)):
        # Remove indices that are OUT of the current window
        while dq and dq[0] <= i - k:
            dq.popleft()

        # Remove smaller elements (they are useless)
        while dq and nums[dq[-1]] <= nums[i]:
            dq.pop()

        dq.append(i)

        # Window becomes valid only after i >= k - 1
        if i >= k - 1:
            result.append(nums[dq[0]])

    return result

# Sliding Window Minimum
def sliding_window_min(nums, k):
    """
    Return a list of minimums for each sliding window of size k.

    Time Complexity: O(n)
    Space Complexity: O(k)
    """
    dq = deque()   # stores indices, values are in increasing order
    result = []

    for i in range(len(nums)):
        # Remove indices that are OUT of the current window
        while dq and dq[0] <= i - k:
            dq.popleft()

        # Remove larger elements (they are useless)
        while dq and nums[dq[-1]] >= nums[i]:
            dq.pop()

        dq.append(i)

        if i >= k - 1:
            result.append(nums[dq[0]])

    return result

# Example usage:
if __name__ == "__main__":
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    print("Sliding Window Maximum:", sliding_window_max(arr, k)) # Output: [3, 3, 5, 5, 6, 7]
    print("Sliding Window Minimum:", sliding_window_min(arr, k)) # Output: [-1, -3, -3, -3, 3, 3]