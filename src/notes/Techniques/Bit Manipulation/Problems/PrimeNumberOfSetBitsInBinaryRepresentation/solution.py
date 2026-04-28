# Problem: Given two integers left and right, return the count of numbers in the inclusive range [left, right] having a prime number of set bits in their binary representation.
def countPrimeSetBits(left: int, right: int) -> int:
    """
    Approach: Bit Manipulation and Primes.
    Time: O(N)
    Space: O(1)
    """
    primes = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31}
    res = 0
    for i in range(left, right + 1):
        if bin(i).count('1') in primes:
            res += 1
    return res
