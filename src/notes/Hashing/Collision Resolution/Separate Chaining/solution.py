class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTableSeparateChaining:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.size = 0
        # The array of linked list heads
        self.buckets = [None] * self.capacity

    def _hash(self, key):
        return hash(key) % self.capacity

    def put(self, key, value):
        if self.size >= self.capacity * 0.75:
            self._resize()

        index = self._hash(key)
        head = self.buckets[index]

        # Check if key already exists, update if so
        current = head
        while current:
            if current.key == key:
                current.value = value
                return
            current = current.next

        # Key doesn't exist, insert at the HEAD of the linked list
        new_node = Node(key, value)
        new_node.next = self.buckets[index]
        self.buckets[index] = new_node
        self.size += 1

    def get(self, key):
        index = self._hash(key)
        current = self.buckets[index]

        # Traverse the list to find the key
        while current:
            if current.key == key:
                return current.value
            current = current.next

        return None

    def remove(self, key):
        index = self._hash(key)
        current = self.buckets[index]
        prev = None

        while current:
            if current.key == key:
                # Remove the node
                if prev:
                    prev.next = current.next
                else:
                    # The node to delete is the head
                    self.buckets[index] = current.next
                
                self.size -= 1
                return True
            
            prev = current
            current = current.next

        return False

    def _resize(self):
        old_buckets = self.buckets
        self.capacity *= 2
        self.size = 0
        self.buckets = [None] * self.capacity

        # Rehash all existing elements
        for head in old_buckets:
            current = head
            while current:
                self.put(current.key, current.value)
                current = current.next

# Example Usage
if __name__ == "__main__":
    ht = HashTableSeparateChaining(5)
    ht.put("apple", 100)
    ht.put("banana", 200)
    
    # Force a collision intentionally for demonstration (if we hardcoded hashes)
    # But Python's hash() handles the distribution. Let's just test functionality.
    ht.put("cherry", 300)
    ht.put("date", 400)
    ht.put("elderberry", 500)
    
    print(f"apple: {ht.get('apple')}") # 100
    
    ht.remove("banana")
    print(f"banana after removal: {ht.get('banana')}") # None
