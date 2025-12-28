def naive_search(text: str, pattern: str) -> list:
    """
    Returns all starting indices where pattern occurs in text.
    Time Complexity: O(n * m)
    Space Complexity: O(k) where k is the number of matches
    """
    n, m = len(text), len(pattern)
    matches = []

    # Iterate through each possible starting position
    for i in range(n - m + 1):
        j = 0
        # Compare pattern with text substring starting at position i
        while j < m and text[i + j] == pattern[j]:
            j += 1
        # If entire pattern matched, record the starting index
        if j == m:
            matches.append(i)
    return matches

# Example usage:
if __name__ == "__main__":
    text = "ABABDABACDABABCABAB"
    pattern = "ABABCABAB"
    result = naive_search(text, pattern)
    print(f"Pattern '{pattern}' found at indices: {result}") # Output: Pattern 'ABABCABAB' found at indices: [10]
    
    text2 = "aaaa"
    pattern2 = "aa"
    result2 = naive_search(text2, pattern2)
    print(f"Pattern '{pattern2}' found at indices: {result2}") # Output: Pattern 'aa' found at indices: [0, 1, 2]