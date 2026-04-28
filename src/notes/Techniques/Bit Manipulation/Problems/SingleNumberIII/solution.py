# Problem: Given an integer array nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once. You can return the answer in any order.
# You must write an algorithm that runs in linear runtime complexity and uses only constant extra space.
from typing import List

def single_number_iii(nums: List[int]) -> List[int]:
    """
    Approach: Bit Manipulation (XOR).
    If we XOR all numbers, the pairs cancel out, and we are left with the XOR of the 
    TWO unique numbers (let's call them A and B).
    XOR_ALL = A ^ B
    
    Since A and B are different, they must differ in at least one bit. 
    We can find ANY set bit (1-bit) in `XOR_ALL`. Let's pick the rightmost set bit.
    
    This set bit MUST come from either A or B, but not both!
    So, we can divide the original array into two groups:
    Group 1: Numbers with this bit set to 1.
    Group 2: Numbers with this bit set to 0.
    
    A will be in one group, B will be in the other. All other pairs will be distributed 
    equally into the same group (since they are identical).
    Now, just XOR all numbers in Group 1 to find A, and Group 2 to find B!
    
    Time: O(n) - Two passes over the array.
    Space: O(1) - Constant space used.
    """
    # 1. XOR all numbers
    xor_all = 0
    for num in nums:
        xor_all ^= num
        
    # 2. Find the rightmost set bit using the trick: x & (-x)
    rightmost_set_bit = xor_all & (-xor_all)
    
    # 3. Partition numbers into two groups and XOR them
    group1 = 0
    group2 = 0
    for num in nums:
        if (num & rightmost_set_bit) != 0:
            # The bit is set
            group1 ^= num
        else:
            # The bit is not set
            group2 ^= num
            
    return [group1, group2]

# Example usage:
print(single_number_iii([1,2,1,3,2,5])) # Output: [3, 5] or [5, 3]
print(single_number_iii([-1,0]))        # Output: [-1, 0] or [0, -1]
print(single_number_iii([0,1]))         # Output: [1, 0] or [0, 1]
