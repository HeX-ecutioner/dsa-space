# Problem: There is a bookstore owner that has a store open for n minutes. Return the maximum number of customers that can be satisfied throughout the day.
def maxSatisfied(customers, grumpy, minutes):
    """
    Approach: Fixed Sliding Window.
    Time: O(N)
    Space: O(1)
    """
    l = 0
    window, max_window = 0, 0
    satisfied = 0
    for r in range(len(customers)):
        if grumpy[r]: window += customers[r]
        else: satisfied += customers[r]
        if r - l + 1 > minutes:
            if grumpy[l]: window -= customers[l]
            l += 1
        max_window = max(max_window, window)
    return satisfied + max_window
