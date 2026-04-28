# Problem: Given an integer array nums and an integer k, return true if nums has a good subarray or false otherwise.
# A good subarray is a contiguous part of the array where:
# - its length is at least two, and
# - the sum of the elements of the subarray is a multiple of k.
from typing import List

def check_subarray_sum(nums: List[int], k: int) -> bool:
    """
    Approach: Prefix Sum with Modulo Arithmetic.
    If the sum of a subarray from index `i` to `j` is a multiple of `k`, then:
    (prefix_sum[j] - prefix_sum[i-1]) % k == 0
    
    By the rules of modular arithmetic, this implies:
    prefix_sum[j] % k == prefix_sum[i-1] % k
    
    So, as we compute the prefix sum, we store `prefix_sum % k` in a hash map 
    along with its first seen index. If we encounter the same modulo value again 
    at an index that is at least 2 steps away from the first seen index, we found 
    a valid subarray!
    
    Time: O(n) - Single pass over the array.
    Space: O(min(n, k)) - Space for the hash map storing modulo values.
    """
    # Dictionary to store {prefix_sum % k: first_seen_index}
    # Initialize with {0: -1} to handle the case where the prefix from index 0 is a multiple of k
    remainder_map = {0: -1}
    
    current_sum = 0
    
    for i in range(len(nums)):
        current_sum += nums[i]
        
        # Calculate modulo
        # We don't have to worry about k=0 because problem constraints typically specify k >= 1
        remainder = current_sum % k
        
        # If we have seen this remainder before
        if remainder in remainder_map:
            # Check if the subarray length is at least 2
            if i - remainder_map[remainder] >= 2:
                return True
        else:
            # Only store the FIRST time we see this remainder to maximize subarray length
            remainder_map[remainder] = i
            
    return False

# Example usage:
print(check_subarray_sum([23,2,4,6,7], 6)) # Output: True (Subarray [2, 4] sums to 6)
print(check_subarray_sum([23,2,6,4,7], 6)) # Output: True (Subarray [23, 2, 6, 4, 7] sums to 42, 42%6==0)
print(check_subarray_sum([23,2,6,4,7], 13))# Output: False
