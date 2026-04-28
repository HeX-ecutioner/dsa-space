# Problem: Write a function that takes the binary representation of an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).

def hamming_weight(n: int) -> int:
    """
    Approach: Brian Kernighan's Algorithm.
    The trick `n & (n - 1)` flips the least significant 1-bit of `n` to 0.
    Instead of checking every single bit (which would take 32 iterations for a 32-bit int),
    we can just repeatedly apply `n & (n - 1)` until `n` becomes 0.
    The number of times we can do this is exactly the number of 1-bits in `n`.
    
    Time: O(k) - Where k is the number of set bits (1s) in the number.
    Space: O(1) - Constant space.
    """
    count = 0
    while n != 0:
        # Drop the lowest set bit
        n = n & (n - 1)
        count += 1
        
    return count

# Example usage:
print(hamming_weight(11)) # Output: 3 (11 is 1011 in binary, which has three 1s)
print(hamming_weight(128)) # Output: 1 (128 is 10000000 in binary, which has one 1)
