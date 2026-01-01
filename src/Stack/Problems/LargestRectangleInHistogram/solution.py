""" Problem: Given an array of integers heights representing the histogram's bar height where the width of each bar is 1,
return the area of the largest rectangle in the histogram"""

def largest_rectangle(heights):
    """
    Given a list of bar heights in a histogram (width = 1), return the area of the largest rectangle.

    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    stack = [] # stack to store indices
    max_area = 0

    # Append a sentinel value to flush the stack at the end
    heights.append(0)

    for i, h in enumerate(heights):
        # Resolve all bars taller than current bar
        while stack and heights[stack[-1]] > h:
            height = heights[stack.pop()]
            width = i if not stack else i - stack[-1] - 1 # Width calculation
            max_area = max(max_area, height * width)

        stack.append(i)

    heights.pop()  # remove sentinel to avoid side effects
    return max_area

# Example usage:
heights = [2, 1, 5, 6, 2, 3]
print(largest_rectangle(heights)) # Output: 10