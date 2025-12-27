# Compress String in-place (like "aaabb" -> "a3b2") simplified
from typing import List

def compress(chars: List[str]) -> int:
    """
    Modify chars in-place to its compressed form and return new length.
    Approach:
    - Two pointers: read scanning groups, write writing compressed output.
    - For each group of same chars, write char then its count digits (if >1).
    Time: O(n), Space: O(1)
    """
    write = 0
    read = 0
    n = len(chars)
    while read < n:
        ch = chars[read]
        count = 0
        while read < n and chars[read] == ch:
            read += 1
            count += 1
        # write the character
        chars[write] = ch
        write += 1
        # write count if >1
        if count > 1:
            for c in str(count):
                chars[write] = c
                write += 1
    return write

# Example:
# chars = list("aabbccc") -> compress(chars) -> returns new length, chars[:newlen] = compressed string
