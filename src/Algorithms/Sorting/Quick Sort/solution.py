def quick_sort(arr, low, high):
    if low < high:
        # Partition the array and get the pivot index
        pivot_index = partition(arr, low, high)

        # Recursively sort the left part
        quick_sort(arr, low, pivot_index - 1)

        # Recursively sort the right part
        quick_sort(arr, pivot_index + 1, high)


def partition(arr, low, high):
    """
    This function follows the Lomuto Partition Scheme:
    - Choose the last element as the pivot.
    - Move all smaller elements to the left side.
    - Place pivot in its correct sorted position.

    Returns:
        The index where the pivot ends up.
    """

    pivot = arr[high]    # Pivot chosen as the last element
    i = low - 1          # Index of the smaller element section

    # Traverse the array and compare each element with the pivot
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]   # Pythonic swap

    # Place pivot just after the last smaller element
    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    return i + 1   # Return pivot's final position


# Example usage:
if __name__ == "__main__":
    nums = [10, 7, 8, 9, 1, 5]
    quick_sort(nums, 0, len(nums) - 1)
    print("Sorted array:", nums)  # Output → [1, 5, 7, 8, 9, 10]
