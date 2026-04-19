from typing import List, Callable

def partition_by_condition(nums: List[int], cond: Callable[[int], bool]) -> None:
    """
    In-place partition nums so that elements with cond(x) == True
    come before those with cond(x) == False.
    Order is not preserved.

    Time: O(n)
    Space: O(1)
    """
    left, right = 0, len(nums) - 1

    while left < right:
        # move left until it finds a bad element
        while left < right and cond(nums[left]):
            left += 1

        # move right until it finds a good element
        while left < right and not cond(nums[right]):
            right -= 1

        if left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

# Example usage:
nums = [3, 1, 2, 4, 5, 6]
condition = lambda x: x < 4
partition_by_condition(nums, condition)
print(nums) # Output could be: [3, 1, 2, 6, 5, 4] (elements < 4 are on the left)

nums = [10, 15, 20, 25, 30, 35]
condition = lambda x: x % 20 == 0
partition_by_condition(nums, condition)
print(nums) # Output could be: [20, 15, 10, 25, 30, 35] (elements divisible by 20 are on the left)