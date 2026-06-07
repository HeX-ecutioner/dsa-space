from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Map: character frequency tuple -> list of anagrams
        # defaultdict automatically creates an empty list if the key doesn't exist
        res = defaultdict(list)
        
        for s in strs:
            # Create a frequency array for the 26 lowercase English letters
            count = [0] * 26
            for char in s:
                count[ord(char) - ord('a')] += 1
                
            # Convert the list to a tuple because lists are mutable 
            # and cannot be used as dictionary keys in Python.
            # Tuples are immutable and hashable.
            res[tuple(count)].append(s)
            
        return list(res.values())

    # Alternative approach using Sorting (slightly slower: O(N * K log K))
    # def groupAnagramsSorted(self, strs: List[str]) -> List[List[str]]:
    #     res = defaultdict(list)
    #     for s in strs:
    #         # Sort the string to use as a key
    #         sorted_s = "".join(sorted(s))
    #         res[sorted_s].append(s)
    #     return list(res.values())

# --- Example Usage ---
# sol = Solution()
# print(sol.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
# Output (order may vary): [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
