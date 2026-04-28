# Problem: Given a string s and an integer k, return the length of the longest substring of s that contains at most k distinct characters.
def lengthOfLongestSubstringKDistinct(s: str, k: int) -> int:
    """
    Approach: Variable Sliding Window.
    Time: O(N)
    Space: O(K)
    """
    count = {}
    res = 0
    l = 0
    for r in range(len(s)):
        count[s[r]] = count.get(s[r], 0) + 1
        while len(count) > k:
            count[s[l]] -= 1
            if count[s[l]] == 0:
                del count[s[l]]
            l += 1
        res = max(res, r - l + 1)
    return res
