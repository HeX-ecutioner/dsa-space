# Problem: Given a list of daily stock prices, calculate the stock span for each day.

def stock_span(prices):
    """
    Efficiently calculates the stock span for each day using a stack.

    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    stack = []                      # stack to store indices of days
    span = [0] * len(prices)        # result array

    for i, price in enumerate(prices):
        # Pop indices of days with prices <= current price
        while stack and prices[stack[-1]] <= price:
            stack.pop()

        # If stack is empty, price is greater than all previous prices
        span[i] = i + 1 if not stack else i - stack[-1]

        # Push current day's index
        stack.append(i)

    return span

# Example usage:
prices = [100, 80, 60, 70, 60, 75, 85]
print(stock_span(prices)) # Output: [1, 1, 1, 2, 1, 4, 6]