# Problem: There are n flights. You are given an array of flight bookings bookings, where bookings[i] = [firsti, lasti, seatsi]. Return an array answer of length n, where answer[i] is the total number of seats reserved for flight i.
def corpFlightBookings(bookings, n):
    """
    Approach: Difference Array / Prefix Sum.
    Time: O(N)
    Space: O(N)
    """
    diff = [0] * (n + 1)
    for start, end, seats in bookings:
        diff[start - 1] += seats
        diff[end] -= seats
    res = []
    current = 0
    for i in range(n):
        current += diff[i]
        res.append(current)
    return res
