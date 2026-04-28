# Problem: Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
# You must implement a solution with a linear runtime complexity and use only constant extra space.
from typing import List

def single_number(nums: List[int]) -> int:
    """
    Approach: Bit Manipulation (XOR).
    We use the fundamental XOR property:
    1. a ^ a = 0 (XORing a number with itself gives 0)
    2. a ^ 0 = a (XORing a number with 0 leaves it unchanged)
    3. XOR is commutative and associative.
    
    If we XOR all the numbers in the array together, the numbers that appear
    twice will cancel each other out (become 0). The only remaining number
    will be the single number that appears once.
    
    Time: O(n) - We iterate through the array once.
    Space: O(1) - We only use one integer variable.
    """
    result = 0
    for num in nums:
        # XOR the current number with our running result
        result ^= num
        
    return result

# Example usage:
print(single_number([2, 2, 1]))       # Output: 1
print(single_number([4, 1, 2, 1, 2])) # Output: 4
print(single_number([1]))             # Output: 1
