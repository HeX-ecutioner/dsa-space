# Problem: Given an integer array nums and an integer k, return the number of good subarrays of nums. A good array is an array where the number of different integers in that array is exactly k.
def subarraysWithKDistinct(nums, k):
    """
    Approach: Sliding Window (At most K - At most K-1).
    Time: O(N)
    Space: O(N)
    """
    def atMostK(k):
        count = {}
        res = i = 0
        for j in range(len(nums)):
            if count.get(nums[j], 0) == 0: k -= 1
            count[nums[j]] = count.get(nums[j], 0) + 1
            while k < 0:
                count[nums[i]] -= 1
                if count[nums[i]] == 0: k += 1
                i += 1
            res += j - i + 1
        return res
    return atMostK(k) - atMostK(k - 1)
