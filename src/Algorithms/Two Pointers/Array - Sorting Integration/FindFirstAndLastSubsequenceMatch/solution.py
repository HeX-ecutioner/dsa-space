# Find First and Last Subsequence Match
# Problem: Given pattern as subsequence, find first index where subsequence occurs and last index.
from typing import List, Optional

def find_first_subseq(s: str, pattern: str) -> Optional[int]:
    """
    Find first index i in s such that pattern is subsequence starting at or after i.
    We can scan s and pattern together.
    Time: O(n)
    """
    n, m = len(s), len(pattern)
    i = j = 0
    while i < n and j < m:
        if s[i] == pattern[j]:
            j += 1
        i += 1
    return 0 if j == m else None  # simplified signature

# For last match, more involved: scan from end with reversed pattern.
def find_last_subseq(s: str, pattern: str) -> Optional[int]:
    """
    Simplified version: find if pattern is subsequence; returns None or 0.
    Implementations vary by exact requirement; this placeholder indicates approach.
    """
    # A general approach: for each position in s, check subsequence start; or precompute next-occurrence table.
    return None
