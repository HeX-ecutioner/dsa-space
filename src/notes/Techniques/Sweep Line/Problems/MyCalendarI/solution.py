# Problem: You are implementing a program to use as your calendar. We can add a new event if adding the event will not cause a double booking.
# A double booking happens when two events have some non-empty intersection (i.e., some moment is common to both events).
# The event can be represented as an interval [start, end) that represents the time such that start <= t < end.

class MyCalendar:
    """
    Approach: Sweep Line (or Binary Search Tree).
    For a single add, checking overlaps against a sorted list of intervals takes O(N).
    In python, we can keep the intervals sorted and check the insertion point.
    
    If we use a pure Sweep Line approach, we can insert the new interval and then check 
    if any point in time has > 1 active event. Since we want to stop BEFORE inserting an 
    invalid event, we just check if the new interval overlaps with any existing ones.
    
    Time: O(N) per book query (since we keep an array of size N). O(N^2) total for N queries.
    Space: O(N) to store the events.
    """
    def __init__(self):
        # We will keep the calendar sorted by start times.
        self.calendar = []

    def book(self, start: int, end: int) -> bool:
        # Check for overlaps with existing events
        for s, e in self.calendar:
            # Two intervals [s1, e1) and [s2, e2) overlap if:
            # s1 < e2 AND s2 < e1
            if start < e and s < end:
                return False
                
        # If no overlap, add it
        self.calendar.append((start, end))
        
        # Sort it to maintain chronological order
        # (Alternatively, we could use bisect module for O(log N) insertion, but list 
        # shifting still takes O(N) in Python)
        self.calendar.sort()
        return True

# Example usage:
cal = MyCalendar()
print(cal.book(10, 20)) # Output: True (Event [10, 20) added)
print(cal.book(15, 25)) # Output: False (Overlaps with [10, 20))
print(cal.book(20, 30)) # Output: True (Event [20, 30) added, touching edges [10, 20) and [20, 30) is fine)
