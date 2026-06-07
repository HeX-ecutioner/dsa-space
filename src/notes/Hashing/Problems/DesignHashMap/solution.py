class ListNode:
    def __init__(self, key=-1, val=-1, next=None):
        self.key = key
        self.val = val
        self.next = next

class MyHashMap:
    def __init__(self):
        # Array of dummy head nodes
        self.map = [ListNode() for i in range(1000)]

    def _hash(self, key: int) -> int:
        return key % len(self.map)

    def put(self, key: int, value: int) -> None:
        current = self.map[self._hash(key)]
        
        # Traverse to find if key exists or reach the end
        while current.next:
            if current.next.key == key:
                current.next.val = value
                return
            current = current.next
            
        # Key does not exist, append to the end
        current.next = ListNode(key, value)

    def get(self, key: int) -> int:
        current = self.map[self._hash(key)].next
        
        # Traverse list to find key
        while current:
            if current.key == key:
                return current.val
            current = current.next
            
        return -1

    def remove(self, key: int) -> None:
        current = self.map[self._hash(key)]
        
        # Traverse looking ahead to bypass the target node
        while current and current.next:
            if current.next.key == key:
                current.next = current.next.next
                return
            current = current.next

# --- Example Usage ---
# obj = MyHashMap()
# obj.put(1, 1)
# obj.put(2, 2)
# print(obj.get(1))    # Output: 1
# print(obj.get(3))    # Output: -1
# obj.put(2, 1)        # Update value for key 2
# print(obj.get(2))    # Output: 1
# obj.remove(2)        # Remove mapping for key 2
# print(obj.get(2))    # Output: -1
