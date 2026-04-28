# Problem: Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.
from typing import List

def min_meeting_rooms(intervals: List[List[int]]) -> int:
    """
    Approach: Sweep Line Technique.
    Instead of checking how intervals overlap with each other directly, we can
    break each interval down into two events:
    1. A meeting starts (we need a room) -> Add +1 to our active room count.
    2. A meeting ends (a room is freed) -> Subtract -1 from our active room count.
    
    We collect all these events, sort them by time, and 'sweep' a line across time.
    At any point in time, the sum of active events is the number of rooms in use.
    The maximum rooms in use at any time is our answer.
    
    Time: O(N log N) - Because we must sort the events. N is the number of intervals.
    Space: O(N) - To store the 2*N events.
    """
    if not intervals:
        return 0
        
    events = []
    for start, end in intervals:
        # We use +1 for start, -1 for end
        events.append((start, 1))
        events.append((end, -1))
        
    # Sort events.
    # IMPORTANT: If a meeting ends at the exact same time another starts,
    # we should process the end event FIRST so we can reuse the room.
    # Because -1 < 1, Python's default tuple sorting handles this perfectly!
    events.sort()
    
    max_rooms = 0
    current_rooms = 0
    
    # Sweep line across all events
    for time, event_type in events:
        current_rooms += event_type
        max_rooms = max(max_rooms, current_rooms)
        
    return max_rooms

# Example usage:
print(min_meeting_rooms([[0, 30], [5, 10], [15, 20]])) # Output: 2
print(min_meeting_rooms([[7, 10], [2, 4]]))            # Output: 1
