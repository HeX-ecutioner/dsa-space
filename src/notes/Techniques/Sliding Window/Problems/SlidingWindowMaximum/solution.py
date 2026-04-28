# Problem: You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position. Return the max sliding window.
from collections import deque
from typing import List

def max_sliding_window(nums: List[int], k: int) -> List[int]:
    """
    Approach: Fixed-size Sliding Window with Monotonic Deque.
    We maintain a deque (double-ended queue) of INDICES.
    The deque will store indices of elements in descending order of their values.
    This means the index of the maximum element in the current window will always 
    be at the front of the deque (`deque[0]`).
    
    For each element at index `i`:
    1. Remove indices from the front of the deque if they are out of the current window `(i - k)`.
    2. Remove indices from the back of the deque if the current element `nums[i]` is 
       greater than or equal to the elements at those indices (because they can never 
       be the maximum in any window going forward).
    3. Add the current index `i` to the back.
    4. If our window has reached size `k` (i.e., `i >= k - 1`), append the element at 
       the front of the deque to our result.
       
    Time: O(n) - Every element is pushed and popped from the deque at most once.
    Space: O(k) - The deque will store at most k indices.
    """
    if not nums:
        return []
        
    result = []
    # Stores indices, not actual values
    dq = deque()
    
    for i in range(len(nums)):
        # 1. Remove indices that are out of the bounds of the current window
        if dq and dq[0] < i - k + 1:
            dq.popleft()
            
        # 2. Remove smaller elements from the back of the deque
        # They are useless because the current element is larger and comes later
        while dq and nums[dq[-1]] < nums[i]:
            dq.pop()
            
        # 3. Add the current index
        dq.append(i)
        
        # 4. If window has reached size k, add the max to result
        if i >= k - 1:
            result.append(nums[dq[0]])
            
    return result

# Example usage:
print(max_sliding_window([1,3,-1,-3,5,3,6,7], 3)) # Output: [3,3,5,5,6,7]
print(max_sliding_window([1], 1))                 # Output: [1]
