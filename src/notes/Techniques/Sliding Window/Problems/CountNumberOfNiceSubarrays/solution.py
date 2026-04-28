# Problem: Given an array of integers nums and an integer k. A continuous subarray is called nice if there are k odd numbers on it.
def numberOfSubarrays(nums, k):
    """
    Approach: Sliding Window (At most K - At most K-1).
    Time: O(N)
    Space: O(1)
    """
    def atMost(k):
        res = i = 0
        for j in range(len(nums)):
            k -= nums[j] % 2
            while k < 0:
                k += nums[i] % 2
                i += 1
            res += j - i + 1
        return res
    return atMost(k) - atMost(k - 1)
