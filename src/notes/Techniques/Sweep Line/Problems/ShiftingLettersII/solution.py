# Problem: You are given a string s of lowercase English letters and a 2D integer array shifts. Return the final string after all such shifts to s are applied.
def shiftingLetters(s, shifts):
    """
    Approach: Difference Array / Sweep Line.
    Time: O(N)
    Space: O(N)
    """
    n = len(s)
    diff = [0] * (n + 1)
    for start, end, direction in shifts:
        shift_val = 1 if direction == 1 else -1
        diff[start] += shift_val
        diff[end + 1] -= shift_val
    res = []
    current_shift = 0
    for i in range(n):
        current_shift += diff[i]
        new_char = chr(((ord(s[i]) - ord('a') + current_shift) % 26) + ord('a'))
        res.append(new_char)
    return "".join(res)
