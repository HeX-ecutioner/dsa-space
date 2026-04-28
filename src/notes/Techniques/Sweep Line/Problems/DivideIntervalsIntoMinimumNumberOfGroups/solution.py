# Problem: You are given a 2D integer array intervals. Divide the intervals into the minimum number of groups so that no two intervals in the same group overlap.
def minGroups(intervals):
    """
    Approach: Sweep Line (Exactly like Meeting Rooms II).
    Time: O(N log N)
    Space: O(N)
    """
    events = []
    for start, end in intervals:
        events.append((start, 1))
        events.append((end + 1, -1))
    events.sort()
    max_groups = 0
    curr_groups = 0
    for time, change in events:
        curr_groups += change
        max_groups = max(max_groups, curr_groups)
    return max_groups
