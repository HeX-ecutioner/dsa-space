# Problem: Given a string array words, return the maximum value of length(word[i]) * length(word[j]) where the two words do not share common letters.
def maxProduct(words):
    """
    Approach: Bitmask.
    Time: O(N^2 + N * L)
    Space: O(N)
    """
    masks = [0] * len(words)
    lens = [len(w) for w in words]
    for i, word in enumerate(words):
        for char in word:
            masks[i] |= 1 << (ord(char) - ord('a'))
    res = 0
    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            if not (masks[i] & masks[j]):
                res = max(res, lens[i] * lens[j])
    return res
