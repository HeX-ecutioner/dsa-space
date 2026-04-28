# Problem: Given two strings s and t, return the minimum window in s which will contain all the characters in t. If there is no such window, return the empty string "".
from collections import Counter

def min_window(s: str, t: str) -> str:
    """
    Approach: Variable-size Sliding Window.
    We use two pointers to create a window. We expand the right pointer until
    we have all the characters from string `t` inside our window.
    Once we have a valid window, we start shrinking from the left to find
    the MINIMUM window possible that still contains all characters of `t`.
    
    Time: O(n) - where n is the length of string s. Left and right pointers only move forward.
    Space: O(m) - where m is the unique characters in string t (for the hash map).
    """
    if not t or not s:
        return ""
        
    # Dictionary to keep track of the required characters and their counts
    dict_t = Counter(t)
    required = len(dict_t)
    
    # Left and Right pointer
    l, r = 0, 0
    
    # Formed is used to keep track of how many unique characters in t
    # are present in the current window in its desired frequency.
    formed = 0
    window_counts = {}
    
    # ans tuple of the form (window length, left, right)
    ans = float("inf"), None, None
    
    while r < len(s):
        # Add one character from the right to the window
        character = s[r]
        window_counts[character] = window_counts.get(character, 0) + 1
        
        # If the frequency of the current character added equals to the
        # desired count in t then increment the formed count by 1.
        if character in dict_t and window_counts[character] == dict_t[character]:
            formed += 1
            
        # Try and contract the window till the point where it ceases to be 'desirable'.
        while l <= r and formed == required:
            character = s[l]
            
            # Save the smallest window until now.
            if r - l + 1 < ans[0]:
                ans = (r - l + 1, l, r)
                
            # The character at the position pointed by the `left` pointer is no longer a part of the window.
            window_counts[character] -= 1
            if character in dict_t and window_counts[character] < dict_t[character]:
                formed -= 1
                
            # Move the left pointer ahead, this would help to look for a new window.
            l += 1    
            
        # Keep expanding the window once we are done contracting.
        r += 1    
        
    return "" if ans[0] == float("inf") else s[ans[1] : ans[2] + 1]

# Example usage:
print(min_window("ADOBECODEBANC", "ABC")) # Output: "BANC"
print(min_window("a", "a"))               # Output: "a"
print(min_window("a", "aa"))              # Output: ""
