class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # If lengths are different, they can't be anagrams
        if len(s) != len(t):
            return False
        
        # Array of size 26 to act as a hash map for character frequencies
        # (Assuming inputs are only lowercase English letters)
        counts = [0] * 26
        
        # Build the frequency map
        for i in range(len(s)):
            counts[ord(s[i]) - ord('a')] += 1
            counts[ord(t[i]) - ord('a')] -= 1
            
        # Check if all frequencies are zero
        for count in counts:
            if count != 0:
                return False
                
        return True

    # Alternative Pythonic approach using Hash Maps (Counter)
    # import collections
    # def isAnagramCounter(self, s: str, t: str) -> bool:
    #     return collections.Counter(s) == collections.Counter(t)

# --- Example Usage ---
# sol = Solution()
# print(sol.isAnagram("anagram", "nagaram")) # Output: True
# print(sol.isAnagram("rat", "car"))         # Output: False
