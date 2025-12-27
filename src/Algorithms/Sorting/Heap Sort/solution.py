def heap_sort(arr):
    """
    Python uses index arithmetic to navigate the heap:
        left child = 2*i + 1
        right child = 2*i + 2
    """

    n = len(arr)

    # Step 1: Build max heap
    for i in range(n // 2 - 1, -1, -1): # (Start from last non-leaf node and heapify each root)
        heapify(arr, n, i)

    # Step 2: Extract elements from heap one by one
    for i in range(n - 1, 0, -1):
        # Move current max (root) to the end
        arr[0], arr[i] = arr[i], arr[0]

        # Restore heap property on the reduced heap
        heapify(arr, i, 0)


def heapify(arr, heap_size, i):
    # This function ensures that the subtree rooted at index `i` obeys the max-heap property
    """
    Parameters:
        arr        - the array representing the heap
        heap_size  - number of elements still in the heap
        i          - index of the root of the subtree to fix

    Steps:
    - Compare root with its left and right children.
    - Swap with the larger child if needed.
    - Recursively heapify the affected subtree.
    """

    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    # Check if left child exists and is greater than root
    if left < heap_size and arr[left] > arr[largest]:
        largest = left

    # Check if right child exists and is greater than current largest
    if right < heap_size and arr[right] > arr[largest]:
        largest = right

    # If the root is not the largest, swap and continue heapifying
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, heap_size, largest)

# Example usage:
if __name__ == "__main__":
    nums = [12, 11, 13, 5, 6, 7]
    heap_sort(nums)
    print("Sorted array:", nums)  # Output → [5, 6, 7, 11, 12, 13]
