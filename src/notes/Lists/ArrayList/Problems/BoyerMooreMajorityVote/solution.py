"""
Problem: Majority Element (Boyer-Moore Voting Algorithm)
Statement: Given an array nums of size n, return the majority element. The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.
"""

def majorityElement(nums):
    # Time Complexity: O(n) - Linear scan.
    # Space Complexity: O(1) - Constant space used.
    
    count = 0
    candidate = None
    
    for num in nums:
        # If count hits 0, we assign a new candidate
        if count == 0:
            candidate = num
            
        # If the current number is the candidate, increment, else decrement
        if num == candidate:
            count += 1
        else:
            count -= 1
            
    return candidate

if __name__ == "__main__":
    nums = [2, 2, 1, 1, 1, 2, 2]
    print("Majority Element:", majorityElement(nums)) # Expected: 2