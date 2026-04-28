# Problem: Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.
from typing import List

def count_bits(n: int) -> List[int]:
    """
    Approach: Bit Manipulation with Dynamic Programming.
    Instead of calculating the number of 1s for each number from scratch (O(n log n)),
    we can use previously computed results.
    
    Trick: `i >> 1` (or `i // 2`) shifts the bits of `i` to the right by 1.
    This effectively chops off the last bit.
    So, the number of 1s in `i` is equal to the number of 1s in `i // 2` PLUS
    1 if the last bit was a 1 (which we check via `i & 1`).
    
    Formula: ans[i] = ans[i >> 1] + (i & 1)
    
    Time: O(n) - We calculate the answer for each number in O(1) time.
    Space: O(n) - For the result array (or O(1) extra space).
    """
    ans = [0] * (n + 1)
    
    for i in range(1, n + 1):
        # i >> 1 is the same as i // 2
        # i & 1 is the same as i % 2 (checks if last bit is 1)
        ans[i] = ans[i >> 1] + (i & 1)
        
    return ans

# Example usage:
print(count_bits(2)) # Output: [0, 1, 1] (0->0, 1->1, 2->10)
print(count_bits(5)) # Output: [0, 1, 1, 2, 1, 2]
