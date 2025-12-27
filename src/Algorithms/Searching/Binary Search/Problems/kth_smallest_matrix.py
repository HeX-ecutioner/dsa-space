# Find the k-th smallest element in a matrix where rows and columns are sorted
from typing import List

def kth_smallest_in_sorted_matrix(matrix: List[List[int]], k: int) -> int:
    """
    Return the k-th smallest element (1-indexed) in a matrix where each row and
    each column is sorted in ascending order.

    Strategy:
    - Binary search on the value domain [lo, hi] where lo = smallest element,
      hi = largest element.
    - For a candidate mid value, count how many elements in the matrix are <= mid
      using an O(rows + cols) scan from the bottom-left corner.
    - If count < k, we need larger values (lo = mid + 1); else hi = mid.
    - When lo == hi, that's the k-th smallest element.

    Complexity:
    - Counting is O(rows + cols) per iteration; number of iterations is O(log(range)),
      where range = hi - lo.
    """
    if not matrix or not matrix[0]:
        raise ValueError("matrix must be non-empty")

    rows, cols = len(matrix), len(matrix[0])
    lo = matrix[0][0]  # smallest element
    hi = matrix[rows - 1][cols - 1]  # largest element

    def count_leq(x: int) -> int:
        """
        Count elements <= x in O(rows + cols) time.
        Start at bottom-left (row = rows-1, col = 0). If matrix[row][col] <= x,
        then all elements in that column above row are also <= x, so add (row+1)
        and move right. Otherwise move up.
        """
        r = rows - 1
        c = 0
        cnt = 0
        while r >= 0 and c < cols:
            if matrix[r][c] <= x:
                # everything in column c from row 0..r is <= x
                cnt += (r + 1)
                c += 1  # move to next column
            else:
                r -= 1  # move up
        return cnt

    # Binary search on values
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if count_leq(mid) < k:
            lo = mid + 1
        else:
            hi = mid
    return lo


if __name__ == "__main__":
    matrix = [
        [1, 5, 9],
        [10, 11, 13],
        [12, 13, 15],
    ]
    print("k=8 ->", kth_smallest_in_sorted_matrix(matrix, 8))  # expect 13
