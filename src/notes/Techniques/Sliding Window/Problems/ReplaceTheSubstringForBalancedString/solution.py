# Problem: You are given a string containing only 4 kinds of characters 'Q', 'W', 'E', and 'R'. Return the minimum length of the substring that can be replaced to make the string balanced.
import collections
def balancedString(s):
    """
    Approach: Variable Sliding Window.
    Time: O(N)
    Space: O(1)
    """
    count = collections.Counter(s)
    res = n = len(s)
    i = 0
    for j, c in enumerate(s):
        count[c] -= 1
        while i < n and all(n / 4 >= count[c] for c in 'QWER'):
            res = min(res, j - i + 1)
            count[s[i]] += 1
            i += 1
    return res
