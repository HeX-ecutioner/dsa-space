def next_greater_element(arr):
    """
    For each element in the array, find the next greater element to its right.
    If no such element exists, return -1 for that position.

    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    stack = []                       # stack to store indices
    result = [-1] * len(arr)         # default result

    for i in range(len(arr)):
        # Resolve all elements smaller than current
        while stack and arr[stack[-1]] < arr[i]:
            idx = stack.pop()
            result[idx] = arr[i]

        # Push current index
        stack.append(i)

    return result

# Example usage:
arr = [4, 5, 2, 10, 8]
print(next_greater_element(arr)) # Output: [5, 10, 10, -1, -1]