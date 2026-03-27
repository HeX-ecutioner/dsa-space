"""
Problem: Container With Most Water
Statement: You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]). Find two lines that together with the x-axis form a container, such that the container contains the most water.
"""

def maxArea(height):
    # Time Complexity: O(n) - We check the array exactly once.
    # Space Complexity: O(1) - Two pointers only.
    
    left = 0
    right = len(height) - 1
    max_water = 0
    
    while left < right:
        # Calculate area: width * min(heights)
        width = right - left
        current_water = min(height[left], height[right]) * width
        max_water = max(max_water, current_water)
        
        # Move the pointer pointing to the shorter line, as moving the 
        # taller line cannot possibly increase the area.
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
            
    return max_water

if __name__ == "__main__":
    heights = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print("Max Water Area:", maxArea(heights)) # Expected: 49