def z_algorithm(s: str) -> list:
    """
    Parameters:
    s (str): The input string for which to compute the Z-array.
    
    Returns:
    list: The Z-array of the input string.
    """
    n = len(s)  # Length of the input string
    z = [0] * n  # Initialize Z-array with zeros
    l = r = 0  # Initialize left and right pointers

    for i in range(1, n):
        # If i is within the bounds of the current Z-box
        if i <= r:
            z[i] = min(r - i + 1, z[i - l])  # Use previously computed values
        # Attempt to extend the Z-box
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        # Update the left and right pointers if we found a longer Z-box
        if i + z[i] - 1 > r:
            l, r = i, i + z[i] - 1
    return z

# Example usage:
if __name__ == "__main__":
    input_string = "abacaba"
    z_array = z_algorithm(input_string)
    print(f"Z-array for '{input_string}': {z_array}") # Output: Z-array for 'abacaba': [0, 0, 1, 0, 3, 0, 1]
