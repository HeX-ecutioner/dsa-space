"""
Problem: Sort Colors (Dutch National Flag Problem)
Statement: Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue. We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
"""

def sortColors(nums):
    # Time Complexity: O(n) - Single pass.
    # Space Complexity: O(1) - In-place swaps.
    
    low = 0          # Pointer for the end of 0s
    mid = 0          # Pointer for iterating
    high = len(nums) - 1 # Pointer for the start of 2s
    
    while mid <= high:
        if nums[mid] == 0:
            # Swap with low pointer, move both forward
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            # Leave it in the middle, just move mid forward
            mid += 1
        else: # nums[mid] == 2
            # Swap with high pointer, move high backward
            # (Don't move mid, because the swapped number needs to be evaluated)
            nums[high], nums[mid] = nums[mid], nums[high]
            high -= 1

if __name__ == "__main__":
    nums = [2, 0, 2, 1, 1, 0]
    sortColors(nums)
    print("Sorted Colors:", nums) # Expected: [0, 0, 1, 1, 2, 2]