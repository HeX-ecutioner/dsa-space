"""
Problem: Suffix Trie Concept
Statement: Demonstrate the logic of a Suffix Tree by building an uncompressed Suffix Trie. 
Note: True Suffix Trees use edge-compression and Ukkonen's O(N) algorithm, which is highly complex.
"""

class TrieNode:
    def __init__(self):
        self.children = {}
        self.indexes = [] # Store starting indexes of the suffix

class SuffixTrieConceptual:
    # Time Complexity: Build O(N^2) (Ukkonen's is O(N)), Search O(M) where M is pattern length.
    
    def __init__(self, text):
        self.root = TrieNode()
        # Build by inserting every possible suffix into the Trie
        for i in range(len(text)):
            self.insert_suffix(text[i:], i)

    def insert_suffix(self, suffix, start_idx):
        curr = self.root
        for char in suffix:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
            curr.indexes.append(start_idx)

    def search(self, pattern):
        """ Returns all starting indices where the pattern occurs in the text. """
        curr = self.root
        for char in pattern:
            if char not in curr.children:
                return [] # Pattern not found
            curr = curr.children[char]
        return curr.indexes

# Example usage
if __name__ == "__main__":
    text = "banana"
    # Suffixes: banana, anana, nana, ana, na, a
    st = SuffixTrieConceptual(text)
    
    print("Pattern 'ana' found at indices:", st.search("ana")) 
    # Expected: [1, 3] (b'ana'na, ban'ana')
    
    print("Pattern 'nan' found at indices:", st.search("nan")) 
    # Expected: [2] (ba'nan'a)