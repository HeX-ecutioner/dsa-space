# Problem: Given an integer num, return a string representing its hexadecimal representation. For negative integers, two’s complement method is used.
def toHex(num: int) -> str:
    """
    Approach: Bitmasking groups of 4 bits.
    Time: O(1)
    Space: O(1)
    """
    if num == 0: return "0"
    chars = "0123456789abcdef"
    res = ""
    for _ in range(8):
        res = chars[num & 15] + res
        num >>= 4
        if num == 0: break
    return res
