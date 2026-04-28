# Problem: Given an array of integers nums, you start with an initial positive value startValue. In each iteration, you calculate the step by step sum of startValue plus elements in nums. Return the minimum positive value of startValue such that the step by step sum is never less than 1.
def minStartValue(nums):
    """
    Approach: Prefix Sum (Find Min).
    Time: O(N)
    Space: O(1)
    """
    min_prefix = float("inf")
    current_sum = 0
    for n in nums:
        current_sum += n
        min_prefix = min(min_prefix, current_sum)
    return max(1, 1 - min_prefix)
