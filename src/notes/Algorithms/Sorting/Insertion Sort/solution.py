def insertion_sort(arr):
    n = len(arr)

    # Start from index 1 because a single element (index 0) is already "sorted"
    for i in range(1, n):
        key = arr[i]  # Element to be inserted into the sorted left portion
        j = i - 1

        # Shift elements to the right until the correct position is found
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]  # Move larger element right
            j -= 1

        # Insert the key in the correct position
        arr[j + 1] = key


# Example usage:
if __name__ == "__main__":
    nums = [12, 11, 13, 5, 6]
    insertion_sort(nums)
    print("Sorted array:", nums)  # Output → [5, 6, 11, 12, 13]
