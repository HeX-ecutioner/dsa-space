# Problem: Given an integer array nums where every element appears three times except for one, which appears exactly once. Find the single element and return it.
# You must implement a solution with a linear runtime complexity and use only constant extra space.
from typing import List

def single_number_ii(nums: List[int]) -> int:
    """
    Approach: Bit Manipulation (Bit Counting).
    Since every number appears three times except for one, if we sum the bits at 
    each position across ALL numbers, the sum at each bit position should be a 
    multiple of 3.
    
    If the sum at a specific bit position is NOT a multiple of 3, it means the 
    single number that appears only once has a '1' at that bit position.
    
    We can count the bits for all 32 positions (for a 32-bit integer).
    Note: Python handles integers differently (arbitrary precision), so we need 
    to handle negative numbers manually by checking the 31st bit (sign bit).
    
    Time: O(32 * n) = O(n) - We iterate through the array 32 times.
    Space: O(1) - Constant space.
    """
    result = 0
    
    # Iterate over all 32 bits (0 to 31)
    for i in range(32):
        bit_sum = 0
        # Count how many numbers have the i-th bit set to 1
        for num in nums:
            if num < 0:
                # Handle Python's negative number representation using bitwise AND with 32-bit mask
                num = num & (2**32 - 1)
            if (num >> i) & 1:
                bit_sum += 1
                
        # If the sum is not divisible by 3, the unique number has a 1 here
        if bit_sum % 3 != 0:
            result |= (1 << i)
            
    # Handle negative numbers in Python
    # If the 31st bit is set, it means the result is negative in 32-bit representation
    if result >= 2**31:
        result -= 2**32
        
    return result

# Example usage:
print(single_number_ii([2,2,3,2]))       # Output: 3
print(single_number_ii([0,1,0,1,0,1,99])) # Output: 99
