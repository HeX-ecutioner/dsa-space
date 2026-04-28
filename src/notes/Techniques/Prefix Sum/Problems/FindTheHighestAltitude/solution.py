# Problem: There is a biker going on a road trip. The trip consists of n + 1 points at different altitudes. The biker starts his trip on point 0 with altitude equal 0. You are given an integer array gain of length n where gain[i] is the net gain in altitude between points i and i + 1. Return the highest altitude of a point.
def largestAltitude(gain):
    """
    Approach: Prefix Sum.
    Time: O(N)
    Space: O(1)
    """
    current_alt = 0
    max_alt = 0
    for g in gain:
        current_alt += g
        max_alt = max(max_alt, current_alt)
    return max_alt
