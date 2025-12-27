# Compare Version Numbers using pointer traversal
# Problem: compare version strings like "1.01" and "1.001"
def compare_version(v1: str, v2: str) -> int:
    """
    Returns 1 if v1>v2, -1 if v1<v2, 0 if equal.
    Approach: parse numbers between dots using two pointers without splitting into arrays.
    """
    i, j = 0, 0
    n1, n2 = len(v1), len(v2)
    while i < n1 or j < n2:
        num1 = 0
        while i < n1 and v1[i] != '.':
            num1 = num1 * 10 + ord(v1[i]) - ord('0')
            i += 1
        num2 = 0
        while j < n2 and v2[j] != '.':
            num2 = num2 * 10 + ord(v2[j]) - ord('0')
            j += 1
        if num1 > num2:
            return 1
        if num1 < num2:
            return -1
        i += 1  # skip dot
        j += 1
    return 0

# Example:
# compare_version("1.01","1.001") -> 0
