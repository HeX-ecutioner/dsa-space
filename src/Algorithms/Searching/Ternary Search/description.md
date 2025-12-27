# Ternary Search

## Description
Ternary Search generalizes binary search by dividing the search interval
into three parts. It's primarily used to find the maximum (or minimum)
of a **unimodal** function on an interval.

This folder demonstrates two useful and distinct flavors:
1. **Ternary search for continuous unimodal functions** (floating-point).
   - Typical use: optimization on a unimodal function (find max/min).
   - We use two interior points m1 and m2 and reduce the interval.
2. **Ternary-like search on discrete unimodal arrays** (find peak index).
   - This adapts the ternary idea; in practice, a binary-style peak finder is common.
   - Good demonstration of logarithmic search on "mountain" arrays.

---

## Example (continuous)
f(x) = -(x-2)^2 + 4  (peak at x=2)
Search interval: [-10, 10]
Ternary search approximates x ≈ 2.0

## Example (discrete)
arr = [1, 3, 7, 12, 11, 6, 2]
Peak index -> 3 (value 12)

---

## Algorithm Steps (continuous unimodal)
1. Choose m1 = left + (right-left)/3 and m2 = right - (right-left)/3
2. If f(m1) < f(m2): left = m1 (peak is to the right)
   Else: right = m2 (peak is to the left)
3. Repeat until desired precision

## Pseudocode (continuous)
```yaml
repeat iterations times:
m1 = left + (right-left)/3
m2 = right - (right-left)/3
if f(m1) < f(m2): left = m1
else: right = m2
return (left+right)/2
```

## Time Complexity
- Continuous float version: O(iterations) where iterations controls precision.
- Discrete unimodal array: O(log n) (using integer divisions), final small-range brute force O(1).

## Space Complexity
- O(1)

## Notes
- Ternary search is perfect for optimization when the function is unimodal.
- For discrete arrays, binary-search-based peak finding may be simpler and more robust.
- Be careful: ternary search assumes unimodality; if the function/array isn't unimodal,
  the algorithm may give incorrect results.
- Ternary search on continuous functions is used in numeric optimization problems.