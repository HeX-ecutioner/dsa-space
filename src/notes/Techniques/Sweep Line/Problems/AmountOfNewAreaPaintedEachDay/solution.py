# Problem: There is a long and thin painting that can be represented by a number line. You are given a 0-indexed 2D integer array paint of length n, where paint[i] = [starti, endi]. Return an array work of length n, where work[i] is the amount of new area that you painted on the ith day.
def amountPainted(paint):
    """
    Approach: Sweep Line / Ordered Set (Jump Intervals).
    Time: O(N + Max_Pos)
    Space: O(Max_Pos)
    """
    jump = {}
    res = []
    for start, end in paint:
        work = 0
        curr = start
        while curr < end:
            if curr in jump:
                next_curr = jump[curr]
                jump[curr] = max(jump[curr], end)
                curr = next_curr
            else:
                jump[curr] = end
                work += 1
                curr += 1
        res.append(work)
    return res
