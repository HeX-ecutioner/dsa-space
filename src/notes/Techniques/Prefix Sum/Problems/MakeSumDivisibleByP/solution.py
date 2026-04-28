# Problem: Given an array of positive integers nums, remove the smallest subarray (possibly empty) such that the sum of the remaining elements is divisible by p.
def minSubarray(nums, p):
    """
    Approach: Prefix Sum with Modulo Arithmetic.
    Time: O(N)
    Space: O(N)
    """
    target = sum(nums) % p
    if target == 0: return 0
    res = len(nums)
    prefix_sum = 0
    remainder_map = {0: -1}
    for i, num in enumerate(nums):
        prefix_sum = (prefix_sum + num) % p
        wanted = (prefix_sum - target + p) % p
        if wanted in remainder_map:
            res = min(res, i - remainder_map[wanted])
        remainder_map[prefix_sum] = i
    return res if res < len(nums) else -1
