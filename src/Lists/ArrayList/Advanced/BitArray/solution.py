# Implement a memory-efficient array of boolean values (True/False) by packing multiple boolean flags into a single integer using bitwise operations.

class BitArray:
    # Time Complexity: O(1) for getting and setting bits.
    # Space Complexity: O(N/32) or O(N/64) depending on the system's integer size.
    
    def __init__(self, size):
        self.size = size
        # We need size // 32 + 1 integers to hold all the bits
        # (Assuming 32 bits per integer for this mental model)
        self.array = [0] * ((size // 32) + 1)

    def set(self, index):
        if index < 0 or index >= self.size: raise IndexError()
        array_idx = index // 32
        bit_idx = index % 32
        # Use bitwise OR to set the specific bit to 1
        self.array[array_idx] |= (1 << bit_idx)

    def get(self, index):
        if index < 0 or index >= self.size: raise IndexError()
        array_idx = index // 32
        bit_idx = index % 32
        # Use bitwise AND to check if the specific bit is 1
        return (self.array[array_idx] & (1 << bit_idx)) != 0

if __name__ == "__main__":
    # A standard boolean array of 100 items would take 100 bytes.
    # This BitArray only takes an array of 4 integers!
    bitset = BitArray(100)
    bitset.set(45)
    
    print("Is index 45 true?", bitset.get(45)) # Expected: True
    print("Is index 46 true?", bitset.get(46)) # Expected: False