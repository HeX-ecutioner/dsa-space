class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # If lengths don't match, they can't be isomorphic
        if len(s) != len(t):
            return False
            
        mapST, mapTS = {}, {}

        for i in range(len(s)):
            charS, charT = s[i], t[i]
            
            # Check if mapping already exists from S to T
            if charS in mapST:
                if mapST[charS] != charT:
                    return False
            else:
                mapST[charS] = charT
                
            # Check if mapping already exists from T to S
            if charT in mapTS:
                if mapTS[charT] != charS:
                    return False
            else:
                mapTS[charT] = charS
                
        return True

    # Alternative Pythonic approach using zip
    # def isIsomorphicZip(self, s: str, t: str) -> bool:
    #     # zip pairs elements, set removes duplicates. 
    #     # If lengths of sets are equal to length of zipped set, it's a 1-to-1 mapping.
    #     return len(set(s)) == len(set(t)) == len(set(zip(s, t)))

# --- Example Usage ---
# sol = Solution()
# print(sol.isIsomorphic("egg", "add")) # Output: True
# print(sol.isIsomorphic("foo", "bar")) # Output: False
