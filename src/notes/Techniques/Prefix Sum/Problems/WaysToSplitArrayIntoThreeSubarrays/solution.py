# Problem: You are given a 0-indexed integer array nums. Find the number of ways to split the array into three continuous subarrays (left, mid, right) such that sum(left) <= sum(mid) <= sum(right).
import bisect
def waysToSplit(nums):
    """
    Approach: Prefix Sum with Binary Search.
    Time: O(N log N)
    Space: O(N)
    """
    n = len(nums)
    prefix = [0] * n
    prefix[0] = nums[0]
    for i in range(1, n): prefix[i] = prefix[i-1] + nums[i]
    res, MOD = 0, 10**9 + 7
    for i in range(n - 2):
        left_sum = prefix[i]
        j = bisect.bisect_left(prefix, 2 * left_sum, i + 1, n - 1)
        k = bisect.bisect_right(prefix, (prefix[-1] + prefix[i]) // 2, i + 1, n - 1)
        if k > j: res = (res + k - j) % MOD
    return res
