# Problem: You are implementing a program to use as your calendar. You can add a new event if adding the event will not cause a triple booking.
class MyCalendarTwo:
    """
    Approach: Sweep Line (Array of intervals).
    Time: O(N)
    Space: O(N)
    """
    def __init__(self):
        self.overlaps = []
        self.calendar = []

    def book(self, start: int, end: int) -> bool:
        for i, j in self.overlaps:
            if start < j and end > i:
                return False
        for i, j in self.calendar:
            if start < j and end > i:
                self.overlaps.append((max(start, i), min(end, j)))
        self.calendar.append((start, end))
        return True
