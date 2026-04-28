# Problem: You are implementing a program to use as your calendar. You can add a new event and return the maximum k-booking.
from sortedcontainers import SortedDict
class MyCalendarThree:
    """
    Approach: Sweep Line using TreeMap (SortedDict).
    Time: O(N) per query
    Space: O(N)
    """
    def __init__(self):
        self.timeline = SortedDict()

    def book(self, start: int, end: int) -> int:
        self.timeline[start] = self.timeline.get(start, 0) + 1
        self.timeline[end] = self.timeline.get(end, 0) - 1
        active = max_active = 0
        for v in self.timeline.values():
            active += v
            if active > max_active:
                max_active = active
        return max_active
