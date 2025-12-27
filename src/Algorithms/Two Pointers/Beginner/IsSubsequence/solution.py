# Is Subsequence (two pointers)
# Problem: Given strings s and t, check if s is subsequence of t.
# Approach: Advance pointer in t while matching characters of s.
def is_subsequence(s: str, t: str) -> bool:
    """
    Returns True if all characters of s appear in t in order.
    Time: O(len(t)), Space: O(1)
    """
    if not s:
        return True
    i, j = 0, 0  # i over s, j over t
    while j < len(t) and i < len(s):
        if s[i] == t[j]:
            i += 1
        j += 1
    return i == len(s)

# Example:
# is_subsequence("abc", "ahbgdc") -> True
# is_subsequence("axc", "ahbgdc") -> False
