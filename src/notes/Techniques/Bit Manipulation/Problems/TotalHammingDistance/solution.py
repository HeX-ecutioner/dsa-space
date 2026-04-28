# Problem: The Hamming distance between two integers is the number of positions at which the corresponding bits are different. Given an integer array nums, return the sum of Hamming distances between all the pairs of the integers in nums.
def totalHammingDistance(nums):
    """
    Approach: Count bits column by column.
    Time: O(N)
    Space: O(1)
    """
    res = 0
    n = len(nums)
    for i in range(32):
        count_ones = sum((num >> i) & 1 for num in nums)
        res += count_ones * (n - count_ones)
    return res
