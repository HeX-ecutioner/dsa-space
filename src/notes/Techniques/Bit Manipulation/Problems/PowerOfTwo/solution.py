# Problem: Given an integer n, return true if it is a power of two. Otherwise, return false.
# An integer n is a power of two, if there exists an integer x such that n == 2^x.

def is_power_of_two(n: int) -> bool:
    """
    Approach: Bit Manipulation.
    A power of two in binary representation always has exactly ONE bit set to 1.
    For example:
    2 = 0010
    4 = 0100
    8 = 1000
    
    If we subtract 1 from a power of two, all bits after the 1-bit become 1s,
    and the 1-bit becomes 0.
    For example:
    8 - 1 = 7 (0111)
    
    Therefore, a bitwise AND of `n` and `n - 1` will always be 0 IF `n` is a power of two.
    i.e., n & (n - 1) == 0.
    
    Time: O(1) - Constant time.
    Space: O(1) - Constant space.
    """
    # A power of two must be strictly greater than 0
    if n <= 0:
        return False
        
    return (n & (n - 1)) == 0

# Example usage:
print(is_power_of_two(1))  # Output: True (2^0)
print(is_power_of_two(16)) # Output: True (2^4)
print(is_power_of_two(3))  # Output: False
print(is_power_of_two(0))  # Output: False
