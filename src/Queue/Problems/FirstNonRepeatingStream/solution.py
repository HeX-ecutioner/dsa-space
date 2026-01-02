# Problem: Given a stream of characters, return a list where each element represents the first non-repeating character seen so far
from collections import deque

def first_non_repeating_stream(stream):
    """
    If no such character exists at any point, return -1 for that step.
    Uses a queue to maintain the order of potential non-repeating characters.

    Time Complexity: O(n)
    Space Complexity: O(1)
    (bounded by character set size)
    """
    freq = {} # Frequency of characters
    queue = deque() # Queue to store candidates
    result = []

    for ch in stream:
        # Update frequency
        freq[ch] = freq.get(ch, 0) + 1

        # Add to queue if first occurrence
        if freq[ch] == 1:
            queue.append(ch)

        # Remove repeating characters from front
        while queue and freq[queue[0]] > 1:
            queue.popleft()

        # Append current first non-repeating character
        result.append(queue[0] if queue else -1)

    return result


# Example usage:
stream = "aabc"
print(first_non_repeating_stream(stream)) # Output: ['a', -1, 'b', 'b']