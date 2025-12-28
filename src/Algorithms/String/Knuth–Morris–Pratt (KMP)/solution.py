def build_lps(pattern: str) -> list:
    """Build the Longest Proper Prefix which is also Suffix (LPS) array."""
    lps = [0] * len(pattern)
    length = 0  # Length of the previous longest prefix suffix
    i = 1
    while i < len(pattern):
        # Characters match, extend the current LPS
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            # Mismatch: backtrack using the LPS array
            if length != 0:
                length = lps[length - 1]
            else:
                # No prefix suffix found
                lps[i] = 0
                i += 1
    return lps

def kmp_search(text: str, pattern: str) -> list:
    """Search for all occurrences of pattern in text using KMP algorithm."""
    lps = build_lps(pattern)
    i = j = 0  # i for text, j for pattern
    matches = []
    while i < len(text):
        # Characters match, move both pointers
        if text[i] == pattern[j]:
            i += 1
            j += 1
        # Pattern found
        if j == len(pattern):
            matches.append(i - j)
            j = lps[j - 1]  # Look for next match
        # Mismatch detected
        elif i < len(text) and text[i] != pattern[j]:
            # Use LPS to avoid redundant comparisons
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return matches

# Example usage:
if __name__ == "__main__":
    text = "ababcabcabababd"
    pattern = "ababd"
    result = kmp_search(text, pattern)
    print(f"Pattern found at indices: {result}") # Output: Pattern found at indices: [10]