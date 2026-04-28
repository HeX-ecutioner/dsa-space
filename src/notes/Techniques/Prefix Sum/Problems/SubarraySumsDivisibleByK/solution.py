# Problem: Given an integer array nums and an integer k, return the number of non-empty subarrays that have a sum divisible by k.
def subarraysDivByK(nums, k):
    """
    Approach: Prefix Sum Modulo Frequency.
    Time: O(N)
    Space: O(K)
    """
    prefix = 0
    res = 0
    count = {0: 1}
    for n in nums:
        prefix = (prefix + n) % k
        res += count.get(prefix, 0)
        count[prefix] = count.get(prefix, 0) + 1
    return res
