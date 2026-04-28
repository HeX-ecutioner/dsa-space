# Problem: Given a positive integer, check whether it has alternating bits: namely, if two adjacent bits will always have different values.
def hasAlternatingBits(n: int) -> bool:
    """
    Approach: Bit Shift.
    Time: O(1)
    Space: O(1)
    """
    n = n ^ (n >> 1)
    return (n & (n + 1)) == 0
