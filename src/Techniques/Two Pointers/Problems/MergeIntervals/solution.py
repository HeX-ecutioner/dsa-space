from typing import List

def merge_intervals(intervals: List[List[int]]) -> List[List[int]]:
    """
    Sort intervals by start then iterate merging overlapping ones.
    Approach:
    - Sort by start
    - Keep current interval; if next.start <= current.end -> merge
    - else output current and move to next
    Time: O(n log n) due to sort
    """
    if not intervals:
        return []
    intervals.sort(key=lambda x: x[0])
    merged = []
    cur_start, cur_end = intervals[0]
    for s, e in intervals[1:]:
        if s <= cur_end:
            cur_end = max(cur_end, e)
        else:
            merged.append([cur_start, cur_end])
            cur_start, cur_end = s, e
    merged.append([cur_start, cur_end])
    return merged

# Example usage:
if __name__ == "__main__":
    intervals = [[1,3],[2,4],[5,7],[6,8]]
    print(merge_intervals(intervals))  # Output: [[1,4],[5,8]]