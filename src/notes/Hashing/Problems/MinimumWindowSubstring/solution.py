class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""
        
        # Hash map to track what we need
        countT = {}
        for char in t:
            countT[char] = countT.get(char, 0) + 1
            
        # Hash map to track what we currently have in our window
        window = {}
        
        # 'have' is the number of unique characters whose frequency requirement is met
        # 'need' is the total number of unique characters required
        have, need = 0, len(countT)
        
        res = [-1, -1]
        resLen = float("infinity")
        left = 0
        
        for right in range(len(s)):
            char = s[right]
            window[char] = window.get(char, 0) + 1
            
            # If the current character is in 't' and we've reached the exact required frequency
            if char in countT and window[char] == countT[char]:
                have += 1
                
            # While the window is valid (we have all necessary characters)
            while have == need:
                # Update our result if this window is smaller than the previous minimum
                if (right - left + 1) < resLen:
                    res = [left, right]
                    resLen = right - left + 1
                
                # Pop the leftmost character from our window to try and shrink it
                left_char = s[left]
                window[left_char] -= 1
                
                # If removing the left character broke our requirement
                if left_char in countT and window[left_char] < countT[left_char]:
                    have -= 1
                    
                left += 1
                
        left_idx, right_idx = res
        # If we never found a valid window, return ""
        return s[left_idx : right_idx + 1] if resLen != float("infinity") else ""

# --- Example Usage ---
# sol = Solution()
# print(sol.minWindow("ADOBECODEBANC", "ABC")) # Output: "BANC"
# print(sol.minWindow("a", "a"))               # Output: "a"
# print(sol.minWindow("a", "aa"))              # Output: ""
