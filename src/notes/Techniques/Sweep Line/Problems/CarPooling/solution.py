# Problem: There is a car with capacity empty seats. You are given an array trips. Return true if it is possible to pick up and drop off all passengers for all the given trips, or false otherwise.
def carPooling(trips, capacity):
    """
    Approach: Sweep Line.
    Time: O(N log N)
    Space: O(N)
    """
    events = []
    for num_passengers, start, end in trips:
        events.append((start, num_passengers))
        events.append((end, -num_passengers))
    events.sort(key=lambda x: (x[0], x[1]))
    current_passengers = 0
    for pos, change in events:
        current_passengers += change
        if current_passengers > capacity:
            return False
    return True
