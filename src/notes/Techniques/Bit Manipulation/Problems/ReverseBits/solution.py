# Problem: Reverse bits of a given 32 bits unsigned integer.
def reverseBits(n: int) -> int:
    """
    Approach: Bit Shift and Mask.
    Time: O(1)
    Space: O(1)
    """
    res = 0
    for i in range(32):
        bit = (n >> i) & 1
        res = res | (bit << (31 - i))
    return res
