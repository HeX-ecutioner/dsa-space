# Problem: You are given a 0-indexed array of strings words and a 2D array of integers queries. Return an array ans of size q, where ans[i] is the number of strings in words[l_i...r_i] that start and end with a vowel.
def vowelStrings(words, queries):
    """
    Approach: Prefix Sum.
    Time: O(N + Q)
    Space: O(N)
    """
    vowels = set("aeiou")
    prefix = [0] * (len(words) + 1)
    for i, w in enumerate(words):
        if w[0] in vowels and w[-1] in vowels:
            prefix[i + 1] = prefix[i] + 1
        else:
            prefix[i + 1] = prefix[i]
    res = []
    for l, r in queries:
        res.append(prefix[r + 1] - prefix[l])
    return res
