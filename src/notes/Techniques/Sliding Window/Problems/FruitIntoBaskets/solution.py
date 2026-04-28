# Problem: You are visiting a farm that has a single row of fruit trees arranged from left to right.
# You have two baskets, and each basket can hold only a single type of fruit. 
# You want to collect as much fruit as possible. Return the maximum number of fruits you can pick.
# This translates to: Find the longest contiguous subarray containing at most 2 distinct elements.
from typing import List

def total_fruit(fruits: List[int]) -> int:
    """
    Approach: Variable-size Sliding Window.
    This problem is exactly "Longest Substring with At Most Two Distinct Characters".
    We use a hash map to keep track of the types of fruits and their counts in the current window.
    When the number of distinct fruit types in our hash map exceeds 2, we shrink the window
    from the left until we have only 2 distinct types again.
    
    Time: O(n) - We traverse the array with two pointers.
    Space: O(1) - The hash map will store at most 3 key-value pairs at any time.
    """
    fruit_counts = {}
    left = 0
    max_fruits = 0
    
    for right in range(len(fruits)):
        current_fruit = fruits[right]
        fruit_counts[current_fruit] = fruit_counts.get(current_fruit, 0) + 1
        
        # If we have more than 2 types of fruits, shrink the window
        while len(fruit_counts) > 2:
            left_fruit = fruits[left]
            fruit_counts[left_fruit] -= 1
            
            # If a fruit type reaches 0 count, remove it from the map completely
            if fruit_counts[left_fruit] == 0:
                del fruit_counts[left_fruit]
            left += 1
            
        # Update the max fruits collected (the size of the valid window)
        max_fruits = max(max_fruits, right - left + 1)
        
    return max_fruits

# Example usage:
print(total_fruit([1,2,1]))     # Output: 3 (Basket gets [1,2,1])
print(total_fruit([0,1,2,2]))   # Output: 3 (Basket gets [1,2,2])
print(total_fruit([1,2,3,2,2])) # Output: 4 (Basket gets [2,3,2,2])
