# Demonstrate the structural concept of a Hashed Array Tree (HAT) which avoids the massive O(N) copy penalty of standard dynamic arrays by keeping an array of pointers to smaller, fixed-size data "chunks"

class SimpleHashedArrayTree:
    # Time Complexity: O(1) amortized append.
    # Space Complexity: O(N) with much less wasted overhead than doubling an array.
    
    def __init__(self, chunk_size=4):
        self.chunk_size = chunk_size
        self.directory = [[]] # Array of arrays (chunks)
        self.size = 0

    def append(self, value):
        # Calculate which chunk this belongs to based on current size
        current_chunk = self.size // self.chunk_size
        
        # If the directory doesn't have this chunk yet, allocate a new empty chunk
        if current_chunk >= len(self.directory):
            self.directory.append([])
            
        self.directory[current_chunk].append(value)
        self.size += 1

    def get(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
            
        chunk_idx = index // self.chunk_size
        element_idx = index % self.chunk_size
        return self.directory[chunk_idx][element_idx]

if __name__ == "__main__":
    hat = SimpleHashedArrayTree(chunk_size=3)
    for i in range(1, 8):
        hat.append(i * 10)
        
    print("Underlying HAT structure:", hat.directory) 
    # Expected: [[10, 20, 30], [40, 50, 60], [70]]
    print("Get index 4:", hat.get(4)) # Expected: 50