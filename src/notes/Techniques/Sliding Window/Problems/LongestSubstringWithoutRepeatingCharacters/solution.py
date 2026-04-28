# Problem: Given a string s, find the length of the longest substring without repeating characters.

def length_of_longest_substring(s: str) -> int:
    """
    Approach: Variable-size Sliding Window.
    We use two pointers (left and right) to represent a window.
    We expand the right pointer to include characters. If a character is already
    in our window (tracked via a hash set or dictionary), we shrink the window 
    from the left until the repeating character is removed.
    
    Time: O(n) - Both left and right pointers traverse the string at most once.
    Space: O(min(n, m)) - Space needed for the hash set, where m is the character set size.
    """
    char_index_map = {}
    left = 0
    max_length = 0
    
    for right in range(len(s)):
        current_char = s[right]
        
        # If the character is already in the map AND its index is inside our current window
        if current_char in char_index_map and char_index_map[current_char] >= left:
            # Move the left pointer to the right of the duplicate's last known index
            left = char_index_map[current_char] + 1
            
        # Update the character's most recent index
        char_index_map[current_char] = right
        
        # Calculate the current window size and update max_length
        current_window_size = right - left + 1
        max_length = max(max_length, current_window_size)
        
    return max_length

# Example usage:
print(length_of_longest_substring("abcabcbb")) # Output: 3 (Substring: "abc")
print(length_of_longest_substring("bbbbb"))    # Output: 1 (Substring: "b")
print(length_of_longest_substring("pwwkew"))   # Output: 3 (Substring: "wke")
