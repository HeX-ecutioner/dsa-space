# Doubly Linked List Implementation


class Node:  # Node class represents a single element in the doubly linked list.
    def __init__(self, data):
        self.data = data  # The value stored
        self.prev = None  # Pointer to previous node
        self.next = None  # Pointer to next node


class DoublyLinkedList:
    def __init__(self):
        self.head = None  # Points to first node
        self.tail = None  # Points to last node
        self.size = 0  # Track number of elements

    # ----------------------------
    # INSERTION OPERATIONS
    # ----------------------------

    def insert_at_beginning(self, data):
        new_node = Node(data)

        if self.head is None:  # If list is empty
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

        self.size += 1

    def insert_at_end(self, data):
        new_node = Node(data)

        if self.tail is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
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

        for _ in range(position):
            curr = curr.next

        prev_node = curr.prev
        prev_node.next = new_node
        new_node.prev = prev_node
        new_node.next = curr
        curr.prev = new_node

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
            self.head.prev = None

        self.size -= 1

    def delete_from_end(self):
        if self.tail is None:
            print("List is empty")
            return

        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None

        self.size -= 1

    def delete_by_value(self, value):
        curr = self.head

        while curr:
            if curr.data == value:
                if curr == self.head:
                    self.delete_from_beginning()
                elif curr == self.tail:
                    self.delete_from_end()
                else:
                    curr.prev.next = curr.next
                    curr.next.prev = curr.prev
                    self.size -= 1
                return

            curr = curr.next

        print("Value not found")

    # ----------------------------
    # UTILITY OPERATIONS
    # ----------------------------

    def search(self, value):
        curr = self.head
        index = 0

        while curr:
            if curr.data == value:
                return index
            curr = curr.next
            index += 1

        return -1

    def display_forward(self):
        curr = self.head
        result = []

        while curr:
            result.append(str(curr.data))
            curr = curr.next

        print(" <-> ".join(result) + " <-> null" if result else "null")

    def display_backward(self):
        curr = self.tail
        result = []

        while curr:
            result.append(str(curr.data))
            curr = curr.prev

        print(" <-> ".join(result) + " <-> null" if result else "null")

    def reverse(self):  # Reverse the doubly linked list
        curr = self.head
        self.head, self.tail = self.tail, self.head

        while curr:
            curr.prev, curr.next = curr.next, curr.prev
            curr = curr.prev

    def find_middle(self):  # Using fast/slow pointer technique
        slow = fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow.data if slow else None

    def get_size(self):
        return self.size  # Return number of elements

def main():
    dll = DoublyLinkedList()

    while True:
        print(
            "\n--- Doubly Linked List Menu ---\n1. Insert at Beginning\n2. Insert at End\n3. Insert at Position\n4. Delete from Beginning"
            "\n5. Delete from End\n6. Delete by Value\n7. Search\n8. Display Forward\n9. Display Backward\n10. Reverse\n11. Find Middle" \
            "\n12. Size\n0. Exit"
        )

        ch = input("\nEnter choice: ").strip()

        try:
            if ch == "1":
                val = int(input("Enter value: "))
                dll.insert_at_beginning(val)
                print(f"✅ Inserted {val} at beginning")

            elif ch == "2":
                val = int(input("Enter value: "))
                dll.insert_at_end(val)
                print(f"✅ Inserted {val} at end")

            elif ch == "3":
                val = int(input("Enter value: "))
                pos = int(input("Enter position: "))
                dll.insert_at_position(val, pos - 1)
                print(f"✅ Inserted {val} at position {pos}")

            elif ch == "4":
                if dll.head is None:
                    print("❌ List is empty")
                else:
                    print("Before:", end=" ")
                    dll.display_forward()
                    dll.delete_from_beginning()
                    print("✅ Deleted from beginning")
                    print("After:", end=" ")
                    dll.display_forward()

            elif ch == "5":
                if dll.head is None:
                    print("❌ List is empty")
                else:
                    print("Before:", end=" ")
                    dll.display_forward()
                    dll.delete_from_end()
                    print("✅ Deleted from end")
                    print("After:", end=" ")
                    dll.display_forward()

            elif ch == "6":
                val = int(input("Enter value: "))
                if dll.head is None:
                    print("❌ List is empty")
                else:
                    print("Before:", end=" ")
                    dll.display_forward()
                    dll.delete_by_value(val)
                    print(f"✅ Attempted deletion of {val}")
                    print("After:", end=" ")
                    dll.display_forward()

            elif ch == "7":
                val = int(input("Enter value: "))
                index = dll.search(val)
                if index != -1:
                    print(f"✅ Value {val} found at index {index}")
                else:
                    print(f"❌ Value {val} not found")

            elif ch == "8":
                print("📋 Forward:", end=" ")
                dll.display_forward()

            elif ch == "9":
                print("📋 Backward:", end=" ")
                dll.display_backward()

            elif ch == "10":
                if dll.head is None:
                    print("❌ List is empty")
                else:
                    print("Before:", end=" ")
                    dll.display_forward()
                    dll.reverse()
                    print("✅ List reversed")
                    print("After:", end=" ")
                    dll.display_forward()

            elif ch == "11":
                mid = dll.find_middle()
                if mid is not None:
                    print(f"📍 Middle element: {mid}")
                else:
                    print("❌ List is empty")

            elif ch == "12":
                print(f"📏 Size of list: {dll.get_size()}")

            elif ch == "0":
                print("👋 Exiting... Goodbye!")
                break

            else:
                print("❌ Invalid choice. Please try again.")

        except ValueError:
            print("❌ Invalid input. Please enter numeric values where required.")


if __name__ == "__main__":
    main() # Example usage
