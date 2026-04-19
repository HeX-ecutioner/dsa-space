"""
Problem: Subarray Sum Equals K
Statement: Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.
"""

def subarraySum(nums, k):
    # Time Complexity: O(n) - Single pass through the array.
    # Space Complexity: O(n) - Hash map to store prefix sums.
    
    count = 0
    current_sum = 0
    # Dictionary to store how many times a specific prefix sum has occurred.
    # Initialize with {0: 1} to handle cases where a prefix itself equals k.
    prefix_sums = {0: 1} 
    
    for num in nums:
        current_sum += num
        
        # If (current_sum - k) exists in our map, it means there is a subarray
        # ending here that sums to k.
        diff = current_sum - k
        if diff in prefix_sums:
            count += prefix_sums[diff]
            
        # Add the current prefix sum to our map
        prefix_sums[current_sum] = prefix_sums.get(current_sum, 0) + 1
            
    return count

if __name__ == "__main__":
    nums = [1, 1, 1]
    k = 2
    print("Subarrays summing to 2:", subarraySum(nums, k)) # Expected: 2