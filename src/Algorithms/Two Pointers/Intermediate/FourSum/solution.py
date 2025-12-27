# Four Sum - optional (k-sum generalization)
# Approach: sort and reduce to 3-sum and two-sum via loops + two pointers
from typing import List

def four_sum(nums: List[int], target: int) -> List[List[int]]:
    """
    Returns list of unique quadruplets that sum to target.
    Approach:
    - Sort nums
    - Fix two indices i and j, then two-pointer for the rest
    - Skip duplicates carefully
    Time: O(n^3)
    """
    nums.sort()
    n = len(nums)
    res = []
    for i in range(n):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        for j in range(i+1, n):
            if j > i+1 and nums[j] == nums[j-1]:
                continue
            target2 = target - nums[i] - nums[j]
            left, right = j+1, n-1
            while left < right:
                s = nums[left] + nums[right]
                if s == target2:
                    res.append([nums[i], nums[j], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                    while left < right and nums[right] == nums[right+1]:
                        right -= 1
                elif s < target2:
                    left += 1
                else:
                    right -= 1
    return res

# Example:
# four_sum([1,0,-1,0,-2,2], 0) -> [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
