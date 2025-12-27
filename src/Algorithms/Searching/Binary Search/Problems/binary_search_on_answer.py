from typing import Callable

def binary_search_on_answer(low: int, high: int, predicate: Callable[[int], bool]) -> int:
    """
    Generic binary search on an integer domain [low, high] to find the smallest x
    such that predicate(x) is True. If no such x exists, returns high + 1 as a sentinel.

    Requirements:
    - predicate must be monotonic over the domain: once predicate(x) is True,
      it must remain True for all larger x. (False...False True...True)

    Use cases:
    - minimize threshold, minimize maximum allowed value, capacity problems, etc.
    """
    ans = high + 1  # sentinel if nothing satisfies predicate
    while low <= high:
        mid = low + (high - low) // 2
        if predicate(mid):
            # mid satisfies predicate; try to find smaller one
            ans = mid
            high = mid - 1
        else:
            # mid does not satisfy; need larger mid
            low = mid + 1
    return ans


# Example: integer_sqrt_ceil using binary_search_on_answer
def integer_sqrt_ceil(n: int) -> int:
    """
    Return smallest integer x such that x*x >= n (ceiling of sqrt).
    Example: integer_sqrt_ceil(10) -> 4
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    return binary_search_on_answer(0, n, lambda x: x * x >= n)


if __name__ == "__main__":
    print("ceil_sqrt(10) ->", integer_sqrt_ceil(10))  # expect 4
    print("ceil_sqrt(16) ->", integer_sqrt_ceil(16))  # expect 4
    print("ceil_sqrt(17) ->", integer_sqrt_ceil(17))  # expect 5
