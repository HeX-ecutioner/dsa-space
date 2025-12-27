# Container With Most Water - two pointers from both ends
# Problem: Given heights array, find max area formed by two vertical lines.
# Approach: two pointers left and right; move the pointer at smaller height inward.
from typing import List

def max_area(height: List[int]) -> int:
    """
    Compute max area by using two-pointer technique:
    - Start left=0, right=n-1.
    - Area = min(height[left],height[right]) * (right-left)
    - Move the pointer with smaller height inward because moving the taller one cannot increase min height.
    Time: O(n), Space: O(1)
    """
    left, right = 0, len(height) - 1
    best = 0
    while left < right:
        h = min(height[left], height[right])
        area = h * (right - left)
        best = max(best, area)
        # move the pointer with smaller height to try to find larger area
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return best

# Example:
# max_area([1,8,6,2,5,4,8,3,7]) -> 49
