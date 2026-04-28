# Problem: Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
# You must write an algorithm that runs in O(n) time and without using the division operation.
from typing import List

def product_except_self(nums: List[int]) -> List[int]:
    """
    Approach: Prefix and Suffix Products (Prefix Sum Variant).
    Since we cannot use division, the product of the array EXCEPT `nums[i]` is exactly:
    (Product of all elements to the LEFT of i) * (Product of all elements to the RIGHT of i)
    
    We can use a variation of the Prefix Sum technique to compute this efficiently.
    1. First, we compute the "prefix product" for each element and store it in our answer array.
    2. Then, we traverse backwards, keeping a running "suffix product", and multiply it 
       with the previously stored prefix product.
       
    Time: O(n) - Two passes over the array.
    Space: O(1) extra space (excluding the output array) as required by the problem's strict definition.
    """
    n = len(nums)
    answer = [1] * n
    
    # Step 1: Calculate prefix products
    # answer[i] will hold the product of all elements to the LEFT of i
    prefix = 1
    for i in range(n):
        answer[i] = prefix
        prefix *= nums[i]
        
    # Step 2: Calculate suffix products and multiply with prefix products
    # We maintain a running suffix product and multiply it into our answer array
    suffix = 1
    for i in range(n - 1, -1, -1):
        answer[i] *= suffix
        suffix *= nums[i]
        
    return answer

# Example usage:
print(product_except_self([1,2,3,4]))    # Output: [24,12,8,6]
print(product_except_self([-1,1,0,-3,3]))# Output: [0,0,9,0,0]
