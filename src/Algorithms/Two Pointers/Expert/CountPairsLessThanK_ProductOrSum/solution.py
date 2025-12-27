# Combined problem: Count Pairs With Sum Less Than K AND Count Pairs With Product Less Than K
# We implement both functions using two pointers after sorting.
from typing import List

def count_pairs_with_sum_less_than(nums: List[int], k: int) -> int:
    """
    Count number of index pairs (i<j) such that nums[i] + nums[j] < k.
    Approach:
    - Sort nums, use two pointers left=0, right=n-1
    - If nums[left] + nums[right] < k => all pairs (left, left+1..right) are valid -> add (right-left) and left++
    - Else right--.
    Time: O(n log n) to sort + O(n) two-pointer pass
    """
    nums.sort()
    left, right = 0, len(nums) - 1
    count = 0
    while left < right:
        s = nums[left] + nums[right]
        if s < k:
            count += (right - left)
            left += 1
        else:
            right -= 1
    return count

def count_pairs_with_product_less_than(nums: List[int], k: int) -> int:
    """
    Count number of pairs with product < k.
    Notes:
    - If nums contain negatives and zeros, logic becomes more complex.
    - Here we implement for non-negative nums (common interview variant).
    Approach for non-negative:
    - Sort nums.
    - Use two pointers similar to sum: if nums[left]*nums[right] < k -> add (right-left) and left++ else right--.
    Time: O(n log n) + O(n)
    """
    nums.sort()
    left, right = 0, len(nums) - 1
    count = 0
    while left < right:
        prod = nums[left] * nums[right]
        if prod < k:
            count += (right - left)
            left += 1
        else:
            right -= 1
    return count

# Example:
# count_pairs_with_sum_less_than([1,2,3,4], 5) -> pairs: (1,2),(1,3),(2,3) => 3
# count_pairs_with_product_less_than([1,2,3,4], 8) -> pairs: (1,2),(1,3),(1,4),(2,3) => 4
