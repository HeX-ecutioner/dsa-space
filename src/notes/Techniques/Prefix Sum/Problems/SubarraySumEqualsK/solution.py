# Problem: Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.
# A subarray is a contiguous non-empty sequence of elements within an array.
from typing import List

def subarray_sum(nums: List[int], k: int) -> int:
    """
    Approach: Prefix Sum with Hash Map.
    If we calculate the cumulative sum (prefix sum) as we iterate, the sum of 
    any subarray [i, j] is `prefix_sum[j] - prefix_sum[i-1]`.
    
    We want to find subarrays where: `prefix_sum[j] - prefix_sum[i-1] == k`
    Which translates to: `prefix_sum[i-1] == prefix_sum[j] - k`
    
    So, as we iterate, we maintain the current prefix sum. We check if 
    `(current_sum - k)` has been seen before. If it has, it means there is a
    valid subarray ending at the current index. We use a hash map to count 
    the occurrences of each prefix sum.
    
    Time: O(n) - Single pass over the array.
    Space: O(n) - Hash map can store up to n distinct prefix sums.
    """
    count = 0
    current_sum = 0
    
    # Hash map to store the frequency of each prefix sum.
    # We initialize it with {0: 1} to handle the case where a subarray
    # starts from the 0-th index and matches exactly `k`.
    prefix_sum_counts = {0: 1}
    
    for num in nums:
        current_sum += num
        
        # Check if we have seen a prefix sum that would leave exactly `k`
        if (current_sum - k) in prefix_sum_counts:
            count += prefix_sum_counts[current_sum - k]
            
        # Add the current prefix sum to our map
        prefix_sum_counts[current_sum] = prefix_sum_counts.get(current_sum, 0) + 1
        
    return count

# Example usage:
print(subarray_sum([1, 1, 1], 2))       # Output: 2 (Subarrays: [1, 1] at start, and [1, 1] at end)
print(subarray_sum([1, 2, 3], 3))       # Output: 2 (Subarrays: [1, 2] and [3])
print(subarray_sum([-1, -1, 1], 0))     # Output: 1 (Subarray: [-1, 1])
