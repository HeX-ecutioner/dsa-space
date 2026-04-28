# Problem: You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.
# Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).
from typing import List

def insert(intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    """
    Approach: Sweep Line / Linear Scan.
    Since the intervals are already sorted and non-overlapping, we don't need to 
    sort them from scratch (which saves us O(N log N) time).
    We can sweep through the intervals and categorize them into three parts:
    1. Intervals that end strictly before the newInterval starts (No overlap, add to result).
    2. Intervals that overlap with the newInterval (Merge them into the newInterval).
    3. Intervals that start strictly after the newInterval ends (No overlap, add to result).
    
    Time: O(N) - Single pass over the intervals.
    Space: O(N) - To store the newly formed list of intervals.
    """
    result = []
    i = 0
    n = len(intervals)
    
    # 1. Add all intervals that end before the newInterval starts
    while i < n and intervals[i][1] < newInterval[0]:
        result.append(intervals[i])
        i += 1
        
    # 2. Merge all intervals that overlap with the newInterval
    # They overlap as long as the current interval starts before the newInterval ends
    while i < n and intervals[i][0] <= newInterval[1]:
        # Expand the newInterval to cover the overlapping interval
        newInterval[0] = min(newInterval[0], intervals[i][0])
        newInterval[1] = max(newInterval[1], intervals[i][1])
        i += 1
    # Add the fully merged newInterval to the result
    result.append(newInterval)
    
    # 3. Add all remaining intervals that start after the newInterval ends
    while i < n:
        result.append(intervals[i])
        i += 1
        
    return result

# Example usage:
print(insert([[1,3],[6,9]], [2,5])) # Output: [[1,5],[6,9]]
print(insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8])) # Output: [[1,2],[3,10],[12,16]]
