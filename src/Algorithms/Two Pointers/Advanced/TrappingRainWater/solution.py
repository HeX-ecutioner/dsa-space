# Trapping Rain Water - two pointers optimized approach
# Problem: Given heights, compute how much rainwater can be trapped.
# Approach: Maintain left_max and right_max, move the smaller side inward.
from typing import List

def trap(height: List[int]) -> int:
    """
    Two-pointer O(n) solution:
    - left, right pointers start at ends
    - track left_max and right_max
    - water trapped at current index is max(0, min(left_max, right_max) - height[idx])
    - move pointer with smaller height inward since that side limits water
    Time: O(n), Space: O(1)
    """
    if not height:
        return 0
    left, right = 0, len(height) - 1
    left_max, right_max = 0, 0
    water = 0
    while left <= right:
        if height[left] <= height[right]:
            # left side is limiting
            if height[left] >= left_max:
                left_max = height[left]
            else:
                water += left_max - height[left]
            left += 1
        else:
            # right side is limiting
            if height[right] >= right_max:
                right_max = height[right]
            else:
                water += right_max - height[right]
            right -= 1
    return water

# Example:
# trap([0,1,0,2,1,0,1,3,2,1,2,1]) -> 6
