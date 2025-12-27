# Check Palindrome (String) using two pointers
# Problem: Determine whether a string is a palindrome (ignoring non-alphanumerics and case).
# Approach: Use left/right pointers, advance inward, compare characters.
from typing import List

def is_palindrome(s: str) -> bool:
    """
    Returns True if s is palindrome considering only alphanumeric chars and ignoring case.
    Time: O(n), Space: O(1) extra (not counting input).
    """
    # normalize pointers
    left, right = 0, len(s) - 1

    # iterate while left < right
    while left < right:
        # move left to next alphanumeric
        while left < right and not s[left].isalnum():
            left += 1
        # move right to previous alphanumeric
        while left < right and not s[right].isalnum():
            right -= 1
        # compare lowercase forms
        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1
    return True

# Example:
# is_palindrome("A man, a plan, a canal: Panama") -> True
