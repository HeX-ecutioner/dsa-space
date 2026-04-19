def bubble_sort(arr):
    n = len(arr)

    # Outer loop runs n-1 times
    for i in range(n - 1):
        # Flag to check if any swap happens during this pass
        swapped = False

        # Inner loop: compare adjacent elements
        
        for j in range(n - i - 1): # We go only to n-i-1 because the last i elements are already sorted after each pass

            # If the current element is greater than the next, swap them
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j] # In Python, you can swap without any extra variables
                swapped = True

        # Optimization: if no swaps happened, array is already sorted
        if not swapped:
            break


# Example usage:
if __name__ == "__main__":
    nums = [5, 1, 4, 2, 8]
    bubble_sort(nums)
    print("Sorted array:", nums)  # Output → [1, 2, 4, 5, 8]