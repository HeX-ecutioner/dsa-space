def manacher(s: str) -> str:
    # Transform string: add '#' between characters and sentinels '^' and '$'
    # This handles even-length palindromes uniformly
    t = '#'.join('^{}$'.format(s))
    p = [0] * len(t) # p[i] = length of palindrome centered at i
    center = right = 0 # center of rightmost palindrome found so far = right boundary of rightmost palindrome

    for i in range(1, len(t) - 1):
        mirror = 2 * center - i # mirror position of i with respect to center
        
        if i < right:
            p[i] = min(right - i, p[mirror])

        while t[i + p[i] + 1] == t[i - p[i] - 1]:
            p[i] += 1

        # Update center and right if palindrome extends further
        if i + p[i] > right:
            center, right = i, i + p[i]


    max_len = max(p) # Find the longest palindrome
    idx = p.index(max_len)
    start = (idx - max_len) // 2
    return s[start:start + max_len]


# Example usage:
if __name__ == "__main__":
    print(manacher("babad"))        # Output: "bab"
    print(manacher("cbbd"))         # Output: "bb"
    print(manacher("racecar"))      # Output: "racecar"
    print(manacher("a"))            # Output: "a"
    print(manacher("ac"))           # Output: "a"