class MyHashSet:
    def __init__(self):
        # Using 1000 buckets
        self.num_buckets = 1000
        # Initialize buckets with empty lists
        self.buckets = [[] for _ in range(self.num_buckets)]

    def _hash(self, key: int) -> int:
        return key % self.num_buckets

    def add(self, key: int) -> None:
        bucket_index = self._hash(key)
        
        # Only add if it doesn't already exist (Set property)
        if key not in self.buckets[bucket_index]:
            self.buckets[bucket_index].append(key)

    def remove(self, key: int) -> None:
        bucket_index = self._hash(key)
        
        # Remove if it exists
        if key in self.buckets[bucket_index]:
            self.buckets[bucket_index].remove(key)

    def contains(self, key: int) -> bool:
        bucket_index = self._hash(key)
        return key in self.buckets[bucket_index]

# --- Example Usage ---
# obj = MyHashSet()
# obj.add(1)
# obj.add(2)
# print(obj.contains(1)) # Output: True
# print(obj.contains(3)) # Output: False
# obj.add(2)             # Does nothing, 2 already exists
# print(obj.contains(2)) # Output: True
# obj.remove(2)
# print(obj.contains(2)) # Output: False
