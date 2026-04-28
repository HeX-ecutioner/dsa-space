# Problem: You are given two lists of closed intervals, firstList and secondList, where each list of intervals is pairwise disjoint and in sorted order. Return the intersection of these two interval lists.
def intervalIntersection(firstList, secondList):
    """
    Approach: Two Pointers / Sweep Line intersection.
    Time: O(M + N)
    Space: O(M + N)
    """
    i, j = 0, 0
    res = []
    while i < len(firstList) and j < len(secondList):
        start = max(firstList[i][0], secondList[j][0])
        end = min(firstList[i][1], secondList[j][1])
        if start <= end:
            res.append([start, end])
        if firstList[i][1] < secondList[j][1]:
            i += 1
        else:
            j += 1
    return res
