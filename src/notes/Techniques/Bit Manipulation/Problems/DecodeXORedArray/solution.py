# Problem: There is a hidden integer array arr that consists of n non-negative integers. It was encoded into another integer array encoded of length n - 1, such that encoded[i] = arr[i] XOR arr[i + 1].
def decode(encoded, first):
    """
    Approach: Reverse XOR.
    Time: O(N)
    Space: O(N)
    """
    res = [first]
    for e in encoded:
        res.append(res[-1] ^ e)
    return res
