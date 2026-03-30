"""
Problem: Implement a Trie (Prefix Tree)
Statement: Implement a Trie class with insert, search, and startsWith methods.
"""

class TrieNode:
    def __init__(self):
        # Hash map is more space efficient than a static array of size 26
        self.children = {} 
        self.is_end_of_word = False

class Trie:
    # Time Complexity: O(M) for all operations, where M is the length of the word/prefix.
    # Space Complexity: O(Total number of characters in all words).
    
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.is_end_of_word = True # Mark the end of the full string

    def search(self, word: str) -> bool:
        """Returns True only if the EXACT word is in the Trie."""
        curr = self.root
        for char in word:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return curr.is_end_of_word

    def startsWith(self, prefix: str) -> bool:
        """Returns True if ANY word in the Trie starts with the prefix."""
        curr = self.root
        for char in prefix:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return True # Doesn't matter if it's the end of a word or not

# Example usage
if __name__ == "__main__":
    trie = Trie()
    trie.insert("apple")
    
    print("Search 'apple':", trie.search("apple"))       # Expected: True
    print("Search 'app':", trie.search("app"))           # Expected: False (it's only a prefix)
    print("Starts with 'app':", trie.startsWith("app"))  # Expected: True
    
    trie.insert("app")
    print("Search 'app' (after inserting):", trie.search("app")) # Expected: True