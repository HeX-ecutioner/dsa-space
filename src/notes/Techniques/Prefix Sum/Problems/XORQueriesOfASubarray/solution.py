# Problem: You are given an array arr of positive integers. You are also given the array queries where queries[i] = [lefti, righti]. For each query i compute the XOR of elements from lefti to righti.
def xorQueries(arr, queries):
    """
    Approach: Prefix XOR.
    Time: O(N + Q)
    Space: O(N)
    """
    prefix = [0] * (len(arr) + 1)
    for i in range(len(arr)):
        prefix[i + 1] = prefix[i] ^ arr[i]
    return [prefix[r + 1] ^ prefix[l] for l, r in queries]
