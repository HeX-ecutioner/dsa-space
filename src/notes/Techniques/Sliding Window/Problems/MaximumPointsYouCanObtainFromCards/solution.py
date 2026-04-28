# Problem: There are several cards arranged in a row, and each card has an associated number of points. You must take exactly k cards from either the beginning or the end. Return the maximum score.
def maxScore(cardPoints, k):
    """
    Approach: Fixed Sliding Window (Min Subarray Sum of size N - K).
    Time: O(N)
    Space: O(1)
    """
    l, r = 0, len(cardPoints) - k
    total = sum(cardPoints[r:])
    res = total
    while r < len(cardPoints):
        total += (cardPoints[l] - cardPoints[r])
        res = max(res, total)
        l += 1
        r += 1
    return res
