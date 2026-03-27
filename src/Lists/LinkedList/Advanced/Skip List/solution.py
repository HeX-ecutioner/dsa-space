import random

MAX_LEVEL = 4  # Maximum number of levels
P = 0.5  # Probability for level generation


class Node:
    """
    Each node contains:
    - value → stored data
    - forward → list of pointers (one for each level)
    """

    def __init__(self, value, level):
        self.value = value
        self.forward = [None] * (level + 1)


class SkipList:
    def __init__(self):
        self.level = 0  # Current highest level
        self.header = Node(-1, MAX_LEVEL)  # Sentinel node


    def random_level(self): # Randomly generate level for a new node. With probability P, node goes to higher level
        lvl = 0
        while random.random() < P and lvl < MAX_LEVEL:
            lvl += 1
        return lvl
    

    def insert(self, value):
        update = [None] * (MAX_LEVEL + 1)
        curr = self.header

        # Step 1: Find positions to update
        for i in range(self.level, -1, -1):
            while curr.forward[i] and curr.forward[i].value < value:
                curr = curr.forward[i]
            update[i] = curr

        curr = curr.forward[0]

        # Step 2: Insert if not duplicate
        if curr is None or curr.value != value:
            lvl = self.random_level()

            # If new level is higher, initialize update
            if lvl > self.level:
                for i in range(self.level + 1, lvl + 1):
                    update[i] = self.header
                self.level = lvl

            new_node = Node(value, lvl)

            # Step 3: Re-link pointers
            for i in range(lvl + 1):
                new_node.forward[i] = update[i].forward[i]
                update[i].forward[i] = new_node


    def search(self, value):
        curr = self.header

        for i in range(self.level, -1, -1):
            while curr.forward[i] and curr.forward[i].value < value:
                curr = curr.forward[i]

        curr = curr.forward[0]

        return curr is not None and curr.value == value


    def delete(self, value):
        update = [None] * (MAX_LEVEL + 1)
        curr = self.header

        for i in range(self.level, -1, -1):
            while curr.forward[i] and curr.forward[i].value < value:
                curr = curr.forward[i]
            update[i] = curr

        curr = curr.forward[0]

        if curr and curr.value == value:
            for i in range(self.level + 1):
                if update[i].forward[i] != curr:
                    break
                update[i].forward[i] = curr.forward[i]

            # Adjust level if needed
            while self.level > 0 and self.header.forward[self.level] is None:
                self.level -= 1


    def display(self): # Display all levels of skip list
        print("\n📊 Skip List Levels:")
        for i in range(self.level, -1, -1):
            curr = self.header.forward[i]
            print(f"Level {i}:", end=" ")
            while curr:
                print(curr.value, end=" -> ")
                curr = curr.forward[i]
            print("None")


def main():
    sl = SkipList()

    while True:
        print("\n--- Skip List Menu ---\n1. Insert\n2. Delete\n3. Search\n4. Display\n5. Exit")

        ch = input("\nEnter choice: ").strip()

        try:
            if ch == "1":
                val = int(input("Enter value: "))
                sl.insert(val)
                print(f"✅ Inserted {val}")

            elif ch == "2":
                val = int(input("Enter value: "))
                sl.delete(val)
                print(f"✅ Attempted deletion of {val}")

            elif ch == "3":
                val = int(input("Enter value: "))
                found = sl.search(val)
                print("✅ Found" if found else "❌ Not found")

            elif ch == "4":
                sl.display()

            elif ch == "5":
                print("👋 Exiting...")
                break

            else:
                print("❌ Invalid choice")

        except ValueError:
            print("❌ Invalid input")


if __name__ == "__main__":
    main() # Example usage
