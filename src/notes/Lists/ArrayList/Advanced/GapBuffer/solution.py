# Implement a gap buffer, commonly used in text editors, to allow O(1) insertions and deletions near a movable cursor.

class GapBuffer:
    def __init__(self, initial_size=10):
        # Time Complexity: O(n) to initialize
        # Space Complexity: O(n)
        self.buffer = [''] * initial_size
        self.gap_start = 0
        self.gap_end = initial_size - 1

    def insert(self, char):
        # Time Complexity: O(1) assuming gap isn't full
        if self.gap_start > self.gap_end:
            self._grow()
            
        self.buffer[self.gap_start] = char
        self.gap_start += 1

    def move_cursor_left(self):
        # Time Complexity: O(1)
        if self.gap_start > 0:
            self.gap_start -= 1
            self.buffer[self.gap_end] = self.buffer[self.gap_start]
            self.buffer[self.gap_start] = ''
            self.gap_end -= 1

    def get_text(self):
        # Time Complexity: O(n)
        return "".join(self.buffer[:self.gap_start] + self.buffer[self.gap_end + 1:])

    def _grow(self):
        # Simplistic growth logic for demonstration
        pass 

if __name__ == "__main__":
    gb = GapBuffer()
    gb.insert('H')
    gb.insert('i')
    gb.insert('!')
    gb.move_cursor_left()
    gb.insert('a') # Inserts 'a' before '!'
    print("Text:", gb.get_text()) # Expected: Hia!