"""
Problem: Rotate Array
Statement: Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
"""

def rotate(nums, k):
    # Time Complexity: O(n) - Elements are reversed a total of 3 times.
    # Space Complexity: O(1) - Done entirely in-place.
    
    k = k % len(nums) # Handle cases where k > len(nums)
    
    def reverse(start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
            
    # 1. Reverse the entire array
    reverse(0, len(nums) - 1)
    
    # 2. Reverse the first k elements
    reverse(0, k - 1)
    
    # 3. Reverse the rest of the array
    reverse(k, len(nums) - 1)

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7]
    rotate(arr, 3)
    print("Rotated Array:", arr) # Expected: [5, 6, 7, 1, 2, 3, 4]