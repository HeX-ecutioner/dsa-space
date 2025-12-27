# Three Sum - find unique triplets that sum to zero
# Approach: sort + fix one element, then two-pointer for remaining two
from typing import List

def three_sum(nums: List[int]) -> List[List[int]]:
    """
    Returns list of unique triplets [a,b,c] with a+b+c == 0.
    Steps:
    - Sort array.
    - For each i, use two pointers (left=i+1, right=end) to find pairs summing to -nums[i].
    - Skip duplicates to ensure uniqueness.
    Time: O(n^2), Space: O(1) extra (output excluded)
    """
    nums.sort()
    res = []
    n = len(nums)
    for i in range(n):
        # skip duplicates for i
        if i > 0 and nums[i] == nums[i-1]:
            continue
        target = -nums[i]
        left, right = i+1, n-1
        while left < right:
            s = nums[left] + nums[right]
            if s == target:
                res.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
                # skip duplicates for left and right
                while left < right and nums[left] == nums[left-1]:
                    left += 1
                while left < right and nums[right] == nums[right+1]:
                    right -= 1
            elif s < target:
                left += 1
            else:
                right -= 1
    return res

# Example:
# three_sum([-1,0,1,2,-1,-4]) -> [[-1,-1,2],[-1,0,1]]
