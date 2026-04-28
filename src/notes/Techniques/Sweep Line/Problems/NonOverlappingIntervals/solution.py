# Problem: Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.
from typing import List

def erase_overlap_intervals(intervals: List[List[int]]) -> int:
    """
    Approach: Sweep Line / Greedy Scheduling.
    This problem is equivalent to finding the maximum number of non-overlapping intervals 
    (Activity Selection Problem). If we find the max non-overlapping ones, the answer is just:
    Total intervals - Max non-overlapping intervals.
    
    To greedily maximize the number of non-overlapping intervals, we should always pick 
    the interval that ENDS earliest. Why? Because the earlier an interval ends, the more 
    room it leaves for subsequent intervals.
    
    We sort the intervals by their END times, then sweep through them to count how many 
    we must remove when they conflict with our earliest-ending chosen interval.
    
    Time: O(N log N) - We must sort the intervals.
    Space: O(1) - Assuming in-place sorting and constant extra variables.
    """
    if not intervals:
        return 0
        
    # Sort intervals by their END time
    intervals.sort(key=lambda x: x[1])
    
    removed_count = 0
    # Keep track of the end time of the last safely added interval
    last_end = intervals[0][1]
    
    for i in range(1, len(intervals)):
        current_start, current_end = intervals[i]
        
        # If the current interval overlaps with the last added one
        if current_start < last_end:
            # We must remove it
            removed_count += 1
        else:
            # No overlap! We keep this one, and update our tracking end time
            last_end = current_end
            
    return removed_count

# Example usage:
print(erase_overlap_intervals([[1,2],[2,3],[3,4],[1,3]])) # Output: 1 (Remove [1,3])
print(erase_overlap_intervals([[1,2],[1,2],[1,2]]))       # Output: 2
print(erase_overlap_intervals([[1,2],[2,3]]))             # Output: 0
