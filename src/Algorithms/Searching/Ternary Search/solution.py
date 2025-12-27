# Ternary Search - two useful flavors:
# 1) Ternary search to find maximum of a unimodal continuous function (float input)
# 2) Ternary search to find peak in a discrete unimodal array (integer array)
from typing import List, Callable

def ternary_search_max_func(f: Callable[[float], float], left: float, right: float, iterations: int = 100) -> float:
    """
    Ternary search for the maximum of a unimodal continuous function f on [left, right].
    - Assumes f is unimodal (increasing then decreasing) on the interval.
    - iterations controls precision (for floating-point search).
    Returns x that approximately maximizes f(x).
    """
    for _ in range(iterations):
        m1 = left + (right - left) / 3.0
        m2 = right - (right - left) / 3.0
        if f(m1) < f(m2):
            left = m1
        else:
            right = m2
    return (left + right) / 2.0


def ternary_search_peak_array(arr: List[int]) -> int:
    """
    Ternary-like search for the peak index in a discrete unimodal array.
    (Array increases then decreases; strict unimodal)
    Returns index of peak (maximum value).
    Note: For discrete arrays, a binary-search-style 'peak finding' is more common, but this demonstrates the ternary idea
    """
    left, right = 0, len(arr) - 1
    while right - left > 2:
        m1 = left + (right - left) // 3
        m2 = right - (right - left) // 3
        if arr[m1] < arr[m2]:
            left = m1
        else:
            right = m2
    # brute-force final small range
    best = left
    for i in range(left, right + 1):
        if arr[i] > arr[best]:
            best = i
    return best


# Example usage (not a full main, but demonstration):
if __name__ == "__main__":
    # 1) Maximize a continuous unimodal function, e.g., f(x) = -(x-2)^2 + 4  -> peak at x=2
    def f(x): return -(x - 2) ** 2 + 4
    x_peak = ternary_search_max_func(f, -10.0, 10.0, iterations=100)
    print("Approximate peak x (continuous):", x_peak, "f(x)=", f(x_peak))

    # 2) Peak in discrete unimodal array
    arr = [1, 3, 7, 12, 11, 6, 2]
    peak_idx = ternary_search_peak_array(arr)
    print("Peak index (discrete unimodal):", peak_idx, "value:", arr[peak_idx])
