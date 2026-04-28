# Problem: Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose sum is greater than or equal to target.
def minSubArrayLen(target, nums):
    """
    Approach: Variable Sliding Window.
    Time: O(N)
    Space: O(1)
    """
    l, total = 0, 0
    res = float("inf")
    for r in range(len(nums)):
        total += nums[r]
        while total >= target:
            res = min(res, r - l + 1)
            total -= nums[l]
            l += 1
    return 0 if res == float("inf") else res
