# Circular Linked List Implementation


class Node:  # Node class represents a single element in the circular linked list.
    def __init__(self, data):
        self.data = data  # The value stored
        self.next = None  # Pointer to next node


class CircularLinkedList:
    def __init__(self):
        self.head = None  # Points to first node
        self.tail = None  # Points to last node
        self.size = 0  # Track number of elements

    # ----------------------------
    # INSERTION OPERATIONS
    # ----------------------------

    def insert_at_beginning(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = self.tail = new_node
            new_node.next = new_node
        else:
            new_node.next = self.head
            self.tail.next = new_node
            self.head = new_node

        self.size += 1

    def insert_at_end(self, data):
        new_node = Node(data)

        if self.tail is None:
            self.head = self.tail = new_node
            new_node.next = new_node
        else:
            new_node.next = self.head
            self.tail.next = new_node
            self.tail = new_node

        self.size += 1

    def insert_at_position(self, data, position):
        if position < 0 or position > self.size:
            print("Invalid position")
            return

        if position == 0:
            self.insert_at_beginning(data)
            return

        if position == self.size:
            self.insert_at_end(data)
            return

        new_node = Node(data)
        curr = self.head

        for _ in range(position - 1):
            curr = curr.next

        new_node.next = curr.next
        curr.next = new_node

        self.size += 1

    # ----------------------------
    # DELETION OPERATIONS
    # ----------------------------

    def delete_from_beginning(self):
        if self.head is None:
            print("List is empty")
            return

        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.tail.next = self.head

        self.size -= 1

    def delete_from_end(self):
        if self.tail is None:
            print("List is empty")
            return

        if self.head == self.tail:
            self.head = self.tail = None
        else:
            curr = self.head
            while curr.next != self.tail:
                curr = curr.next

            curr.next = self.head
            self.tail = curr

        self.size -= 1

    def delete_by_value(self, value):
        if self.head is None:
            print("Value not found")
            return

        curr = self.head
        prev = self.tail

        for _ in range(self.size):
            if curr.data == value:
                if curr == self.head:
                    self.delete_from_beginning()
                elif curr == self.tail:
                    self.delete_from_end()
                else:
                    prev.next = curr.next
                    self.size -= 1
                return
            prev, curr = curr, curr.next

        print("Value not found")

    # ----------------------------
    # UTILITY OPERATIONS
    # ----------------------------

    def search(self, value):
        curr = self.head

        for i in range(self.size):
            if curr.data == value:
                return i
            curr = curr.next

        return -1

    def display(self):
        if self.head is None:
            print("null")
            return

        curr = self.head
        result = []

        for _ in range(self.size):
            result.append(str(curr.data))
            curr = curr.next

        print(" -> ".join(result) + " -> (head)")

    def reverse(self):  # Reverse the circular linked list
        if self.head is None or self.head == self.tail:
            return

        prev = self.tail
        curr = self.head

        for _ in range(self.size):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        self.head, self.tail = self.tail, self.head

    def find_middle(self):  # Using fast/slow pointer technique
        if self.head is None:
            return None

        slow = fast = self.head

        while fast.next != self.head and fast.next.next != self.head:
            slow = slow.next
            fast = fast.next.next

        return slow.data

    def get_size(self):
        return self.size

def main():
    cll = CircularLinkedList()

    while True:
        print(
            "\n--- Circular Linked List Menu ---\n1. Insert at Beginning\n2. Insert at End\n3. Insert at Position\n4. Delete from Beginning"
            "\n5. Delete from End\n6. Delete by Value\n7. Search\n8. Display\n9. Reverse\n10. Find Middle\n11. Size\n0. Exit"
        )

        ch = input("\nEnter choice: ").strip()

        try:
            if ch == "1":
                val = int(input("Enter value: "))
                cll.insert_at_beginning(val)
                print(f"✅ Inserted {val} at beginning")

            elif ch == "2":
                val = int(input("Enter value: "))
                cll.insert_at_end(val)
                print(f"✅ Inserted {val} at end")

            elif ch == "3":
                val = int(input("Enter value: "))
                pos = int(input("Enter position: "))
                cll.insert_at_position(val, pos - 1)
                print(f"✅ Inserted {val} at position {pos}")

            elif ch == "4":
                if cll.head is None:
                    print("❌ List is empty")
                else:
                    print("Before:", end=" ")
                    cll.display()
                    cll.delete_from_beginning()
                    print("✅ Deleted from beginning")
                    print("After:", end=" ")
                    cll.display()

            elif ch == "5":
                if cll.head is None:
                    print("❌ List is empty")
                else:
                    print("Before:", end=" ")
                    cll.display()
                    cll.delete_from_end()
                    print("✅ Deleted from end")
                    print("After:", end=" ")
                    cll.display()

            elif ch == "6":
                val = int(input("Enter value: "))
                if cll.head is None:
                    print("❌ List is empty")
                else:
                    print("Before:", end=" ")
                    cll.display()
                    cll.delete_by_value(val)
                    print(f"✅ Attempted deletion of {val}")
                    print("After:", end=" ")
                    cll.display()

            elif ch == "7":
                val = int(input("Enter value: "))
                index = cll.search(val)
                if index != -1:
                    print(f"✅ Value {val} found at index {index}")
                else:
                    print(f"❌ Value {val} not found")

            elif ch == "8":
                print("📋 Current List:", end=" ")
                cll.display()

            elif ch == "9":
                if cll.head is None:
                    print("❌ List is empty")
                else:
                    print("Before:", end=" ")
                    cll.display()
                    cll.reverse()
                    print("✅ List reversed")
                    print("After:", end=" ")
                    cll.display()

            elif ch == "10":
                mid = cll.find_middle()
                if mid is not None:
                    print(f"📍 Middle element: {mid}")
                else:
                    print("❌ List is empty")

            elif ch == "11":
                print(f"📏 Size of list: {cll.get_size()}")

            elif ch == "0":
                print("👋 Exiting... Goodbye!")
                break

            else:
                print("❌ Invalid choice. Please try again.")

        except ValueError:
            print("❌ Invalid input. Please enter numeric values where required.")


if __name__ == "__main__":
    main() # Example usage
