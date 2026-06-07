import random

class RandomizedSet:

    def __init__(self):
        # Hash Map to store {value : index in the list}
        self.val_to_index = {}
        # List to store values for O(1) random access
        self.nums = []

    def insert(self, val: int) -> bool:
        if val in self.val_to_index:
            return False
            
        # Append to the end of the list
        self.nums.append(val)
        # Store its index in the hash map
        self.val_to_index[val] = len(self.nums) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.val_to_index:
            return False
            
        # To delete in O(1) without shifting elements in the array:
        # 1. Swap the element to delete with the last element in the array
        idx_to_remove = self.val_to_index[val]
        last_element = self.nums[-1]
        
        # Move the last element to the spot we are deleting
        self.nums[idx_to_remove] = last_element
        self.val_to_index[last_element] = idx_to_remove
        
        # 2. Pop the last element (which is now our target 'val')
        self.nums.pop()
        del self.val_to_index[val]
        
        return True

    def getRandom(self) -> int:
        # random.choice is O(1) because it generates a random index and accesses the list
        return random.choice(self.nums)

# --- Example Usage ---
# obj = RandomizedSet()
# print(obj.insert(1))   # Output: True
# print(obj.remove(2))   # Output: False
# print(obj.insert(2))   # Output: True
# print(obj.getRandom()) # Output: 1 or 2 randomly
# print(obj.remove(1))   # Output: True
# print(obj.insert(2))   # Output: False
# print(obj.getRandom()) # Output: 2
