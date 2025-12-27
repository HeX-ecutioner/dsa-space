def selection_sort(arr):
    n = len(arr)

    # Loop over each index where the correct element should go
    for i in range(n):
        min_index = i  # Assume the current position contains the minimum

        # Find the index of the smallest element in the remaining array
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Swap the smallest element found with the element at index i
        arr[i], arr[min_index] = arr[min_index], arr[i]


# Example usage:
if __name__ == "__main__":
    nums = [64, 25, 12, 22, 11]
    selection_sort(nums)
    print("Sorted array:", nums)  # Output → [11, 12, 22, 25, 64]
