# Problem: Sort Colors (of the Dutch National Flag) - Given array with values 0,1,2. Sort them in-place.
from typing import List

def sort_colors(nums: List[int]) -> None:
    """
    Three pointers: low for 0 zone, mid for current, high for 2 zone.
    Steps:
    - mid iterates through array
    - if nums[mid]==0 -> swap with low, low+=1, mid+=1
    - if nums[mid]==1 -> mid+=1
    - if nums[mid]==2 -> swap with high, high-=1 (do NOT mid+=1 here)
    Time: O(n), Space: O(1)
    """
    low, mid, high = 0, 0, len(nums) - 1
    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:  # nums[mid] == 2
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1

# Example usage:
if __name__ == "__main__":
    arr = [2, 0, 2, 1, 1, 0]
    sort_colors(arr)
    print(arr)  # Output: [0, 0, 1, 1, 2, 2]