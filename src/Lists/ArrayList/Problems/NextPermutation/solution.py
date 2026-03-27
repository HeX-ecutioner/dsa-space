"""
Problem: Next Permutation
Statement: Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers. If such an arrangement is not possible, it must rearrange it as the lowest possible order (i.e., sorted in ascending order).
"""

def nextPermutation(nums):
    # Time Complexity: O(n) - At worst, we do a few linear passes.
    # Space Complexity: O(1) - Mutates the array in-place.
    
    n = len(nums)
    i = n - 2
    
    # 1. Find the first decreasing element from the right
    while i >= 0 and nums[i] >= nums[i + 1]:
        i -= 1
        
    if i >= 0:
        # 2. Find the element just larger than nums[i] from the right
        j = n - 1
        while nums[j] <= nums[i]:
            j -= 1
        # 3. Swap them
        nums[i], nums[j] = nums[j], nums[i]
        
    # 4. Reverse the remaining suffix to get the smallest possible lexicographical order
    left, right = i + 1, n - 1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1

if __name__ == "__main__":
    arr = [1, 2, 3]
    nextPermutation(arr)
    print("Next Permutation of [1, 2, 3]:", arr) # Expected: [1, 3, 2]
    
    arr2 = [3, 2, 1]
    nextPermutation(arr2)
    print("Next Permutation of [3, 2, 1]:", arr2) # Expected: [1, 2, 3]