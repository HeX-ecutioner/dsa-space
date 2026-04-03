from typing import List

def longest_mountain(arr: List[int]) -> int:
    """
    A mountain: strictly increasing then strictly decreasing, length >=3.
    Approach: scan each possible peak by finding increasing run to left and decreasing run to right.
    Optimize by skipping processed segments.
    Time: O(n)
    """
    n = len(arr)
    best = 0
    i = 1
    while i < n - 1:
        # check if arr[i] is peak
        if arr[i-1] < arr[i] > arr[i+1]:
            left = i - 1 # expand left
            while left > 0 and arr[left-1] < arr[left]:
                left -= 1
            right = i + 1 # expand right
            while right < n - 1 and arr[right] > arr[right+1]:
                right += 1
            best = max(best, right - left + 1)
            i = right + 1 # skip to right+1 for efficiency
        else:
            i += 1
    return best

# Example usage:
print(longest_mountain([2,1,4,7,3,2,5])) # Output: 5 (1,4,7,3,2)
print(longest_mountain([2,2,2])) # Output: 0 (no mountain)