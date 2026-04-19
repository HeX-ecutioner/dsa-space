def rabin_karp(text: str, pattern: str, base=256, mod=101) -> list:
    """
    Rabin-Karp algorithm for pattern matching using rolling hash.
    
    Args:
        text: The text to search in
        pattern: The pattern to find
        base: Base for hash calculation (default: 256 for ASCII)
        mod: Prime modulus for hash (default: 101)
    
    Returns:
        List of starting indices where pattern is found in text
    """
    n, m = len(text), len(pattern)
    h = pow(base, m - 1, mod) # Precompute base^(m-1) mod for rolling hash update
    p_hash = t_hash = 0
    matches = []
    # Calculate hash of pattern and first window of text
    for i in range(m):
        p_hash = (base * p_hash + ord(pattern[i])) % mod
        t_hash = (base * t_hash + ord(text[i])) % mod
    # Slide the window through text
    for i in range(n - m + 1):
        # Hash match found, verify actual characters
        if p_hash == t_hash:
            if text[i:i + m] == pattern:
                matches.append(i)
        # Calculate hash of next window using rolling hash
        if i < n - m:
            t_hash = (base * (t_hash - ord(text[i]) * h) + ord(text[i + m])) % mod
            t_hash = (t_hash + mod) % mod
    return matches

# Example usage:
if __name__ == "__main__":
    text = "ABCCDDEFFGHHIJ"
    pattern = "DDEF"
    result = rabin_karp(text, pattern)
    print(f"Pattern '{pattern}' found at indices: {result}") # Output: Pattern 'DDEF' found at indices: [4]