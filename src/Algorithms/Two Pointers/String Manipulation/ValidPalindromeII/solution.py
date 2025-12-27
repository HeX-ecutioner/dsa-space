# Valid Palindrome II - can remove at most one char to make palindrome
# Approach: two pointers, when mismatch occurs, try skipping left or right and check palindrome.
def is_palindrome_range(s: str, left: int, right: int) -> bool:
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

def valid_palindrome_ii(s: str) -> bool:
    """
    Time: O(n), Space: O(1)
    At most one deletion allowed.
    """
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            # try skipping left or right
            return is_palindrome_range(s, left+1, right) or is_palindrome_range(s, left, right-1)
        left += 1
        right -= 1
    return True

# Example:
# valid_palindrome_ii("abca") -> True (remove 'c' or 'b')
