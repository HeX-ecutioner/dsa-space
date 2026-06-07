class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Map to store {character : its most recent index}
        char_index_map = {}
        
        left = 0
        max_length = 0
        
        for right in range(len(s)):
            current_char = s[right]
            
            # If we've seen this character before AND its previous occurrence 
            # is inside our current sliding window
            if current_char in char_index_map and char_index_map[current_char] >= left:
                # Move the left pointer directly after the previous occurrence
                left = char_index_map[current_char] + 1
                
            # Update the most recent index of the current character
            char_index_map[current_char] = right
            
            # Calculate the length of the current valid window
            current_length = right - left + 1
            max_length = max(max_length, current_length)
            
        return max_length

# --- Example Usage ---
# sol = Solution()
# print(sol.lengthOfLongestSubstring("abcabcbb")) # Output: 3
# print(sol.lengthOfLongestSubstring("bbbbb"))    # Output: 1
# print(sol.lengthOfLongestSubstring("pwwkew"))   # Output: 3
