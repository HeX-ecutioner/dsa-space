"""
Problem: Suffix Trie Substring Search
Statement: Pre-process a massive text into a Suffix structure to 
search for any pattern in time proportional only to the pattern length.
"""

class TrieNode:
    def __init__(self):
        self.children = {}

class SuffixTrie:
    # Time Complexity: O(N^2) Build, O(M) Search (where M is pattern length).
    # Space Complexity: O(N^2) for the trie.

    def __init__(self, text):
        self.root = TrieNode()
        # Add all possible suffixes to the Trie
        for i in range(len(text)):
            self._insert(text[i:])

    def _insert(self, suffix):
        curr = self.root
        for char in suffix:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]

    def contains(self, pattern):
        curr = self.root
        # Traverse the trie using pattern characters
        for char in pattern:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        # If we successfully traversed the pattern, the substring exists
        return True

if __name__ == "__main__":
    massive_text = "abracadabra_dna_sequence_data"
    st = SuffixTrie(massive_text)
    
    print("Contains 'cadab'?", st.contains("cadab")) # Expected: True
    print("Contains 'xyz'?", st.contains("xyz"))     # Expected: False