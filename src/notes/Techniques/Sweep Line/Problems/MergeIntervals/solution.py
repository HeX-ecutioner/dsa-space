# Problem: Given an array of intervals where intervals[i] = [start_i, end_i], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.
from typing import List

def merge_intervals(intervals: List[List[int]]) -> List[List[int]]:
    """
    Approach: Sweep Line / Sorting.
    This is closely related to the Sweep Line pattern. We first sort the intervals 
    based on their starting times.
    Then, we sweep through the intervals from left to right.
    We maintain the 'current' interval we are trying to merge others into.
    If the next interval's start time is less than or equal to our current's end time,
    it overlaps! So we extend our current interval's end to the maximum of both.
    Otherwise, it doesn't overlap, so we add our current interval to the answer 
    and start a new current interval.
    
    Time: O(N log N) - Sorting the intervals dominates the time complexity.
    Space: O(N) - For the output array (or O(1) if modifying in-place, but sorting might take O(N) or O(log N) depending on language).
    """
    if not intervals:
        return []
        
    # Sort intervals based on start time
    intervals.sort(key=lambda x: x[0])
    
    merged = [intervals[0]]
    
    for current_start, current_end in intervals[1:]:
        # Get the last added interval in our merged list
        last_added_start, last_added_end = merged[-1]
        
        # If the current interval overlaps with the last added one, merge them
        if current_start <= last_added_end:
            merged[-1][1] = max(last_added_end, current_end)
        else:
            # They don't overlap, add the current one to the merged list
            merged.append([current_start, current_end])
            
    return merged

# Example usage:
print(merge_intervals([[1,3],[2,6],[8,10],[15,18]])) # Output: [[1,6],[8,10],[15,18]]
print(merge_intervals([[1,4],[4,5]]))               # Output: [[1,5]]
