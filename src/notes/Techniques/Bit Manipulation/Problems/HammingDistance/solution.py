# Problem: The Hamming distance between two integers is the number of positions at which the corresponding bits are different. Given two integers x and y, return the Hamming distance between them.
def hammingDistance(x: int, y: int) -> int:
    """
    Approach: XOR and Brian Kernighan's Algorithm.
    Time: O(1)
    Space: O(1)
    """
    xor = x ^ y
    res = 0
    while xor:
        res += 1
        xor = xor & (xor - 1)
    return res
