"""
Problem: Move Zeroes
Statement: Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements. MUST be done in-place.
"""

def moveZeroes(nums):
    # Time Complexity: O(n) - Single pass through the array.
    # Space Complexity: O(1) - In-place mutation.
    
    insert_pos = 0 # Points to where the next non-zero should go
    
    # 1. Shift all non-zeros to the front
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[insert_pos] = nums[i]
            insert_pos += 1
            
    # 2. Fill the rest of the array with zeros
    for i in range(insert_pos, len(nums)):
        nums[i] = 0

if __name__ == "__main__":
    arr = [0, 1, 0, 3, 12]
    moveZeroes(arr)
    print("Array after moving zeroes:", arr) # Expected: [1, 3, 12, 0, 0]