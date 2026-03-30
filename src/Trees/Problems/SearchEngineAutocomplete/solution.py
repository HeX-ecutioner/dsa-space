"""
Problem: Design Search Autocomplete System (Simplified)
Statement: Given a dictionary of words, return all words that start with a given prefix.
"""

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
        self.word = "" # Store the full word at the leaf for easy retrieval

class AutocompleteSystem:
    # Time Complexity: Insert O(M), Autocomplete O(M + K) where M is prefix length and K is number of matching nodes.
    # Space Complexity: O(Total characters in dataset)

    def __init__(self, dictionary):
        self.root = TrieNode()
        for word in dictionary:
            self._insert(word)

    def _insert(self, word):
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.is_word = True
        curr.word = word

    def get_words_with_prefix(self, prefix):
        curr = self.root
        # 1. Traverse to the end of the prefix
        for char in prefix:
            if char not in curr.children:
                return [] # Prefix doesn't exist
            curr = curr.children[char]
            
        # 2. Run DFS from this node to collect all valid words
        results = []
        self._dfs(curr, results)
        return results

    def _dfs(self, node, results):
        if node.is_word:
            results.append(node.word)
        for child_node in node.children.values():
            self._dfs(child_node, results)

# Example usage
if __name__ == "__main__":
    dictionary = ["dog", "dark", "cat", "door", "dodge", "dentist"]
    search_engine = AutocompleteSystem(dictionary)
    
    print("Autocomplete 'do':", search_engine.get_words_with_prefix("do"))
    # Expected: ['dog', 'door', 'dodge'] (Order may vary based on hash map)
    
    print("Autocomplete 'da':", search_engine.get_words_with_prefix("da"))
    # Expected: ['dark']