"""
Problem: Remove Duplicates from Sorted Array
Statement: Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. Return the number of unique elements.
"""

def removeDuplicates(nums):
    # Time Complexity: O(n) - Single pass through the array.
    # Space Complexity: O(1) - In-place manipulation.
    
    if not nums: return 0
    
    # insert_pos tracks where the NEXT unique element should be placed
    insert_pos = 1 
    
    for i in range(1, len(nums)):
        # If the current element is different from the previous one, it's unique
        if nums[i] != nums[i - 1]:
            nums[insert_pos] = nums[i]
            insert_pos += 1
            
    # The array is mutated in place, but we return the count of unique elements
    return insert_pos

if __name__ == "__main__":
    arr = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    k = removeDuplicates(arr)
    print(f"Unique count: {k}") # Expected: 5
    print(f"Modified Array (first {k} elements): {arr[:k]}") # Expected: [0, 1, 2, 3, 4]