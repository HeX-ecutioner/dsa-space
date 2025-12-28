from typing import List

def count_pairs_with_distance(nums: List[int], max_dist: int) -> int:
    # Count number of pairs with difference <= max_dist using two pointers after sorting
    nums.sort()
    count = left = 0
    for right in range(len(nums)):
        while nums[right] - nums[left] > max_dist:
            left += 1
        count += (right - left)
    return count

def kth_smallest_pair_distance(nums: List[int], k: int) -> int:
    """
    Binary search on answer (distance), using count_pairs_with_distance as predicate.
    Time: O(n log M) where M is range of values.
    """
    nums.sort()
    low, high = 0, nums[-1] - nums[0]
    while low < high:
        mid = (low + high) // 2
        if count_pairs_with_distance(nums, mid) >= k:
            high = mid
        else:
            low = mid + 1
    return low

# Example usage:
print(kth_smallest_pair_distance([1,3,1], 1))  # Output: 0
print(kth_smallest_pair_distance([1,6,1], 3))  # Output: 5
