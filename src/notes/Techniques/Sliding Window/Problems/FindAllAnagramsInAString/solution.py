# Problem: Given two strings s and p, return an array of all the start indices of p's anagrams in s.
from collections import Counter
def findAnagrams(s: str, p: str):
    """
    Approach: Fixed Sliding Window.
    Time: O(N)
    Space: O(1) (26 characters)
    """
    res = []
    pCount, sCount = Counter(p), Counter(s[:len(p)-1])
    l = 0
    for r in range(len(p)-1, len(s)):
        sCount[s[r]] = 1 + sCount.get(s[r], 0)
        if sCount == pCount:
            res.append(l)
        sCount[s[l]] -= 1
        if sCount[s[l]] == 0: sCount.pop(s[l])
        l += 1
    return res
