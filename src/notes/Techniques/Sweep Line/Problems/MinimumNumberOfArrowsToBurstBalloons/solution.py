# Problem: There are some spherical balloons taped onto a flat wall. An arrow can be shot up exactly vertically. Find the minimum number of arrows that must be shot to burst all balloons.
def findMinArrowShots(points):
    """
    Approach: Sweep Line / Greedy Interval Scheduling.
    Time: O(N log N)
    Space: O(1)
    """
    if not points: return 0
    points.sort(key=lambda x: x[1])
    arrows = 1
    last_end = points[0][1]
    for x_start, x_end in points:
        if x_start > last_end:
            arrows += 1
            last_end = x_end
    return arrows
