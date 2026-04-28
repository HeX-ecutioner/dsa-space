# Problem: Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
from typing import List

def missing_number(nums: List[int]) -> int:
    """
    Approach: Bit Manipulation (XOR).
    We know that XOR of a number with itself is 0 (a ^ a = 0).
    The array is supposed to contain all numbers from 0 to n. 
    If we XOR all the indices (from 0 to n) AND all the values in the array,
    the numbers that are present will cancel out with their corresponding indices.
    The only number left will be the one that is missing.
    
    Example: nums = [3, 0, 1]
    Indices: 0, 1, 2, 3 (n = 3)
    Values:  3, 0, 1
    
    XOR everything:
    (0^0) ^ (1^1) ^ (3^3) ^ 2 = 0 ^ 0 ^ 0 ^ 2 = 2
    
    Time: O(n) - Single pass over the array.
    Space: O(1) - Constant space.
    """
    missing = len(nums) # Initialize with n
    for i, num in enumerate(nums):
        missing ^= i ^ num
        
    return missing

# Example usage:
print(missing_number([3, 0, 1]))                   # Output: 2
print(missing_number([0, 1]))                      # Output: 2
print(missing_number([9, 6, 4, 2, 3, 5, 7, 0, 1])) # Output: 8
