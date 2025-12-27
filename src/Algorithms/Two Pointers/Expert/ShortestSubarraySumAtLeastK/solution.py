# Shortest Subarray with Sum at Least K - advanced two-pointer + deque/prefix trick
from typing import List
import collections

def shortest_subarray_at_least_K(nums: List[int], K: int) -> int:
    """
    This problem is hard: for possibly negative numbers, sliding-window doesn't directly work.
    Use prefix sums + monotonic deque (O(n)).
    Brief steps:
    - Compute prefix sums P where P[0]=0, P[i+1]=P[i]+nums[i]
    - Maintain deque of indices with increasing P values
    - For each j, while P[j] - P[deque[0]] >= K, update answer and pop left
    - While P[j] <= P[deque[-1]], pop right to keep deque monotonic
    Time: O(n)
    """
    n = len(nums)
    P = [0] * (n + 1)
    for i in range(n):
        P[i+1] = P[i] + nums[i]
    ans = n + 1
    dq = collections.deque()  # stores indices
    for j in range(n + 1):
        # if current prefix is large enough with smallest prefix in deque
        while dq and P[j] - P[dq[0]] >= K:
            ans = min(ans, j - dq.popleft())
        # maintain increasing P indices
        while dq and P[j] <= P[dq[-1]]:
            dq.pop()
        dq.append(j)
    return ans if ans <= n else -1

# Example:
# shortest_subarray_at_least_K([2,-1,2], 3) -> 3 (whole array)
