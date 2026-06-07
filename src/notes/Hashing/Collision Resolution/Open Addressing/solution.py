class HashTableLinearProbing:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.size = 0
        # We store keys and values in parallel arrays (or tuples in a single array)
        self.keys = [None] * self.capacity
        self.values = [None] * self.capacity
        # Tombstone marker for deleted elements
        self.TOMBSTONE = "<DELETED>"

    def _hash(self, key):
        return hash(key) % self.capacity

    def put(self, key, value):
        if self.size >= self.capacity * 0.7:
            self._resize()

        index = self._hash(key)
        
        # Linear probing: continue while slot is occupied by a real key
        # (We can overwrite tombstones)
        while self.keys[index] is not None and self.keys[index] != self.TOMBSTONE:
            # If the key already exists, update its value
            if self.keys[index] == key:
                self.values[index] = value
                return
            index = (index + 1) % self.capacity

        # Insert at the found empty or tombstone slot
        self.keys[index] = key
        self.values[index] = value
        self.size += 1

    def get(self, key):
        index = self._hash(key)

        # Probe until we find an empty slot (None)
        while self.keys[index] is not None:
            if self.keys[index] == key:
                return self.values[index]
            index = (index + 1) % self.capacity

        return None

    def remove(self, key):
        index = self._hash(key)

        while self.keys[index] is not None:
            if self.keys[index] == key:
                # Mark as tombstone instead of None to not break the probe chain
                self.keys[index] = self.TOMBSTONE
                self.values[index] = None
                self.size -= 1
                return True
            index = (index + 1) % self.capacity

        return False

    def _resize(self):
        old_keys = self.keys
        old_values = self.values
        
        self.capacity *= 2
        self.size = 0
        self.keys = [None] * self.capacity
        self.values = [None] * self.capacity

        # Rehash all existing elements into the new array
        for i in range(len(old_keys)):
            k = old_keys[i]
            if k is not None and k != self.TOMBSTONE:
                self.put(k, old_values[i])

# Example Usage
if __name__ == "__main__":
    ht = HashTableLinearProbing(5)
    ht.put("apple", 100)
    ht.put("banana", 200)
    ht.put("cherry", 300)
    
    print(f"apple: {ht.get('apple')}") # 100
    
    # Removing an element
    ht.remove("banana")
    print(f"banana after removal: {ht.get('banana')}") # None
    
    # "cherry" can still be found even though "banana" was removed, thanks to the tombstone
    print(f"cherry: {ht.get('cherry')}") # 300
