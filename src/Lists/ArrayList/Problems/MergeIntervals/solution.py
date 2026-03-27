"""
Problem: Merge Intervals
Statement: Given an array of intervals where intervals[i] = [start_i, end_i], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.
"""

def merge(intervals):
    # Time Complexity: O(n log n) - Due to the sorting step.
    # Space Complexity: O(n) - In the worst case, no intervals merge.
    
    if not intervals:
        return []
        
    # Sort the intervals based on the starting value
    intervals.sort(key=lambda x: x[0])
    
    merged = [intervals[0]]
    
    for i in range(1, len(intervals)):
        last_added_interval = merged[-1]
        current_interval = intervals[i]
        
        # If the current interval overlaps with the last added one, merge them
        if current_interval[0] <= last_added_interval[1]:
            last_added_interval[1] = max(last_added_interval[1], current_interval[1])
        else:
            # Otherwise, add it to the list
            merged.append(current_interval)
            
    return merged

if __name__ == "__main__":
    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    print("Merged Intervals:", merge(intervals)) # Expected: [[1, 6], [8, 10], [15, 18]]