# Compute floor(sqrt(n)) for a non-negative integer using binary search

def integer_sqrt(n: int) -> int:
    """
    Return floor(sqrt(n)), i.e., the largest integer r such that r*r <= n.

    Binary search approach:
    - Search integer domain [0, n].
    - Maintain ans as the best candidate seen so far (largest mid with mid*mid <= n).
    - If mid*mid == n, return mid immediately.
    - If mid*mid < n, shift low up (and record mid as candidate).
    - Else shift high down.

    Works for large integers in Python (Python ints arbitrary precision).
    """
    if n < 0:
        raise ValueError("n must be non-negative")

    low, high = 0, n
    ans = 0
    while low <= high:
        mid = low + (high - low) // 2
        sq = mid * mid
        if sq == n:
            return mid  # exact square
        if sq < n:
            ans = mid
            low = mid + 1
        else:
            high = mid - 1
    return ans


if __name__ == "__main__":
    for x in [0, 1, 2, 3, 4, 15, 16, 17, 10**12]:
        print(f"sqrt({x}) = {integer_sqrt(x)}")
