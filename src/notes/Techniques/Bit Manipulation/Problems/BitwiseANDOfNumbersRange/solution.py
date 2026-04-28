# Problem: Given two integers left and right that represent the range [left, right], return the bitwise AND of all numbers in this range, inclusive.
def rangeBitwiseAnd(left: int, right: int) -> int:
    """
    Approach: Bit Shift.
    Time: O(1)
    Space: O(1)
    """
    shift = 0
    while left < right:
        left >>= 1
        right >>= 1
        shift += 1
    return left << shift
