def counting_sort(arr, exp):
    """
    Counting Sort used as a subroutine for Radix Sort.
    -------------------------------------------------
    exp = 1 → sort by ones place
    exp = 10 → sort by tens place
    exp = 100 → sort by hundreds place

    This is NOT full counting sort — it's specifically adapted to sort digits 0–9.
    """

    n = len(arr)
    output = [0] * n  # Output array (final sorted form for this digit)
    count = [0] * 10  # Count array for digits 0–9

    # Count how many times each digit appears
    for number in arr:
        digit = (number // exp) % 10
        count[digit] += 1

    # Convert count[i] to actual positions (prefix sum)
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Build the output array (iterate backwards for stability)
    for i in range(n - 1, -1, -1):
        digit = (arr[i] // exp) % 10
        output[count[digit] - 1] = arr[i]
        count[digit] -= 1

    # Copy sorted values back to original array
    for i in range(n):
        arr[i] = output[i]


def radix_sort(arr):
    # Sorts integers by processing digits from least significant to most significant using Counting Sort as a stable subroutine
    if len(arr) == 0:
        return arr

    # Find the maximum number to know how many digits we need to sort
    max_num = max(arr)

    exp = 1  # exponent representing current digit place (1s, 10s, 100s...)
    while max_num // exp > 0:
        counting_sort(arr, exp)
        exp *= 10


# Example usage:
if __name__ == "__main__":
    nums = [170, 45, 75, 90, 802, 24, 2, 66]
    radix_sort(nums)
    print("Sorted array:", nums)  # Output → [2, 24, 45, 66, 75, 90, 170, 802]
