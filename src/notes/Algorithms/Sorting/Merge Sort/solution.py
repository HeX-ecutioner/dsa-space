def merge_sort(arr):
    # Base case: A list of length 0 or 1 is already sorted.
    if len(arr) <= 1:
        return arr

    # Step 1: Divide the array into left and right halves
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])  # Recursively sort left half
    right_half = merge_sort(arr[mid:])  # Recursively sort right half

    # Step 2: Merge the sorted halves
    return merge(left_half, right_half)


def merge(left, right):

    result = []
    i = j = 0

    # Compare elements from both lists
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Append any leftover elements
    result.extend(left[i:])
    result.extend(right[j:])

    return result


# Example usage:
if __name__ == "__main__":
    nums = [38, 27, 43, 3, 9, 82, 10]
    sorted_nums = merge_sort(nums) # We need to store the result in a new array
    print("Sorted array:", sorted_nums)  # Output → [3, 9, 10, 27, 38, 43, 82]
