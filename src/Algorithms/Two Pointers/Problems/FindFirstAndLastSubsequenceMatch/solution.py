# Problem: Given pattern as subsequence, find first index where subsequence occurs and last index
from typing import Optional

def find_first_subseq(s: str, pattern: str) -> Optional[int]:
    """
    Returns the smallest index i such that pattern is a subsequence of s[i:].
    """
    n, m = len(s), len(pattern)
    j = 0; start = None

    for i in range(n):
        if s[i] == pattern[j]:
            if j == 0:
                start = i
            j += 1
            if j == m:
                return start
    return None

def find_last_subseq(s: str, pattern: str) -> Optional[int]:
    """
    Returns the largest index i such that pattern is a subsequence of s[i:].
    """
    n, m = len(s), len(pattern)
    j = m - 1; start = None

    for i in range(n - 1, -1, -1):
        if s[i] == pattern[j]:
            if j == m - 1:
                start = i
            j -= 1
            if j < 0:
                return i
    return None

# Example usage:
s = "abcdebdde"; pattern = "bde"
print(f"First index: {find_first_subseq(s, pattern)}, " f"Last index: {find_last_subseq(s, pattern)}") # Output: 1 and 5