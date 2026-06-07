class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(" ")
        
        # If the number of characters in pattern doesn't match the number of words
        if len(pattern) != len(words):
            return False
            
        charToWord = {}
        wordToChar = {}
        
        for c, w in zip(pattern, words):
            # Check character -> word mapping
            if c in charToWord:
                if charToWord[c] != w:
                    return False
            else:
                charToWord[c] = w
                
            # Check word -> character mapping
            if w in wordToChar:
                if wordToChar[w] != c:
                    return False
            else:
                wordToChar[w] = c
                
        return True

# --- Example Usage ---
# sol = Solution()
# print(sol.wordPattern("abba", "dog cat cat dog"))  # Output: True
# print(sol.wordPattern("abba", "dog cat cat fish")) # Output: False
