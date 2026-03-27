# Circular Singly Linked List (Tail Pointer Only)


class Node:
    # Represents a single node in the list
    def __init__(self, data):
        self.data = data
        self.next = None  # Points to next node


class CircularSLL:
    def __init__(self):
        self.tail = None  # Only tail is stored
        self.size = 0

    def insert_at_beginning(self, data):
        new_node = Node(data)

        # Case 1: Empty list
        if self.tail is None:
            self.tail = new_node
            new_node.next = new_node  # Points to itself
        else:
            # Insert after tail, but before head
            new_node.next = self.tail.next
            self.tail.next = new_node

        self.size += 1

    def insert_at_end(self, data):
        new_node = Node(data)

        if self.tail is None:
            self.tail = new_node
            new_node.next = new_node
        else:
            # Insert after tail
            new_node.next = self.tail.next
            self.tail.next = new_node
            self.tail = new_node  # Move tail forward

        self.size += 1

    def delete_from_beginning(self):
        if self.tail is None:
            print("❌ List is empty")
            return

        head = self.tail.next

        # Single node case
        if self.tail == head:
            self.tail = None
        else:
            self.tail.next = head.next  # Skip head

        self.size -= 1

    def delete_from_end(self):
        if self.tail is None:
            print("❌ List is empty")
            return

        curr = self.tail.next  # Start from head

        # Single node case
        if curr == self.tail:
            self.tail = None
            self.size -= 1
            return

        # Traverse to node before tail
        while curr.next != self.tail:
            curr = curr.next

        curr.next = self.tail.next  # Link to head
        self.tail = curr  # Update tail

        self.size -= 1

    def search(self, value):
        if self.tail is None:
            return -1

        curr = self.tail.next  # Start from head
        index = 0

        while True:
            if curr.data == value:
                return index

            curr = curr.next
            index += 1

            if curr == self.tail.next:
                break

        return -1

    def display(self):
        if self.tail is None:
            print("null")
            return

        curr = self.tail.next  # Start from head

        while True:
            print(curr.data, end=" -> ")
            curr = curr.next

            if curr == self.tail.next:
                break

        print("(head)")

    def get_size(self):
        return self.size


def main():
    cll = CircularSLL()

    while True:
        print(
            "--- Circular SLL (Tail Pointer Only) ---\n1. Insert at Beginning\n2. Insert at End\n3. Delete from Beginning\n"
            "4. Delete from End\n5. Search\n6. Display\n7. Size\n8. Exit\n"
        )

        ch = input("Enter choice: ").strip()

        try:
            if ch == "1":
                cll.insert_at_beginning(int(input("Value: ")))

            elif ch == "2":
                cll.insert_at_end(int(input("Value: ")))

            elif ch == "3":
                cll.delete_from_beginning()

            elif ch == "4":
                cll.delete_from_end()

            elif ch == "5":
                val = int(input("Value: "))
                print("Index:", cll.search(val))

            elif ch == "6":
                cll.display()

            elif ch == "7":
                print("Size:", cll.get_size())

            elif ch == "8":
                print("👋 Exiting...")
                break
            else:
                print("❌ Invalid choice")
        except ValueError:
            print("❌ Invalid input")


if __name__ == "__main__":
    main()  # Example usage
