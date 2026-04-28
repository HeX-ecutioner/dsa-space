# Problem: Given a binary array, find the maximum number of consecutive 1s in this array if you can flip at most one 0.
def findMaxConsecutiveOnes(nums):
    """
    Approach: Variable Sliding Window.
    Time: O(N)
    Space: O(1)
    """
    l = 0
    zeroes = 0
    res = 0
    for r in range(len(nums)):
        if nums[r] == 0:
            zeroes += 1
        while zeroes > 1:
            if nums[l] == 0:
                zeroes -= 1
            l += 1
        res = max(res, r - l + 1)
    return res
