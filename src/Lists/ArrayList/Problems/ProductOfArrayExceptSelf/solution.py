"""
Problem: Product of Array Except Self
Statement: Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i]. You must write an algorithm that runs in O(n) time and without using the division operation.
"""

def productExceptSelf(nums):
    # Time Complexity: O(n) - Two passes over the array.
    # Space Complexity: O(1) extra space (excluding the output array).
    
    n = len(nums)
    res = [1] * n
    
    # 1. Calculate running prefix products (left to right)
    prefix = 1
    for i in range(n):
        res[i] = prefix
        prefix *= nums[i]
        
    # 2. Calculate running suffix products (right to left) and multiply
    postfix = 1
    for i in range(n - 1, -1, -1):
        res[i] *= postfix
        postfix *= nums[i]
        
    return res

if __name__ == "__main__":
    nums = [1, 2, 3, 4]
    print("Product Except Self:", productExceptSelf(nums)) # Expected: [24, 12, 8, 6]