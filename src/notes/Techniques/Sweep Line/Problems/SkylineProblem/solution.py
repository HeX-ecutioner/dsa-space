# Problem: A city's skyline is the outer contour of the silhouette formed by all the buildings in that city. Given the locations and heights of all the buildings, return the skyline formed by these buildings collectively.
import heapq
def getSkyline(buildings):
    """
    Approach: Sweep Line with Max-Heap.
    Time: O(N log N)
    Space: O(N)
    """
    events = []
    for l, r, h in buildings:
        events.append((l, -h, r)) 
        events.append((r, 0, 0))  
    events.sort()
    res = [[0, 0]]
    live = [(0, float('inf'))] 
    for pos, negH, r in events:
        while live[0][1] <= pos:
            heapq.heappop(live)
        if negH != 0:
            heapq.heappush(live, (negH, r))
        if res[-1][1] != -live[0][0]:
            res.append([pos, -live[0][0]])
    return res[1:]
