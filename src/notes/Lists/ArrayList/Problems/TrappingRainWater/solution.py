"""
Problem: Trapping Rain Water
Statement: Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.
"""

def trap(height):
    # Time Complexity: O(n) - Single pass using two pointers.
    # Space Complexity: O(1) - No extra arrays used.
    
    if not height: return 0
    
    left, right = 0, len(height) - 1
    left_max, right_max = height[left], height[right]
    water_trapped = 0
    
    while left < right:
        # We always process the side with the smaller maximum bound
        if left_max < right_max:
            left += 1
            left_max = max(left_max, height[left])
            water_trapped += left_max - height[left]
        else:
            right -= 1
            right_max = max(right_max, height[right])
            water_trapped += right_max - height[right]
            
    return water_trapped

if __name__ == "__main__":
    heights = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    print("Trapped Water:", trap(heights)) # Expected: 6