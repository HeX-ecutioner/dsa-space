# Problem: Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
# In other words, return true if one of s1's permutations is the substring of s2.
from collections import Counter

def check_inclusion(s1: str, s2: str) -> bool:
    """
    Approach: Fixed-size Sliding Window.
    Since a permutation of s1 must have the exact same length and character frequencies as s1,
    we can use a sliding window of size `len(s1)` over `s2`.
    We maintain a frequency map for `s1` and another for our current window in `s2`.
    As we slide the window, we add the new character entering the window and remove
    the old character exiting the window. If at any point the frequency maps match,
    we found a permutation!
    
    Time: O(n) - Where n is the length of s2. We process each character effectively in O(1).
    Space: O(1) - The hash maps will store at most 26 lowercase English letters.
    """
    len1, len2 = len(s1), len(s2)
    if len1 > len2:
        return False
        
    # Count frequencies of characters in s1
    s1_count = Counter(s1)
    # Count frequencies of characters in the first window of s2
    window_count = Counter(s2[:len1])
    
    # If the first window matches, we are done
    if s1_count == window_count:
        return True
        
    # Slide the window across s2
    for i in range(len1, len2):
        # Add the new character entering the window from the right
        new_char = s2[i]
        window_count[new_char] = window_count.get(new_char, 0) + 1
        
        # Remove the old character exiting the window from the left
        old_char = s2[i - len1]
        window_count[old_char] -= 1
        
        # If the count drops to 0, completely delete it from the dictionary
        # to ensure dictionary comparison `==` works correctly
        if window_count[old_char] == 0:
            del window_count[old_char]
            
        # Check if the current window is a permutation
        if s1_count == window_count:
            return True
            
    return False

# Example usage:
print(check_inclusion("ab", "eidbaooo")) # Output: True (s2 contains "ba")
print(check_inclusion("ab", "eidboaoo")) # Output: False
