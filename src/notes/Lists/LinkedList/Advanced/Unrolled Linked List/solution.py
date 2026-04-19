class Node:
    """
    Each node stores:
    - elements → list of values
    - next → pointer to next node
    """

    def __init__(self, capacity):
        self.elements = []
        self.next = None
        self.capacity = capacity


class UnrolledLinkedList:
    def __init__(self, capacity=4):
        self.head = Node(capacity)
        self.capacity = capacity
        self.size = 0

    def insert(self, value): # Insert at end (most common operation)
        curr = self.head

        while curr:
            # If space available, insert here
            if len(curr.elements) < self.capacity:
                curr.elements.append(value)
                self.size += 1
                return

            # Move to next node
            if curr.next is None:
                break
            curr = curr.next

        # Node full → split
        new_node = Node(self.capacity)

        mid = len(curr.elements) // 2
        new_node.elements = curr.elements[mid:]
        curr.elements = curr.elements[:mid]

        new_node.next = curr.next
        curr.next = new_node

        # Insert into appropriate node
        if len(curr.elements) < self.capacity:
            curr.elements.append(value)
        else:
            new_node.elements.append(value)

        self.size += 1

    def delete(self, value):
        curr = self.head

        while curr:
            if value in curr.elements:
                curr.elements.remove(value)
                self.size -= 1
                return
            curr = curr.next

        print("❌ Value not found")

    def search(self, value):
        curr = self.head

        while curr:
            if value in curr.elements:
                return True
            curr = curr.next

        return False

    def display(self):
        curr = self.head
        print("\n📋 Unrolled Linked List:")

        while curr:
            print(curr.elements, end=" -> ")
            curr = curr.next

        print("None")

    def get_size(self):
        return self.size


def main():
    ull = UnrolledLinkedList()

    while True:
        print(
            "\n--- Unrolled Linked List Menu ---\n1. Insert\n2. Delete\n3. Search\n4. Display\n5. Size\n6. Exit"
        )

        ch = input("\nEnter choice: ").strip()

        try:
            if ch == "1":
                val = int(input("Enter value: "))
                ull.insert(val)
                print(f"✅ Inserted {val}")

            elif ch == "2":
                val = int(input("Enter value: "))
                ull.delete(val)

            elif ch == "3":
                val = int(input("Enter value: "))
                found = ull.search(val)
                print("✅ Found" if found else "❌ Not found")

            elif ch == "4":
                ull.display()

            elif ch == "5":
                print(f"📏 Size: {ull.get_size()}")

            elif ch == "6":
                print("👋 Exiting...")
                break

            else:
                print("❌ Invalid choice")

        except ValueError:
            print("❌ Invalid input")


if __name__ == "__main__":
    main() # Example usage
