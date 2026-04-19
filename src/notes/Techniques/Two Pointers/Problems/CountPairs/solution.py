# This is a combined problem: Count Pairs With Sum Less Than K and Count Pairs With Product Less Than K
from typing import List

def count_pairs(nums: List[int], k: int, operation: str = "sum") -> int:
    """
    Count number of index pairs (i<j) based on the chosen operation.
    Args:
        nums: List of integers
        k: Threshold value
        operation: "sum" or "product" (default: "sum")
    Returns:
        Count of valid pairs
    Time: O(n log n) to sort + O(n) two-pointer pass
    """
    if operation not in ["sum", "product"]:
        raise ValueError("operation must be 'sum' or 'product'")
    
    nums.sort()
    left, right = 0, len(nums) - 1
    count = 0
    
    while left < right:
        if operation == "sum":
            value = nums[left] + nums[right]
        else:  # product
            value = nums[left] * nums[right]
        
        if value < k:
            count += (right - left)
            left += 1
        else:
            right -= 1
    
    return count

# Example:
print(count_pairs([1,2,3,4,5,6], 10, "sum"))  # Output: 13
print(count_pairs([1,2,3,4], 8, "product"))  # Output: 4